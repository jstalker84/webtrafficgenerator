# Website Traffic Generator

A powerful and configurable web traffic simulator designed for testing FortiGate/FortiAnalyzer and other network monitoring systems. This tool generates realistic web browsing patterns by making HTTP requests to various websites with configurable parameters.

## Overview

This tool simulates real-world web traffic by:
- Making HTTP requests to a diverse set of popular websites
- Using realistic browsing patterns with variable delays
- Supporting concurrent requests through multi-threading
- Providing detailed logging of all traffic generation activities
- Offering customizable configuration options

Perfect for:
- Testing network monitoring systems
- Evaluating firewall configurations
- Simulating user browsing behavior
- Generating controlled network traffic for analysis
- Benchmarking network performance

## Features

- **Realistic Traffic Simulation**: Mimics human browsing patterns with variable delays between requests
- **Extensive Website Coverage**: Includes 90+ popular websites across various categories (search engines, social media, news, e-commerce, etc.)
- **Concurrent Request Handling**: Multi-threaded architecture for efficient traffic generation
- **Configurable Parameters**: Customize request delays, timeouts, concurrency, and more
- **Custom User-Agent Support**: Rotate through different user agents for realistic browser fingerprinting
- **Detailed Logging**: Comprehensive logging of all requests and responses
- **Retry Mechanism**: Built-in retry strategy for handling transient network errors
- **Command-Line Interface**: Easy-to-use CLI with various options
- **Connectivity Testing**: Verify network connectivity before starting traffic generation

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/website-traffic-generator.git
   cd website-traffic-generator
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If no requirements.txt is present, install the necessary packages:
   ```bash
   pip install requests
   ```

## Usage

### Basic Usage

Run the script with default settings (60 minutes duration, 10 requests per minute):

```bash
python websitetraffic.py
```

### Command-Line Options

```bash
python websitetraffic.py [options]
```

Available options:

| Option | Description |
|--------|-------------|
| `--duration MINUTES` | Duration in minutes (default: 60) |
| `--rpm REQUESTS` | Requests per minute (default: 10) |
| `--config FILE` | Path to configuration file |
| `--test` | Test connectivity only |
| `--create-config` | Create a sample configuration file |

### Examples

1. Generate traffic for 30 minutes with 20 requests per minute:
   ```bash
   python websitetraffic.py --duration 30 --rpm 20
   ```

2. Use a custom configuration file:
   ```bash
   python websitetraffic.py --config my_config.json
   ```

3. Test connectivity to sample websites:
   ```bash
   python websitetraffic.py --test
   ```

4. Create a sample configuration file:
   ```bash
   python websitetraffic.py --create-config
   ```

## Configuration

The tool can be configured using a JSON configuration file. Create a sample configuration with:

```bash
python websitetraffic.py --create-config
```

This will generate a `traffic_config.json` file with the following structure:

```json
{
