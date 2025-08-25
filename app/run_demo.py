#!/usr/bin/env python3
"""
DeFiIntel.ai Dashboard Demo Runner
Quick setup and run script for demonstrating the fraud detection dashboard.
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'streamlit', 'plotly', 'pandas', 'numpy', 
        'requests', 'python-dotenv', 'scikit-learn', 'joblib'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - missing")
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
        print("✅ Dependencies installed!")
    else:
        print("✅ All dependencies are installed!")

def setup_environment():
    """Set up environment variables for demo."""
    print("\n🔧 Setting up environment...")
    
    # Create .env file if it doesn't exist
    env_file = Path(".env")
    if not env_file.exists():
        print("📝 Creating .env file with demo API keys...")
        env_content = """# Demo API Keys (replace with real keys for production)
HELIUS_API_KEY=demo_key_helius
ETHERSCAN_API_KEY=demo_key_etherscan
TWITTER_BEARER_TOKEN=demo_key_twitter
COINGECKO_API_KEY=demo_key_coingecko
"""
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ .env file created with demo keys")
    else:
        print("✅ .env file already exists")

def run_dashboard():
    """Run the Streamlit dashboard."""
    print("\n🚀 Starting DeFiIntel.ai Dashboard...")
    print("📊 Dashboard will open in your browser at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the dashboard")
    
    try:
        # Run streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Thanks for trying DeFiIntel.ai!")

def main():
    """Main demo runner."""
    print("=" * 60)
    print("🎯 DeFiIntel.ai Dashboard Demo")
    print("=" * 60)
    print("This will set up and run the fraud detection dashboard.")
    print()
    
    # Check if we're in the right directory
    if not Path("streamlit_app.py").exists():
        print("❌ Error: streamlit_app.py not found!")
        print("Please run this script from the 'app' directory.")
        sys.exit(1)
    
    # Setup
    check_dependencies()
    setup_environment()
    
    # Run dashboard
    run_dashboard()

if __name__ == "__main__":
    main() 