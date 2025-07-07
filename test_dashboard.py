#!/usr/bin/env python3
"""
Test script for DeFiIntel.ai Dashboard
Tests the core functionality without running the full Streamlit app
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        from api.helius_api import get_wallet_transactions
        from api.coingecko_api import get_token_data_solana
        from api.etherscan_api import get_token_transfers
        from api.twitter_api import search_tweets
        print("✅ API modules imported successfully")
    except ImportError as e:
        print(f"❌ API import error: {e}")
        return False
    
    try:
        from features.wallet_features import extract_wallet_features
        from features.token_features import extract_token_features
        print("✅ Feature modules imported successfully")
    except ImportError as e:
        print(f"❌ Feature import error: {e}")
        return False
    
    try:
        from models.fraud_detector import FraudDetector
        from models.ml_detector import MLFraudDetector
        print("✅ Model modules imported successfully")
    except ImportError as e:
        print(f"❌ Model import error: {e}")
        return False
    
    try:
        import streamlit as st
        import plotly.express as px
        import pandas as pd
        import numpy as np
        print("✅ Dashboard dependencies imported successfully")
    except ImportError as e:
        print(f"❌ Dashboard dependency import error: {e}")
        return False
    
    return True

def test_api_functionality():
    """Test API functionality"""
    print("\n🔍 Testing API functionality...")
    
    try:
        # Test wallet analysis
        wallet = "4F3qMHdHHuDzxkeX282WQmZRcsjv6ATUThLKDbDHaubj"
        transactions = get_wallet_transactions(wallet, limit=10)
        print(f"✅ Wallet transactions fetched: {len(transactions)} transactions")
        
        # Test token data
        token = "So11111111111111111111111111111111111111112"
        token_data = get_token_data_solana(token)
        print("✅ Token data fetched successfully")
        
        # Test Ethereum transfers
        eth_token = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
        eth_transfers = get_token_transfers(eth_token)
        print("✅ Ethereum transfers fetched successfully")
        
        return True
    except Exception as e:
        print(f"❌ API test error: {e}")
        return False

def test_feature_extraction():
    """Test feature extraction functionality"""
    print("\n🔍 Testing feature extraction...")
    
    try:
        # Test wallet features
        wallet = "4F3qMHdHHuDzxkeX282WQmZRcsjv6ATUThLKDbDHaubj"
        transactions = get_wallet_transactions(wallet, limit=20)
        
        if transactions:
            wallet_features = extract_wallet_features(transactions)
            print(f"✅ Wallet features extracted: {len(wallet_features)} features")
            print(f"   Risk score: {wallet_features.get('risk_score', 0):.1f}")
        
        return True
    except Exception as e:
        print(f"❌ Feature extraction error: {e}")
        return False

def test_fraud_detection():
    """Test fraud detection functionality"""
    print("\n🔍 Testing fraud detection...")
    
    try:
        # Test fraud detector
        detector = FraudDetector()
        print("✅ Fraud detector initialized")
        
        # Test ML detector
        ml_detector = MLFraudDetector()
        print("✅ ML detector initialized")
        
        return True
    except Exception as e:
        print(f"❌ Fraud detection error: {e}")
        return False

def test_dashboard_components():
    """Test dashboard component functions"""
    print("\n🔍 Testing dashboard components...")
    
    try:
        # Test data processing
        import pandas as pd
        import numpy as np
        
        # Create sample data
        sample_data = {
            'timestamp': pd.date_range('2024-01-01', periods=10, freq='D'),
            'value': np.random.randn(10),
            'type': ['TRANSFER'] * 5 + ['SWAP'] * 5
        }
        df = pd.DataFrame(sample_data)
        print("✅ Sample data created for dashboard")
        
        # Test visualization data preparation
        daily_counts = df.groupby(df['timestamp'].dt.date).size()
        print(f"✅ Data aggregation for charts: {len(daily_counts)} days")
        
        return True
    except Exception as e:
        print(f"❌ Dashboard component error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 DeFiIntel.ai Dashboard Test Suite")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("API Functionality", test_api_functionality),
        ("Feature Extraction", test_feature_extraction),
        ("Fraud Detection", test_fraud_detection),
        ("Dashboard Components", test_dashboard_components)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name}...")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary")
    print("=" * 50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! Dashboard is ready to run.")
        print("\n💡 To start the dashboard:")
        print("   python app/run_dashboard.py")
        print("   or")
        print("   streamlit run app/streamlit_app.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == len(results)

if __name__ == "__main__":
    main() 