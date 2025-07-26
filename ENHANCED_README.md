# Enhanced Web Traffic Simulator with Security Simulation

A comprehensive, advanced web traffic simulator designed for security testing, network monitoring, and cybersecurity training. This tool generates realistic human-like browsing patterns while simulating compromised host behaviors and security threat scenarios.

## 🔥 Key Features

### Core Capabilities
- **Human-like Browsing Simulation**: Realistic browsing patterns with variable delays, form submissions, and page interactions
- **Compromised Host Simulation**: Simulates various compromise scenarios including credential theft, data exfiltration, and C2 communications
- **Security Threat Simulation**: Generates malicious traffic patterns including SQL injection, XSS, directory traversal, and command injection attempts
- **Extensive Website Database**: 200+ popular websites across all categories for realistic traffic generation
- **Advanced Logging System**: Comprehensive logging with specialized loggers for traffic, security events, DNS queries, and statistics

### Security Simulation Features
- **Credential Theft Simulation**: Simulates credential harvesting attempts
- **Data Exfiltration Simulation**: Models data theft scenarios
- **Lateral Movement Simulation**: Mimics internal network reconnaissance
- **C2 Communication Simulation**: Simulates command and control traffic
- **Attack Pattern Generation**: SQL injection, XSS, directory traversal, command injection
- **Compromised User Agent Rotation**: Uses outdated browsers for compromised host simulation

### Logging & Analytics
- **Multi-layered Logging**: Separate logs for traffic, security events, compromised activities, DNS queries, and statistics
- **Session Tracking**: Unique session IDs for correlation across log files
- **Real-time Statistics**: Request success rates, security event counts, and performance metrics
- **Forensic-ready Logs**: Structured logging suitable for SIEM integration and forensic analysis

## 📋 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Internet connectivity for external requests

### Setup
1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Basic Usage
Run with default settings (60 minutes, 15 requests per minute):
```bash
python enhanced_web_traffic_simulator.py
```

### Advanced Usage

#### Generate Traffic with Custom Parameters
```bash
# Run for 2 hours with 25 requests per minute
python enhanced_web_traffic_simulator.py --duration 120 --rpm 25

# Use custom configuration file
python enhanced_web_traffic_simulator.py --config my_config.json

# Disable security simulations for pure traffic generation
python enhanced_web_traffic_simulator.py --no-compromise --no-malicious

# Custom log directory
python enhanced_web_traffic_simulator.py --log-dir /var/log/traffic_sim
```

#### Configuration Management
```bash
# Create advanced configuration template
python enhanced_web_traffic_simulator.py --create-config

# Test connectivity before running simulation
python enhanced_web_traffic_simulator.py --test
```

### Command Line Options

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

## ⚙️ Configuration

### Configuration File Structure
```json
{
    "request_delay_min": 0.5,
    "request_delay_max": 8.0,
    "timeout": 15,
    "max_workers": 8,
    "compromise_probability": 0.15,
    "malicious_traffic_probability": 0.05,
    "simulate_compromised_host": true,
    "security_simulation_enabled": true,
    "advanced_logging": true,
    "log_directory": "security_logs",
    "user_agents": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36..."
    ]
}
```

### Configuration Parameters

| Parameter | Description | Type | Default |
|-----------|-------------|------|---------|
| `request_delay_min` | Minimum delay between requests (seconds) | float | 0.5 |
| `request_delay_max` | Maximum delay between requests (seconds) | float | 8.0 |
| `timeout` | Request timeout (seconds) | int | 15 |
| `max_workers` | Maximum concurrent threads | int | 8 |
| `compromise_probability` | Probability of compromise behavior per session | float | 0.15 |
| `malicious_traffic_probability` | Probability of malicious traffic generation | float | 0.05 |
| `simulate_compromised_host` | Enable compromised host simulation | bool | true |
| `security_simulation_enabled` | Enable security threat simulation | bool | true |
| `advanced_logging` | Enable detailed logging | bool | true |

## 📊 Traffic Composition

The simulator generates three types of traffic:

1. **Normal Traffic (80%)**: Legitimate browsing patterns
   - Search engines, social media, news sites
   - E-commerce, entertainment, productivity tools
   - Realistic user interactions and page navigation

