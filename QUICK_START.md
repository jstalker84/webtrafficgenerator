# Quick Start Guide - Enhanced Web Traffic Simulator

## 🚀 Get Started in 5 Minutes

### Step 1: Setup
```bash
# Make the runner script executable (if not already)
chmod +x run_traffic_simulator.sh

# Run setup to install dependencies and create configuration
./run_traffic_simulator.sh setup
```

### Step 2: Test Connectivity
```bash
# Test connectivity to ensure everything is working
./run_traffic_simulator.sh test
```

### Step 3: Run Your First Simulation
```bash
# Quick 15-minute simulation for testing
./run_traffic_simulator.sh quick
```

## 📊 Common Usage Scenarios

### For Security Testing
```bash
# High-intensity security simulation with lots of malicious activity
./run_traffic_simulator.sh security
```

### For Network Load Testing
```bash
# Clean traffic without security threats
./run_traffic_simulator.sh clean
```

### For Extended Testing
```bash
# 4-hour simulation for long-term testing
./run_traffic_simulator.sh extended
```

### Custom Scenarios
```bash
# Custom 30-minute simulation with 20 requests per minute
./run_traffic_simulator.sh custom --duration 30 --rpm 20

# High-volume simulation without security features
./run_traffic_simulator.sh custom --duration 60 --rpm 50 --no-compromise --no-malicious
```

## 📋 Quick Commands Reference

| Command | Description | Duration | Requests/Min |
|---------|-------------|----------|--------------|
| `quick` | Quick test simulation | 15 min | 10 |
| `normal` | Standard simulation | 60 min | 15 |
| `extended` | Long-term simulation | 240 min | 20 |
| `security` | High-threat simulation | 90 min | 25 |
| `clean` | No security threats | 60 min | 15 |

## 🔍 Monitoring Your Simulation

### View Logs in Real-time
```bash
# View all log files
./run_traffic_simulator.sh logs

# Monitor traffic in real-time
tail -f security_logs/traffic.log

# Monitor security events
tail -f security_logs/security_events.log

# Monitor compromise activities
tail -f security_logs/compromised_activity.log
```

### Basic Analysis
```bash
# Get summary statistics
./run_traffic_simulator.sh analyze
```

## ⚙️ Traffic Types Generated

### Normal Traffic (80%)
- Search engines (Google, Bing, DuckDuckGo)
- Social media (Facebook, Twitter, Instagram)
- News sites (CNN, BBC, Reuters)
- E-commerce (Amazon, eBay, Walmart)
- Entertainment (YouTube, Netflix, Spotify)

### Compromised Host Traffic (15%)
- Credential theft attempts
- Data exfiltration simulation
- Lateral movement patterns
- Suspicious browsing with outdated browsers

### Malicious Traffic (5%)
- SQL injection attempts
- XSS attack simulations
- Directory traversal attempts
- Command injection tests

## 🛡️ Security Simulation Features

### What Gets Simulated
- **Credential Harvesting**: Login page attacks
- **Data Theft**: File exfiltration attempts  
- **Network Reconnaissance**: Internal scanning
- **C2 Communications**: Command & control traffic
- **Attack Payloads**: SQL injection, XSS, etc.

### What Gets Logged
- All HTTP requests with response codes
- Security events with severity levels
- Compromise activities with payload hashes
- DNS queries with response times
- Session statistics and metrics

## 📁 Log Files Created

```
security_logs/
├── traffic.log              # All HTTP requests
├── security_events.log      # Security threats detected
├── compromised_activity.log # Compromise simulations
├── dns_activity.log         # DNS lookup activities
└── statistics.log           # Session statistics
```

## 🔧 Troubleshooting

### Common Issues

**Connection Errors**
```bash
# Test connectivity first
./run_traffic_simulator.sh test

# If issues persist, try with lower request rate
./run_traffic_simulator.sh custom --duration 15 --rpm 5
```

**High CPU Usage**
```bash
# Reduce concurrent workers and request rate
./run_traffic_simulator.sh custom --duration 30 --rpm 8
```

**Permission Errors**
```bash
# Ensure script is executable
chmod +x run_traffic_simulator.sh

# Check log directory permissions
mkdir -p security_logs
chmod 755 security_logs
```

## 💡 Tips for Best Results

### For Security Testing
1. Run `security` mode for maximum threat diversity
2. Monitor `security_events.log` for attack patterns
3. Use extended duration for comprehensive testing
4. Correlate logs using session IDs

### For Performance Testing
1. Use `clean` mode to avoid security overhead
2. Increase `--rpm` for higher load
3. Monitor system resources during testing
4. Use multiple concurrent sessions if needed

### For Training
1. Start with `quick` to understand log formats
2. Progress to `security` for threat analysis practice
3. Use `analyze` command for basic statistics
4. Import logs into SIEM for advanced analysis

## 🚨 Important Notes

### Legal Compliance
- Only use on networks you own or have permission to test
- Ensure compliance with organizational policies
- Do not use for actual attacks or unauthorized testing

### Best Practices
- Start with short duration tests
- Monitor system resources
- Keep logs for analysis but protect sensitive data
- Use isolated test environments when possible

## 📞 Need Help?

**View full documentation:**
```bash
./run_traffic_simulator.sh help
```

**Check logs for errors:**
```bash
./run_traffic_simulator.sh logs
```

**Get basic statistics:**
```bash
./run_traffic_simulator.sh analyze
```

---

**Ready to start? Run your first simulation:**
```bash
./run_traffic_simulator.sh quick
```