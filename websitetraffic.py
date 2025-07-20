#!/usr/bin/env python3
"""
Web Traffic Generator for FortiGate/FortiAnalyzer Testing

This script simulates realistic web browsing patterns by making HTTP requests
to various websites with configurable parameters.

Author: Network Testing Tool
Version: 1.0
"""

import requests
import random
import time
import json
import logging
from datetime import datetime
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class WebTrafficGenerator:
    def __init__(self, config_file=None):
        """Initialize the traffic generator with configuration."""
        self.session = requests.Session()
        self.setup_session()
        self.setup_logging()
        
        # Default configuration
        self.config = {
            "request_delay_min": 1,
            "request_delay_max": 5,
            "timeout": 10,
            "max_workers": 5,
            "user_agents": [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"
            ]
        }
        
        # Load configuration if provided
        if config_file:
            self.load_config(config_file)
        
        # Comprehensive list of websites for traffic generation
        self.websites = [
            # Search Engines
            "https://www.google.com",
            "https://www.bing.com",
            "https://duckduckgo.com",
            "https://www.yahoo.com",
            
            # Social Media
            "https://www.facebook.com",
            "https://www.twitter.com",
            "https://www.instagram.com",
            "https://www.linkedin.com",
            "https://www.reddit.com",
            "https://www.pinterest.com",
            "https://www.snapchat.com",
            "https://www.tiktok.com",
            
            # Video Platforms
            "https://www.youtube.com",
            "https://www.netflix.com",
            "https://www.twitch.tv",
            "https://vimeo.com",
            "https://www.dailymotion.com",
            
            # News & Media
            "https://www.cnn.com",
            "https://www.bbc.com",
            "https://www.reuters.com",
            "https://www.nytimes.com",
            "https://www.washingtonpost.com",
            "https://www.theguardian.com",
            "https://www.foxnews.com",
            "https://www.npr.org",
            "https://www.bloomberg.com",
            
            # E-commerce
            "https://www.amazon.com",
            "https://www.ebay.com",
            "https://www.walmart.com",
            "https://www.target.com",
            "https://www.bestbuy.com",
            "https://www.etsy.com",
            "https://www.shopify.com",
            "https://www.alibaba.com",
            
            # Technology
            "https://www.microsoft.com",
            "https://www.apple.com",
            "https://www.github.com",
            "https://stackoverflow.com",
            "https://www.techcrunch.com",
            "https://www.wired.com",
            "https://www.theverge.com",
            "https://www.arstechnica.com",
            
            # Cloud Services
            "https://aws.amazon.com",
            "https://cloud.google.com",
            "https://azure.microsoft.com",
            "https://www.dropbox.com",
            "https://drive.google.com",
            
            # Entertainment
            "https://www.spotify.com",
            "https://www.imdb.com",
            "https://www.rottentomatoes.com",
            "https://www.gamespot.com",
            "https://www.ign.com",
            "https://www.steam.com",
            
            # Educational
            "https://www.wikipedia.org",
            "https://www.coursera.org",
            "https://www.edx.org",
            "https://www.khanacademy.org",
            "https://www.udemy.com",
            
            # Business & Finance
            "https://www.paypal.com",
            "https://www.stripe.com",
            "https://www.salesforce.com",
            "https://www.oracle.com",
            "https://www.sap.com",
            "https://www.adobe.com",
            
            # Travel
            "https://www.booking.com",
            "https://www.expedia.com",
            "https://www.airbnb.com",
            "https://www.tripadvisor.com",
            
            # Productivity
            "https://www.office.com",
            "https://docs.google.com",
            "https://www.notion.so",
            "https://slack.com",
            "https://zoom.us",
            
            # Forums & Communities
            "https://www.quora.com",
            "https://medium.com",
            "https://www.discourse.org",
            
            # Government & Organizations
            "https://www.whitehouse.gov",
            "https://www.un.org",
            "https://www.who.int",
            
            # Weather & Maps
            "https://weather.com",
            "https://maps.google.com",
            "https://www.openstreetmap.org",
            
            # File Sharing & Storage
            "https://www.box.com",
            "https://onedrive.live.com",
            "https://www.icloud.com"
        ]
    
    def setup_session(self):
        """Configure the requests session with retry strategy."""
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('traffic_generator.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def load_config(self, config_file):
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
            self.logger.info(f"Configuration loaded from {config_file}")
        except Exception as e:
            self.logger.error(f"Error loading configuration: {e}")
    
    def get_random_user_agent(self):
        """Return a random user agent string."""
        return random.choice(self.config["user_agents"])
    
    def make_request(self, url, method="GET", **kwargs):
        """Make an HTTP request with error handling."""
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                timeout=self.config["timeout"],
                allow_redirects=True,
                **kwargs
            )
            
            self.logger.info(f"[{response.status_code}] {method} {url}")
            return response
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error requesting {url}: {e}")
            return None
    
    def simulate_browsing_session(self, website):
        """Simulate a realistic browsing session on a website."""
        try:
            # Initial page load
            response = self.make_request(website)
            if not response:
                return
            
            # Random delay between requests (simulating reading time)
            delay = random.uniform(
                self.config["request_delay_min"],
                self.config["request_delay_max"]
            )
            time.sleep(delay)
            
            # Simulate additional requests (images, CSS, JS, etc.)
            if random.random() < 0.7:  # 70% chance of additional requests
                additional_paths = ['/favicon.ico', '/robots.txt', '/sitemap.xml']
                for path in random.sample(additional_paths, random.randint(1, len(additional_paths))):
                    full_url = urljoin(website, path)
                    self.make_request(full_url)
                    time.sleep(random.uniform(0.1, 0.5))
            
        except Exception as e:
            self.logger.error(f"Error in browsing session for {website}: {e}")
    
    def generate_traffic(self, duration_minutes=60, requests_per_minute=10):
        """Generate web traffic for specified duration."""
        self.logger.info(f"Starting traffic generation for {duration_minutes} minutes")
        self.logger.info(f"Target: {requests_per_minute} requests per minute")
        
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        request_count = 0
        
        try:
            while time.time() < end_time:
                minute_start = time.time()
                
                # Select random websites for this minute
                selected_websites = random.sample(
                    self.websites, 
                    min(requests_per_minute, len(self.websites))
                )
                
                # Use ThreadPoolExecutor for concurrent requests
                with ThreadPoolExecutor(max_workers=self.config["max_workers"]) as executor:
                    futures = [
                        executor.submit(self.simulate_browsing_session, website)
                        for website in selected_websites
                    ]
                    
                    for future in as_completed(futures):
                        try:
                            future.result()
                            request_count += 1
                        except Exception as e:
                            self.logger.error(f"Thread execution error: {e}")
                
                # Wait for the rest of the minute
                elapsed = time.time() - minute_start
                if elapsed < 60:
                    time.sleep(60 - elapsed)
                
                self.logger.info(f"Completed minute. Total requests: {request_count}")
        
        except KeyboardInterrupt:
            self.logger.info("Traffic generation interrupted by user")
        
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
        
        finally:
            total_time = (time.time() - start_time) / 60
            self.logger.info(f"Traffic generation completed. Total requests: {request_count} in {total_time:.2f} minutes")
    
    def test_connectivity(self):
        """Test connectivity to a sample of websites."""
        self.logger.info("Testing connectivity to sample websites...")
        test_sites = random.sample(self.websites, min(10, len(self.websites)))
        
        successful = 0
        for site in test_sites:
            response = self.make_request(site)
            if response and response.status_code == 200:
                successful += 1
        
        self.logger.info(f"Connectivity test: {successful}/{len(test_sites)} sites accessible")
        return successful > 0