2. **Compromised Host Traffic (15%)**: Suspicious but not overtly malicious
   - Outdated user agents
   - Unusual browsing patterns
   - Credential theft attempts
   - Data exfiltration simulations

3. **Malicious Traffic (5%)**: Clearly malicious activity
   - Attack payload generation
   - Malicious domain requests
   - Security tool testing traffic

## 📁 Website Database

The simulator includes 200+ websites across categories:

### Core Categories
- **Search Engines**: Google, Bing, DuckDuckGo, Yahoo, Yandex
- **Social Media**: Facebook, Twitter, Instagram, LinkedIn, Reddit, TikTok
- **Video Platforms**: YouTube, Netflix, Twitch, Vimeo, Hulu
- **News & Media**: CNN, BBC, Reuters, NYTimes, Guardian
- **E-commerce**: Amazon, eBay, Walmart, Target, Best Buy
- **Technology**: Microsoft, Apple, GitHub, Stack Overflow
- **Cloud Services**: AWS, Google Cloud, Azure, Dropbox
- **Entertainment**: Spotify, IMDB, Steam, Gaming sites
- **Financial**: PayPal, Stripe, Banking sites, Crypto exchanges
- **Travel**: Booking, Expedia, Airbnb, TripAdvisor

### Specialized Categories
- **Adult Content**: For realistic traffic simulation
- **File Sharing**: MediaFire, Mega, WeTransfer, Torrents
- **Anonymous Services**: Tor Project, Privacy tools, ProtonMail
- **Cryptocurrency**: Bitcoin, Ethereum, Blockchain explorers
- **Regional Sites**: Chinese, Russian, Korean platforms

## 🔍 Logging System

### Log Files Generated

1. **traffic.log**: All HTTP requests and responses
   ```
   2024-01-15 10:30:45 - traffic - INFO - SESSION:a1b2c3d4 TYPE:normal GET https://www.google.com STATUS:200 TIME:1.23s UA:Mozilla/5.0...
   ```

2. **security_events.log**: Security-related events and threats
   ```
   2024-01-15 10:31:22 - security - WARNING - SESSION:a1b2c3d4 TYPE:sql_injection SEVERITY:high DESC:Simulated SQL injection attack INDICATORS:{"target":"search","payload":"' OR 1=1--"}
   ```

3. **compromised_activity.log**: Compromised host behaviors
   ```
   2024-01-15 10:32:15 - compromise - INFO - SESSION:a1b2c3d4 ACTIVITY:credential_theft TARGET:https://example.com STATUS:ATTEMPT PAYLOAD_HASH:d41d8cd98f00b204
   ```

4. **dns_activity.log**: DNS lookup activities
   ```
   2024-01-15 10:33:01 - dns - INFO - SESSION:a1b2c3d4 DOMAIN:google.com TYPE:A TIME:0.045s
   ```

5. **statistics.log**: Session statistics and metrics
   ```
   2024-01-15 11:30:45 - stats - INFO - SESSION:a1b2c3d4 STATS:{"total_requests":150,"successful_requests":147,"failed_requests":3}
   ```

### Log Analysis
The structured logging format enables:
- SIEM integration (Splunk, ELK Stack, etc.)
- Forensic analysis and correlation
- Security event detection
- Performance monitoring
- Threat hunting scenarios

## 🛡️ Security Simulations

### Compromised Host Behaviors

1. **Credential Theft**
   - Targets login pages and authentication endpoints
   - Simulates credential harvesting attempts
   - Logs attempted credential theft activities

2. **Data Exfiltration**
   - Simulates data theft to external servers
   - Models file upload and transfer activities
   - Tracks potential data loss scenarios

3. **Lateral Movement**
   - Simulates internal network reconnaissance
   - Models privilege escalation attempts
   - Generates scanning and enumeration traffic

4. **Persistence Mechanisms**
   - Simulates installation of persistent access
   - Models configuration changes
   - Tracks system modification attempts

5. **C2 Communication**
   - Simulates command and control traffic
   - Models beacon and heartbeat communications
   - Generates encrypted C2 payload traffic

### Attack Pattern Simulation

1. **SQL Injection**
   - Classic injection payloads
   - Union-based attacks
   - Boolean-based blind attacks

