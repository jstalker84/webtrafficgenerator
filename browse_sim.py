#!/usr/bin/env python3
"""browse_sim.py
A human-like web browsing traffic generator with optional compromised-host simulation.
"""

import argparse
import asyncio
import json
import logging
import os
import random
import re
import socket
import string
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

from fake_useragent import UserAgent
from pythonjsonlogger import jsonlogger
from tqdm import tqdm

# Import playwright lazily – allows the script to run even if the package is missing
try:
    from playwright.async_api import async_playwright, Page, BrowserContext
except ImportError as e:  # pragma: no cover – playwright might be unavailable during linting
    print("[!] Playwright not found; please install with 'pip install -r requirements.txt' and run 'playwright install chromium'.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
LOGGER = logging.getLogger("browse_sim")
LOGGER.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s")
_handler.setFormatter(_formatter)
LOGGER.addHandler(_handler)

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

DURATION_PATTERN = re.compile(r"^(?P<value>\d+)(?P<unit>[smh])$")

def parse_duration(dur: str) -> timedelta:
    """Parse duration strings like '30m', '45s', '2h' into a timedelta."""
    match = DURATION_PATTERN.fullmatch(dur.lower())
    if not match:
        raise argparse.ArgumentTypeError("Duration must be in format <number>[s/m/h], e.g., 30m or 2h")
    value = int(match.group("value"))
    unit = match.group("unit")
    if unit == "s":
        return timedelta(seconds=value)
    if unit == "m":
        return timedelta(minutes=value)
    if unit == "h":
        return timedelta(hours=value)
    raise ValueError("Invalid duration unit")


def load_sites(path: Path) -> List[str]:
    """Read site list from file, ignoring comment lines."""
    if not path.exists():
        LOGGER.warning("Site file %s not found.", path)
        return []
    sites = []
    with path.open() as fp:
        for line in fp:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            sites.append(line)
    random.shuffle(sites)
    return sites


def random_user_agent() -> str:
    """Return a realistic random user agent string."""
    try:
        return UserAgent().random  # type: ignore[return-value]
    except Exception:
        # Fallback minimal list
        return random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
        ])


def jitter(base: float, variance: float = 0.3) -> float:
    """Return a time in seconds around base ± variance*base."""
    return max(0.1, random.uniform(base * (1 - variance), base * (1 + variance)))


# ---------------------------------------------------------------------------
# Compromised host simulations
# ---------------------------------------------------------------------------

aSYNC_DEF_TYPE = "async def"  # marker to allow static type hints in older editors

async def beacon_to_c2(url: str, session_id: str) -> None:
    """Simple periodic GET requests to emulate C2 beaconing."""
    LOGGER.info("c2_beacon", extra={"event": "c2_beacon", "url": url, "session_id": session_id})
    try:
        reader, writer = await asyncio.open_connection(socket.gethostbyname(url.split("//")[-1]), 80)
        writer.write(f"GET / HTTP/1.1\r\nHost: {url}\r\nUser-Agent: simulate-bot\r\n\r\n".encode())
        await writer.drain()
        await asyncio.sleep(0.5)
        writer.close()
        await writer.wait_closed()
    except Exception as exc:
        LOGGER.warning("C2 beacon error", extra={"event": "c2_error", "error": str(exc)})


async def download_malware(url: str, session_id: str) -> None:
    """Pretend to download malware (fetch content but discard)."""
    import aiohttp  # import here to keep global deps minimal

    LOGGER.info("malware_download", extra={"event": "malware_download", "url": url, "session_id": session_id})
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(url, timeout=15) as r:
                await r.read()  # discard
    except Exception as exc:
        LOGGER.warning("Malware download error", extra={"event": "malware_error", "error": str(exc)})


async def port_scan(target_prefix: str, session_id: str) -> None:
    """Perform a lightweight port scan of a /24 network (just few ports)."""
    ports = [22, 80, 443]
    for host_octet in random.sample(range(1, 255), 5):  # scan 5 hosts max
        ip = f"{target_prefix}.{host_octet}"
        for port in ports:
            LOGGER.info("port_scan_attempt", extra={"event": "port_scan", "ip": ip, "port": port, "session_id": session_id})
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.settimeout(0.5)
            start = time.perf_counter()
            try:
                conn.connect((ip, port))
            except Exception:
                pass
            finally:
                conn.close()
            await asyncio.sleep(0.05 + random.random() * 0.1)
            if time.perf_counter() - start > 0.5:
                break


