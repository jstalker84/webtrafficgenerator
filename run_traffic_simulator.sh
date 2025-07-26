#!/bin/bash

# Enhanced Web Traffic Simulator Runner Script
# This script provides easy-to-use commands for running the traffic simulator

SCRIPT_NAME="enhanced_web_traffic_simulator.py"
LOG_DIR="security_logs"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_colored() {
    echo -e "${1}${2}${NC}"
}

# Function to check if Python script exists
check_script() {
    if [ ! -f "$SCRIPT_NAME" ]; then
        print_colored $RED "Error: $SCRIPT_NAME not found in current directory"
        exit 1
    fi
}

# Function to check dependencies
check_dependencies() {
    print_colored $BLUE "Checking dependencies..."
    
    if ! command -v python3 &> /dev/null; then
        print_colored $RED "Error: Python 3 is not installed"
        exit 1
    fi
    
    if [ -f "requirements.txt" ]; then
        print_colored $YELLOW "Installing/updating dependencies..."
        pip3 install -r requirements.txt
    fi
    
    print_colored $GREEN "Dependencies check completed"
}

# Function to show usage
show_usage() {
    echo "Enhanced Web Traffic Simulator Runner"
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo "Commands:"
    echo "  setup         - Install dependencies and create config"
    echo "  test          - Test connectivity"
    echo "  quick         - Quick 15-minute simulation"
    echo "  normal        - Standard 1-hour simulation"
    echo "  extended      - Extended 4-hour simulation"
    echo "  security      - Security-focused simulation with high threat activity"
    echo "  clean         - Clean simulation without security threats"
    echo "  custom        - Custom simulation with user parameters"
    echo "  logs          - View recent log files"
    echo "  analyze       - Basic log analysis"
    echo "  help          - Show this help message"
    echo ""
    echo "Options for custom:"
    echo "  --duration MINUTES    Duration in minutes"
    echo "  --rpm REQUESTS       Requests per minute" 
    echo "  --no-compromise      Disable compromised host simulation"
    echo "  --no-malicious       Disable malicious traffic"
    echo ""
    echo "Examples:"
    echo "  $0 setup                               # Initial setup"
    echo "  $0 quick                               # 15-minute test"
    echo "  $0 custom --duration 30 --rpm 20      # 30 min with 20 req/min"
    echo "  $0 security                            # High-security simulation"
}

# Function to setup
setup() {
    print_colored $BLUE "Setting up Enhanced Web Traffic Simulator..."
    check_dependencies
    
    print_colored $YELLOW "Creating configuration file..."
    python3 $SCRIPT_NAME --create-config
    
    print_colored $YELLOW "Creating log directory..."
    mkdir -p $LOG_DIR
    
    print_colored $GREEN "Setup completed!"
    print_colored $YELLOW "You can now run: $0 test"
}

# Function to run connectivity test
test_connectivity() {
    print_colored $BLUE "Testing connectivity to sample websites..."
    check_script
    python3 $SCRIPT_NAME --test
}

# Function for quick simulation
quick_simulation() {
    print_colored $BLUE "Starting quick 15-minute simulation..."
    check_script
    python3 $SCRIPT_NAME --duration 15 --rpm 10
}

# Function for normal simulation
normal_simulation() {
    print_colored $BLUE "Starting standard 1-hour simulation..."
    check_script
    python3 $SCRIPT_NAME --duration 60 --rpm 15
}

# Function for extended simulation
extended_simulation() {
    print_colored $BLUE "Starting extended 4-hour simulation..."
    check_script
    python3 $SCRIPT_NAME --duration 240 --rpm 20
}

# Function for security-focused simulation
security_simulation() {
    print_colored $BLUE "Starting security-focused simulation with high threat activity..."
    check_script
    
    # Create custom config for security simulation
    cat > security_config.json << EOF
{
    "request_delay_min": 0.3,
    "request_delay_max": 3.0,
    "timeout": 15,
    "max_workers": 10,
    "compromise_probability": 0.25,
    "malicious_traffic_probability": 0.15,
    "simulate_compromised_host": true,
    "security_simulation_enabled": true,
    "advanced_logging": true
}
EOF
    
    python3 $SCRIPT_NAME --duration 90 --rpm 25 --config security_config.json
    rm security_config.json
}

# Function for clean simulation
clean_simulation() {
    print_colored $BLUE "Starting clean simulation without security threats..."
    check_script
    python3 $SCRIPT_NAME --duration 60 --rpm 15 --no-compromise --no-malicious
}