2. **Cross-Site Scripting (XSS)**
   - Reflected XSS payloads
   - Stored XSS attempts
   - DOM-based XSS vectors

3. **Directory Traversal**
   - Path traversal attempts
   - File inclusion attacks
   - Directory enumeration

4. **Command Injection**
   - OS command injection
   - Shell command execution
   - System compromise attempts

## 🎯 Use Cases

### Security Testing
- **SIEM Testing**: Generate diverse log data for SIEM rule testing
- **Network Monitoring**: Test network security monitoring tools
- **Firewall Testing**: Validate firewall rules and policies
- **IDS/IPS Testing**: Test intrusion detection and prevention systems

### Training & Education
- **Security Analyst Training**: Provide realistic traffic for analysis practice
- **Incident Response Training**: Generate compromise scenarios for response training
- **Forensic Training**: Create realistic datasets for forensic analysis practice
- **Red Team Exercises**: Simulate realistic user and attacker behaviors

### Research & Development
- **Traffic Analysis**: Study normal vs. malicious traffic patterns
- **Machine Learning**: Generate labeled datasets for ML model training
- **Baseline Establishment**: Create network traffic baselines
- **Performance Testing**: Test network infrastructure under load

## ⚠️ Important Notes

### Legal and Ethical Use
- **Authorized Testing Only**: Only use on networks you own or have explicit permission to test
- **No Real Attacks**: The tool simulates attacks but doesn't perform actual exploitation
- **Compliance**: Ensure compliance with local laws and organizational policies
- **Responsible Disclosure**: Report any actual vulnerabilities found through proper channels

### Security Considerations
- **Isolated Environment**: Run in isolated test environments when possible
- **Network Impact**: Monitor network bandwidth and performance impact
- **Log Storage**: Ensure adequate storage for comprehensive logging
- **Data Protection**: Protect generated logs containing simulated attack data

### Performance Considerations
- **Resource Usage**: Monitor CPU and memory usage during execution
- **Network Bandwidth**: Consider bandwidth impact on production networks
- **Concurrent Connections**: Adjust max_workers based on system capabilities
- **Log File Size**: Implement log rotation for long-running simulations

## 🔧 Troubleshooting

### Common Issues

1. **Connection Timeouts**
   - Increase timeout value in configuration
   - Check network connectivity
   - Verify DNS resolution

2. **High Resource Usage**
   - Reduce max_workers setting
   - Increase delays between requests
   - Monitor system resources

3. **Log File Issues**
   - Ensure log directory permissions
   - Check available disk space
   - Verify log rotation settings

### Performance Optimization

1. **Reduce Request Rate**
   ```bash
   python enhanced_web_traffic_simulator.py --rpm 5
   ```

2. **Disable Heavy Simulations**
   ```bash
   python enhanced_web_traffic_simulator.py --no-compromise --no-malicious
   ```

3. **Optimize Threading**
   - Adjust max_workers in configuration
   - Monitor thread pool performance

## 📈 Monitoring and Metrics

### Real-time Monitoring
The simulator provides real-time statistics including:
- Total requests sent
- Success/failure rates
- Security events generated
- Compromise activities simulated
- Requests per minute achieved

### Long-term Analysis
Log files enable long-term analysis of:
- Traffic patterns over time
- Attack simulation effectiveness
- System performance under load
- Security event correlation

## 🤝 Contributing

We welcome contributions to enhance the simulator's capabilities:

1. **Website Database**: Add new websites to increase traffic diversity
2. **Attack Patterns**: Implement new attack simulation scenarios
3. **User Agents**: Update user agent strings for current browsers
4. **Logging Enhancements**: Improve logging formats and analysis capabilities
5. **Performance Optimizations**: Enhance efficiency and resource usage

## 📄 License

This tool is provided for educational and authorized testing purposes only. Users are responsible for ensuring compliance with applicable laws and regulations.

## 🔗 Related Tools

- **Original Traffic Generator**: Basic web traffic generation
- **SIEM Integration Tools**: Log parsing and analysis utilities
- **Network Monitoring Solutions**: Complement this tool with network monitoring
- **Security Testing Frameworks**: Integrate with broader security testing suites

---

**Disclaimer**: This tool is designed for legitimate security testing and educational purposes only. Users are responsible for ensuring proper authorization before use and compliance with all applicable laws and regulations.