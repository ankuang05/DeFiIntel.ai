#!/usr/bin/env python3
"""
DeFiIntel.ai Dashboard Launcher
Run this script to start the Streamlit dashboard
"""

import subprocess
import sys
import os

def main():
    print("🚀 Starting DeFiIntel.ai Dashboard...")
    print("📊 Dashboard will open in your browser at http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the dashboard")
    print("-" * 50)
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the script directory
    os.chdir(script_dir)
    
    # Run streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")
        print("💡 Make sure you have installed the requirements:")
        print("   pip install -r app/requirements.txt")

if __name__ == "__main__":
    main() 