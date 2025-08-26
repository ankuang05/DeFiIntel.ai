#!/usr/bin/env python3
"""
Test script for ML Fraud Detector
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.models.ml_detector import MLFraudDetector, FeatureAggregator
import pandas as pd

def test_ml_detector():
    """Test the ML detector with sample data"""
    print("🧪 Testing ML Fraud Detector...")
    
    # Create sample features
    sample_features = {
        'total_transactions': 150,
        'avg_transactions_per_day': 5.2,
        'rapid_transactions_ratio': 0.3,
        'night_transactions_ratio': 0.6,
        'fee_volatility': 2.5,
        'volume_volatility': 1.8,
        'total_transfers': 120,
        'large_transfer_ratio': 0.4,
        'value_concentration': 0.7,
        'address_diversity': 0.3,
        'self_transfer_ratio': 0.15,
        'tweet_volume': 50,
        'sentiment_ratio': 0.3
    }
    
    # Initialize detector
    detector = MLFraudDetector()
    
    # Test prediction
    print("\n📊 Making prediction...")
    result = detector.predict_fraud(sample_features)
    
    print(f"✅ Prediction Result:")
    print(f"   Model Type: {result.get('model_type', 'UNKNOWN')}")
    print(f"   Fraud Probability: {result.get('fraud_probability', 0):.3f}")
    print(f"   Prediction: {result.get('prediction', 'UNKNOWN')}")
    print(f"   Confidence: {result.get('confidence', 0):.3f}")
    print(f"   Risk Score: {result.get('risk_score', 0):.1f}/100")
    
    if 'risk_factors' in result:
        print(f"   Risk Factors: {result.get('risk_factors', 0)}/{result.get('total_factors', 1)}")
    
    # Test with different risk levels
    print("\n🧪 Testing different risk scenarios...")
    
    # Low risk scenario
    low_risk_features = {
        'rapid_transactions_ratio': 0.1,
        'night_transactions_ratio': 0.2,
        'fee_volatility': 0.5,
        'large_transfer_ratio': 0.1,
        'self_transfer_ratio': 0.05
    }
    
    low_result = detector.predict_fraud(low_risk_features)
    print(f"   Low Risk Score: {low_result.get('risk_score', 0):.1f}/100")
    
    # High risk scenario
    high_risk_features = {
        'rapid_transactions_ratio': 0.8,
        'night_transactions_ratio': 0.9,
        'fee_volatility': 5.0,
        'large_transfer_ratio': 0.8,
        'self_transfer_ratio': 0.4
    }
    
    high_result = detector.predict_fraud(high_risk_features)
    print(f"   High Risk Score: {high_result.get('risk_score', 0):.1f}/100")
    
    print("\n✅ ML Detector test completed successfully!")

def test_feature_aggregator():
    """Test the feature aggregator"""
    print("\n🧪 Testing Feature Aggregator...")
    
    aggregator = FeatureAggregator()
    
    # Add sample data
    wallet_features = {
        'total_transactions': 100,
        'rapid_transactions_ratio': 0.3
    }
    
    token_features = {
        'total_transfers': 80,
        'large_transfer_ratio': 0.4
    }
    
    social_features = {
        'tweet_volume': 25,
        'sentiment_ratio': 0.6
    }
    
    # Add samples
    aggregator.add_sample(wallet_features, token_features, social_features, label=1)  # Fraud
    aggregator.add_sample(wallet_features, token_features, social_features, label=0)  # Legitimate
    
    # Get training data
    df, labels = aggregator.get_training_data()
    
    print(f"✅ Feature Aggregator test completed!")
    print(f"   Samples: {len(df)}")
    print(f"   Features: {len(df.columns)}")
    print(f"   Labels: {len(labels) if labels else 0}")

if __name__ == "__main__":
    test_ml_detector()
    test_feature_aggregator() 