SIMULATED_ATTACKS = [beacon_to_c2, download_malware, port_scan]

# ---------------------------------------------------------------------------
# Human-like browsing routines
# ---------------------------------------------------------------------------

async def human_like_scroll(page: Page) -> None:
    height = await page.evaluate("() => document.body.scrollHeight")
    scroll_steps = random.randint(3, 7)
    for _ in range(scroll_steps):
        new_y = random.randint(0, height)
        await page.mouse.wheel(0, new_y)
        await asyncio.sleep(jitter(1.2))


async def random_click(page: Page) -> None:
    links = await page.query_selector_all("a")
    if not links:
        return
    link = random.choice(links)
    try:
        await link.click(timeout=3000)
        await asyncio.sleep(jitter(2))
    except Exception:
        pass


async def browse_site(context: BrowserContext, url: str, session_id: str) -> None:
    t0 = time.time()
    LOGGER.info("navigate", extra={"event": "navigate", "url": url, "session_id": session_id})
    try:
        page = await context.new_page()
        await page.goto(url, timeout=30000, wait_until="domcontentloaded")
        await asyncio.sleep(jitter(2, 0.5))
        await human_like_scroll(page)
        if random.random() < 0.5:
            await random_click(page)
        dwell = jitter(3, 0.8)
        await asyncio.sleep(dwell)
    except Exception as exc:
        LOGGER.warning("browse_error", extra={"event": "error", "url": url, "session_id": session_id, "error": str(exc)})
    finally:
        await page.close()
        elapsed = time.time() - t0
        LOGGER.info("navigate_complete", extra={"event": "navigate_complete", "url": url, "session_id": session_id, "elapsed": round(elapsed, 2)})


# ---------------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Human-Like Web Browsing & Compromised Host Simulator")
    p.add_argument("--sites", default="sites.txt", help="Path to benign site list")
    p.add_argument("--mal-sites", default="malicious_sites.txt", help="Path to malicious site list")
    p.add_argument("--compromise", action="store_true", help="Enable compromised-host behaviour")
    p.add_argument("--headful", action="store_true", help="Run browser with UI (default is headless)")
    p.add_argument("--duration", default="30m", type=str, help="Total run time e.g. 45s, 30m, 2h")
    p.add_argument("--log-file", default=None, help="File path to append JSON logs")
    p.add_argument("--verbose", action="store_true", help="Increase log verbosity")
    return p.parse_args()


async def run_browser_session(args: argparse.Namespace) -> None:
    session_id = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))

    if args.log_file:
        Path(args.log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(args.log_file)
        file_handler.setFormatter(jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s"))
        LOGGER.addHandler(file_handler)

    end_time = datetime.utcnow() + parse_duration(args.duration)

    benign_sites = load_sites(Path(args.sites))
    malicious_sites = load_sites(Path(args.mal_sites)) if args.compromise else []
    site_cycle = benign_sites.copy()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not args.headful, args=["--no-sandbox", "--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(user_agent=random_user_agent())

        prog_bar = tqdm(total=int((end_time - datetime.utcnow()).total_seconds()), desc="Session time remaining", unit="s")
        try:
            while datetime.utcnow() < end_time:
                if not site_cycle:
                    site_cycle = benign_sites.copy()
                    random.shuffle(site_cycle)
                url = site_cycle.pop()
                await browse_site(context, url, session_id)
                # Potentially perform malicious action
                if args.compromise and random.random() < 0.2 and malicious_sites:
                    attack_fn = random.choice(SIMULATED_ATTACKS)
                    if attack_fn is port_scan:
                        await attack_fn("192.168.1", session_id)  # Example subnet
                    else:
                        await attack_fn(random.choice(malicious_sites), session_id)
                await asyncio.sleep(jitter(2.5))
                remaining = (end_time - datetime.utcnow()).total_seconds()
                prog_bar.n = int((parse_duration(args.duration).total_seconds()) - remaining)
                prog_bar.refresh()
        finally:
            await context.close()
            await browser.close()
            prog_bar.close()
            LOGGER.info("session_complete", extra={"event": "session_complete", "session_id": session_id})


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parsed_args = parse_args()
    if parsed_args.verbose:
        LOGGER.setLevel(logging.DEBUG)
    try:
        asyncio.run(run_browser_session(parsed_args))
    except KeyboardInterrupt:
        LOGGER.info("terminated_by_user", extra={"event": "terminated", "reason": "keyboard_interrupt"})