# Function for custom simulation
custom_simulation() {
    print_colored $BLUE "Starting custom simulation..."
    check_script
    shift # Remove 'custom' from arguments
    python3 $SCRIPT_NAME "$@"
}

# Function to view logs
view_logs() {
    print_colored $BLUE "Recent log files in $LOG_DIR:"
    if [ -d "$LOG_DIR" ]; then
        ls -la $LOG_DIR/
        echo ""
        print_colored $YELLOW "To view a specific log:"
        print_colored $YELLOW "  tail -f $LOG_DIR/traffic.log"
        print_colored $YELLOW "  tail -f $LOG_DIR/security_events.log"
        print_colored $YELLOW "  tail -f $LOG_DIR/compromised_activity.log"
    else
        print_colored $RED "Log directory $LOG_DIR not found. Run a simulation first."
    fi
}

# Function for basic log analysis
analyze_logs() {
    print_colored $BLUE "Basic log analysis:"
    
    if [ ! -d "$LOG_DIR" ]; then
        print_colored $RED "Log directory $LOG_DIR not found. Run a simulation first."
        return
    fi
    
    echo ""
    print_colored $YELLOW "=== Traffic Summary ==="
    if [ -f "$LOG_DIR/traffic.log" ]; then
        total_requests=$(grep -c "SESSION:" "$LOG_DIR/traffic.log" 2>/dev/null || echo "0")
        successful_requests=$(grep -c "STATUS:200" "$LOG_DIR/traffic.log" 2>/dev/null || echo "0")
        failed_requests=$(grep -c "STATUS:[45]" "$LOG_DIR/traffic.log" 2>/dev/null || echo "0")
        
        echo "Total Requests: $total_requests"
        echo "Successful Requests: $successful_requests"
        echo "Failed Requests: $failed_requests"
    else
        print_colored $RED "No traffic log found"
    fi
    
    echo ""
    print_colored $YELLOW "=== Security Events ==="
    if [ -f "$LOG_DIR/security_events.log" ]; then
        security_events=$(grep -c "SESSION:" "$LOG_DIR/security_events.log" 2>/dev/null || echo "0")
        echo "Total Security Events: $security_events"
        
        if [ $security_events -gt 0 ]; then
            echo "Event Types:"
            grep "TYPE:" "$LOG_DIR/security_events.log" | sed 's/.*TYPE:\([^ ]*\).*/\1/' | sort | uniq -c | head -10
        fi
    else
        print_colored $RED "No security events log found"
    fi
    
    echo ""
    print_colored $YELLOW "=== Compromise Activities ==="
    if [ -f "$LOG_DIR/compromised_activity.log" ]; then
        compromise_activities=$(grep -c "SESSION:" "$LOG_DIR/compromised_activity.log" 2>/dev/null || echo "0")
        echo "Total Compromise Activities: $compromise_activities"
        
        if [ $compromise_activities -gt 0 ]; then
            echo "Activity Types:"
            grep "ACTIVITY:" "$LOG_DIR/compromised_activity.log" | sed 's/.*ACTIVITY:\([^ ]*\).*/\1/' | sort | uniq -c | head -10
        fi
    else
        print_colored $RED "No compromise activity log found"
    fi
    
    echo ""
    print_colored $YELLOW "=== DNS Activities ==="
    if [ -f "$LOG_DIR/dns_activity.log" ]; then
        dns_queries=$(grep -c "SESSION:" "$LOG_DIR/dns_activity.log" 2>/dev/null || echo "0")
        echo "Total DNS Queries: $dns_queries"
    else
        print_colored $RED "No DNS activity log found"
    fi
}

# Main script logic
case "$1" in
    setup)
        setup
        ;;
    test)
        test_connectivity
        ;;
    quick)
        quick_simulation
        ;;
    normal)
        normal_simulation
        ;;
    extended)
        extended_simulation
        ;;
    security)
        security_simulation
        ;;
    clean)
        clean_simulation
        ;;
    custom)
        custom_simulation "$@"
        ;;
    logs)
        view_logs
        ;;
    analyze)
        analyze_logs
        ;;
    help|--help|-h)
        show_usage
        ;;
    "")
        print_colored $RED "No command specified"
        echo ""
        show_usage
        ;;
    *)
        print_colored $RED "Unknown command: $1"
        echo ""
        show_usage
        exit 1
        ;;
esac