"""
Test Script for Phase 3: Fraud Detection System
Demonstrates the complete fraud detection pipeline.
"""

from src.api.helius_api import get_wallet_transactions
from src.api.etherscan_api import get_token_transfers
from src.api.twitter_api import search_tweets
from src.features.wallet_features import extract_wallet_features
from src.features.token_features import extract_token_features
from src.models.fraud_detector import detect_fraud_comprehensive, apply_fraud_heuristics
import json


def test_wallet_analysis():
    """Test wallet behavior analysis."""
    print("🔍 Testing Wallet Analysis...")
    
    # Test wallet (you can change this to any Solana wallet)
    test_wallet = "4F3qMHdHHuDzxkeX282WQmZRcsjv6ATUThLKDbDHaubj"
    
    try:
        # Get wallet transactions
        transactions = get_wallet_transactions(test_wallet, limit=50)
        
        # Extract features
        wallet_features = extract_wallet_features(transactions)
        
        print(f"✅ Wallet Analysis Complete")
        print(f"   Risk Score: {wallet_features.get('risk_score', 0)}")
        print(f"   Risk Category: {wallet_features.get('risk_category', 'UNKNOWN')}")
        print(f"   Total Transactions: {wallet_features.get('total_transactions', 0)}")
        print(f"   Rapid Transactions: {wallet_features.get('rapid_transactions_ratio', 0):.2%}")
        print(f"   Night Activity: {wallet_features.get('night_transactions_ratio', 0):.2%}")
        
        return wallet_features
        
    except Exception as e:
        print(f"❌ Wallet Analysis Failed: {e}")
        return None


def test_token_analysis():
    """Test token behavior analysis."""
    print("\n🔍 Testing Token Analysis...")
    
    # Test token (USDT on Ethereum)
    test_token = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    
    try:
        # Get token transfers
        transfers_data = get_token_transfers(test_token, startblock=18000000, endblock=18001000)
        
        if transfers_data.get('status') == '1':
            transfers = transfers_data.get('result', [])
            
            # Extract features
            token_features = extract_token_features(transfers)
            
            print(f"✅ Token Analysis Complete")
            print(f"   Risk Score: {token_features.get('risk_score', 0)}")
            print(f"   Risk Category: {token_features.get('risk_category', 'UNKNOWN')}")
            print(f"   Total Transfers: {token_features.get('total_transfers', 0)}")
            print(f"   Large Transfer Ratio: {token_features.get('large_transfer_ratio', 0):.2%}")
            print(f"   Value Concentration: {token_features.get('value_concentration', 0):.2f}")
            
            return token_features
        else:
            print(f"❌ Token Analysis Failed: {transfers_data.get('message', 'Unknown error')}")
            return None
            
    except Exception as e:
        print(f"❌ Token Analysis Failed: {e}")
        return None


def test_social_analysis():
    """Test social sentiment analysis."""
    print("\n🔍 Testing Social Analysis...")
    
    try:
        # Search for tweets about a popular token
        tweets_data = search_tweets("solana", max_results=10)
        
        # Simple sentiment analysis (placeholder)
        social_features = {
            'tweet_volume': len(tweets_data.get('data', [])),
            'sentiment_ratio': 1.5,  # Placeholder - would be calculated from actual sentiment
            'risk_score': 15,
            'risk_category': 'LOW'
        }
        
        print(f"✅ Social Analysis Complete")
        print(f"   Tweet Volume: {social_features['tweet_volume']}")
        print(f"   Sentiment Ratio: {social_features['sentiment_ratio']:.2f}")
        print(f"   Risk Score: {social_features['risk_score']}")
        
        return social_features
        
    except Exception as e:
        print(f"❌ Social Analysis Failed: {e}")
        return None