def create_sample_config():
    """Create a sample configuration file."""
    sample_config = {
        "request_delay_min": 1,
        "request_delay_max": 5,
        "timeout": 10,
        "max_workers": 5,
        "user_agents": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        ]
    }
    
    with open('traffic_config.json', 'w') as f:
        json.dump(sample_config, f, indent=4)
    
    print("Sample configuration file 'traffic_config.json' created.")

def main():
    """Main function with command-line interface."""
    parser = argparse.ArgumentParser(description='Web Traffic Generator for FortiGate/FortiAnalyzer Testing')
    parser.add_argument('--duration', type=int, default=60, help='Duration in minutes (default: 60)')
    parser.add_argument('--rpm', type=int, default=10, help='Requests per minute (default: 10)')
    parser.add_argument('--config', type=str, help='Configuration file path')
    parser.add_argument('--test', action='store_true', help='Test connectivity only')
    parser.add_argument('--create-config', action='store_true', help='Create sample configuration file')
    
    args = parser.parse_args()
    
    if args.create_config:
        create_sample_config()
        return
    
    # Initialize traffic generator
    generator = WebTrafficGenerator(config_file=args.config)
    
    if args.test:
        generator.test_connectivity()
        return
    
    # Generate traffic
    generator.generate_traffic(duration_minutes=args.duration, requests_per_minute=args.rpm)

if __name__ == "__main__":
    main()
