# Human-Like Web Browsing & Compromised-Host Simulator

This project provides a Python script that automatically browses a configurable set of web sites using human-like interaction patterns and optionally generates suspicious activity to mimic a compromised endpoint.  All actions are logged in JSON format for easy ingestion by SIEM pipelines.

---

## Features

* Headless (or visible) Chromium driven by Playwright.
* Randomised user-agents, mouse moves, scrolling & dwell times.
* Extensible site list (`sites.txt`) and malicious site list (`malicious_sites.txt`).
* Simulated malicious behaviours (C2 beacon, suspicious downloads, port scan).
* Structured logging (JSON) plus coloured console output.
* Simple CLI flags to control run-time behaviour.

---

## Quick Start

1. **Install Python 3.8+** and [Google Chrome](https://www.google.com/chrome/) or Chromium.

2. **Install dependencies** (creates an isolated venv is recommended):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# One-off Playwright browser download
playwright install chromium
```

3. **Run the simulator** for 30 minutes:

```bash
python browse_sim.py --duration 30m --log-file logs/session.log
```

### Useful Flags

```
--headful            Show the browser window (default is headless)
--sites FILE         Alternative site list (default sites.txt)
--mal-sites FILE     Alternative malicious site list (default malicious_sites.txt)
--compromise         Enable compromised host simulation
--duration 1h30m     Session length (supports s/m/h suffix)
```

---

## Extending

* **Add Sites** – Edit `sites.txt` or `malicious_sites.txt`, one URL per line.
* **Add Behaviours** – Implement additional functions in `browse_sim.py` and register them in `SIMULATED_ATTACKS`.

---

## Disclaimer

This project is **strictly for defensive security research** and blue-team lab environments.  Do not aim it at networks or systems you do not own or have explicit permission to test.