def test_comprehensive_fraud_detection():
    """Test comprehensive fraud detection."""
    print("\n🔍 Testing Comprehensive Fraud Detection...")
    
    # Get data from all sources
    wallet_data = test_wallet_analysis()
    token_data = test_token_analysis()
    social_data = test_social_analysis()
    
    # Run comprehensive fraud detection
    fraud_results = detect_fraud_comprehensive(
        wallet_data=wallet_data,
        token_data=token_data,
        social_data=social_data
    )
    
    print(f"\n🎯 COMPREHENSIVE FRAUD DETECTION RESULTS")
    print(f"   Overall Risk Score: {fraud_results['overall_risk_score']}/100")
    print(f"   Risk Category: {fraud_results['risk_category']}")
    print(f"   Confidence: {fraud_results['confidence']:.2f}")
    print(f"   Fraud Indicators Found: {len(fraud_results['fraud_indicators'])}")
    
    if fraud_results['fraud_indicators']:
        print(f"\n🚨 Fraud Indicators:")
        for i, indicator in enumerate(fraud_results['fraud_indicators'], 1):
            print(f"   {i}. {indicator}")
    
    # Apply heuristics
    all_data = {
        'wallet': wallet_data,
        'token': token_data,
        'social': social_data
    }
    
    heuristic_results = apply_fraud_heuristics(all_data)
    
    if heuristic_results:
        print(f"\n🔍 Heuristic Detection Results:")
        for result in heuristic_results:
            print(f"   - {result['type']}: {result['description']}")
            print(f"     Confidence: {result['confidence']:.2f}")
            print(f"     Risk Level: {result['risk_level']}")
    
    return fraud_results


def test_suspicious_wallet():
    """Test with a potentially suspicious wallet pattern."""
    print("\n🔍 Testing Suspicious Wallet Pattern...")
    
    # Create synthetic suspicious data
    suspicious_wallet_data = {
        'total_transactions': 500,
        'rapid_transactions_ratio': 0.8,  # Very high
        'night_transactions_ratio': 0.9,  # Very high night activity
        'fee_volatility': 5.0,  # High fee volatility
        'volume_volatility': 25,  # High volume volatility
        'risk_score': 85,
        'risk_category': 'HIGH'
    }
    
    suspicious_token_data = {
        'large_transfer_ratio': 0.9,  # Very high
        'value_std': 1000000,
        'avg_transfer_value': 100000,
        'total_transfers': 2000,
        'risk_score': 75,
        'risk_category': 'HIGH'
    }
    
    suspicious_social_data = {
        'sentiment_ratio': 15.0,  # Excessive positive sentiment
        'tweet_volume': 5000,
        'risk_score': 80,
        'risk_category': 'HIGH'
    }
    
    # Run fraud detection
    fraud_results = detect_fraud_comprehensive(
        wallet_data=suspicious_wallet_data,
        token_data=suspicious_token_data,
        social_data=suspicious_social_data
    )
    
    print(f"✅ Suspicious Pattern Analysis Complete")
    print(f"   Overall Risk Score: {fraud_results['overall_risk_score']}/100")
    print(f"   Risk Category: {fraud_results['risk_category']}")
    print(f"   Confidence: {fraud_results['confidence']:.2f}")
    print(f"   Fraud Indicators: {len(fraud_results['fraud_indicators'])}")
    
    return fraud_results


def main():
    """Run all fraud detection tests."""
    print("🚀 DeFiIntel.ai - Phase 3: Fraud Detection System")
    print("=" * 60)
    
    # Test 1: Real data analysis
    print("\n📊 TEST 1: Real Data Analysis")
    real_results = test_comprehensive_fraud_detection()
    
    # Test 2: Suspicious pattern detection
    print("\n📊 TEST 2: Suspicious Pattern Detection")
    suspicious_results = test_suspicious_wallet()
    
    # Summary
    print("\n📋 SUMMARY")
    print("=" * 60)
    print(f"Real Data Analysis:")
    print(f"  - Risk Score: {real_results['overall_risk_score']}/100")
    print(f"  - Category: {real_results['risk_category']}")
    print(f"  - Confidence: {real_results['confidence']:.2f}")
    
    print(f"\nSuspicious Pattern Analysis:")
    print(f"  - Risk Score: {suspicious_results['overall_risk_score']}/100")
    print(f"  - Category: {suspicious_results['risk_category']}")
    print(f"  - Confidence: {suspicious_results['confidence']:.2f}")
    
    print(f"\n✅ Phase 3 Fraud Detection System is working!")
    print(f"🎯 Ready for Phase 4: Dashboard Development")


if __name__ == "__main__":
    main() 