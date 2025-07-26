# Enhanced Web Traffic Simulator

A powerful and configurable web traffic simulator designed for testing security logging systems, SIEM platforms, and network monitoring solutions. This tool generates realistic web browsing patterns while simulating various security scenarios including compromised host behaviors, malicious traffic patterns, and attack attempts.

## Overview

This advanced tool simulates real-world web traffic and security events by:
- Making HTTP requests to a diverse set of popular websites with realistic browsing patterns
- Simulating compromised host behaviors (credential theft, data exfiltration, C2 communications)
- Generating malicious traffic patterns (SQL injection, XSS, directory traversal, command injection)
- Providing comprehensive multi-layered logging for security analysis
- Supporting concurrent requests through multi-threading
- Offering highly customizable configuration options

Perfect for:
- Testing security logging systems and SIEM platforms
- Evaluating firewall and IDS/IPS configurations
- Simulating realistic attack scenarios for security training
- Generating controlled network traffic for security analysis
- Benchmarking security monitoring and detection capabilities
- Validating security incident response procedures

## Features

### Core Traffic Simulation
- **Realistic Browsing Patterns**: Mimics human browsing behavior with variable delays between requests
- **Extensive Website Coverage**: Includes 90+ popular websites across various categories (search engines, social media, news, e-commerce, etc.)
- **Concurrent Request Handling**: Multi-threaded architecture for efficient traffic generation
- **Configurable Parameters**: Customize request delays, timeouts, concurrency, and more
- **Custom User-Agent Support**: Rotate through different user agents for realistic browser fingerprinting

### Security Simulation Capabilities
- **Compromised Host Simulation**: Simulates various compromise scenarios including credential theft, data exfiltration, and C2 communications
- **Malicious Traffic Generation**: Creates attack patterns including SQL injection, XSS, directory traversal, and command injection attempts
- **Credential Theft Simulation**: Models credential harvesting attempts and password spraying
- **Data Exfiltration Simulation**: Simulates data theft scenarios and sensitive information access
- **Lateral Movement Simulation**: Mimics internal network reconnaissance and privilege escalation
- **C2 Communication Simulation**: Simulates command and control traffic patterns

### Advanced Logging & Analytics
- **Multi-layered Logging System**: Separate specialized loggers for traffic, security events, compromised activities, DNS queries, and statistics
- **Session Tracking**: Unique session IDs for correlation across log files
- **Real-time Statistics**: Request success rates, security event counts, and performance metrics
- **Forensic-ready Logs**: Structured logging suitable for SIEM integration and forensic analysis
- **Comprehensive Event Correlation**: Detailed logging with timestamps, user agents, and session information

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Internet connectivity for external requests

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/enhanced-web-traffic-simulator.git
   cd enhanced-web-traffic-simulator
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Run the script with default settings (60 minutes duration, 15 requests per minute):

```bash
python enhanced_web_traffic_simulator.py
```

### Advanced Usage Examples

1. Generate traffic for 2 hours with 25 requests per minute:
   ```bash
   python enhanced_web_traffic_simulator.py --duration 120 --rpm 25
   ```

2. Use a custom configuration file:
   ```bash
   python enhanced_web_traffic_simulator.py --config my_config.json
   ```

3. Disable security simulations for pure traffic generation:
   ```bash
   python enhanced_web_traffic_simulator.py --no-compromise --no-malicious
   ```

4. Test connectivity to sample websites:
   ```bash
   python enhanced_web_traffic_simulator.py --test
   ```

5. Create a sample configuration file:
   ```bash
   python enhanced_web_traffic_simulator.py --create-config
   ```

6. Custom log directory:
   ```bash
   python enhanced_web_traffic_simulator.py --log-dir /var/log/traffic_sim
   ```

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--duration MINUTES` | Simulation duration in minutes | 60 |
| `--rpm REQUESTS` | Requests per minute | 15 |
| `--config FILE` | Configuration file path | None |
| `--test` | Test connectivity only | False |
| `--create-config` | Create configuration template | False |
| `--no-compromise` | Disable compromised host simulation | False |
| `--no-malicious` | Disable malicious traffic simulation | False |
| `--log-dir DIR` | Log directory path | security_logs |

## Configuration

The tool can be configured using a JSON configuration file. Create a sample configuration with:

```bash
python enhanced_web_traffic_simulator.py --create-config
```

This will generate a `traffic_config.json` file with configurable parameters for:
- Request timing and delays
- Concurrency settings
- Security simulation probabilities
- Logging preferences
- Website selection and filtering

## Logging Output

The simulator generates comprehensive logs in the `security_logs/` directory:

- **traffic.log**: All HTTP requests and responses
- **security_events.log**: Security-related events and potential threats
- **compromised_activity.log**: Compromised host simulation activities
- **dns_activity.log**: DNS lookup activities
- **statistics.log**: Performance and usage statistics

## Security Considerations

⚠️ **Important**: This tool is designed for legitimate security testing and training purposes only. Always ensure you have proper authorization before running security simulations in any environment.

- Use only in controlled, authorized testing environments
- Do not run against production systems without explicit permission
- The tool generates realistic attack patterns that may trigger security alerts
- Ensure compliance with your organization's security policies

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
