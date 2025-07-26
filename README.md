# Website Traffic Simulator

A powerful and configurable web traffic simulator designed for testing **security logging**, SIEM solutions, firewalls, and other network-monitoring systems. The tool reproduces realistic human-like browsing patterns by issuing HTTP(S) requests to a wide range of popular websites with fully customisable parameters.

---

## ✨ Key Capabilities

* **Realistic traffic generation** – variable delays, randomised user-agents, and concurrent sessions mimic genuine user behaviour.
* **Extensive site list** – 90+ top websites across search, social, news, e-commerce, tech, and more.
* **Threaded architecture** – parallel requests for high-throughput testing.
* **Flexible CLI** – quickly adjust duration, requests-per-minute, or use a JSON config file.
* **Connectivity testing** – verify outbound reachability before launching a full run.
* **Rich logging** – detailed timestamped logs for easy ingestion by SIEM / log analytics platforms.

---

## 🚀 Quick Start

### 1. Install Python requirements

```bash
python -m pip install -r requirements.txt
```

### 2. Generate traffic with defaults (60 min / 10 RPM)

```bash
python websitetraffic.py
```

Logs are written to `traffic_generator.log` and to the console.

---

## ⚙️ Command-line Reference

```text
python websitetraffic.py [options]
```

| Option                | Type | Default | Description                                    |
|-----------------------|------|---------|------------------------------------------------|
| `--duration MIN`      | int  | 60      | How long to run (minutes)                      |
| `--rpm REQUESTS`      | int  | 10      | Requests per minute                            |
| `--config FILE`       | str  | ―       | Path to a JSON configuration file              |
| `--test`              | flag | False   | Only test connectivity to a sample of sites    |
| `--create-config`     | flag | False   | Write a template `traffic_config.json` file    |

---

## 🧑‍💻 Usage Examples

1. 30-minute run at 20 requests per minute:

```bash
python websitetraffic.py --duration 30 --rpm 20
```

2. Use a custom configuration:

```bash
python websinetraffic.py --config my_config.json
```

3. Connectivity test only:

```bash
python websitetraffic.py --test
```

4. Generate a starter configuration file:

```bash
python websitetraffic.py --create-config
```

---

## 📄 Configuration File

The optional JSON config allows fine-grained control without long CLI arguments. Create it yourself or with `--create-config`.

```json
{
  "request_delay_min": 1,
  "request_delay_max": 5,
  "timeout": 10,
  "max_workers": 5,
  "user_agents": [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  ]
}
```

| Key                 | Description                                           | Default |
|---------------------|-------------------------------------------------------|---------|
| `request_delay_min` | Minimum delay between two requests (seconds)          | 1       |
| `request_delay_max` | Maximum delay between two requests (seconds)          | 5       |
| `timeout`           | HTTP request timeout (seconds)                        | 10      |
| `max_workers`       | Number of parallel worker threads                     | 5       |
| `user_agents`       | List of user-agent strings to rotate                  | preset  |

---

## 📝 Logs

All activity is recorded in `traffic_generator.log` (rotated each run) plus standard output. Logs include timestamps, HTTP status codes, and error details for straightforward ingestion by log analysis pipelines.

---

## 💡 Tips

* Run from a host that can reach the Internet without captive portals or proxies.
* Adjust `--rpm` and `--max_workers` (via config) to stress-test logging pipelines at higher throughput.
* Combine with packet-capture tools (e.g., tcpdump, Wireshark) for deeper analysis.

---

## 🙌 Contributing

Pull requests welcome! Please open an issue first to discuss major changes.

## 📜 License

This project is released under the MIT License.
