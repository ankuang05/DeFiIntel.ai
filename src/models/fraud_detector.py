"""
Fraud Detection Module
Implements heuristics and scoring algorithms for detecting DeFi scams and fraud.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta


class FraudDetector:
    """
    Main fraud detection class that combines multiple detection methods.
    """
    
    def __init__(self):
        self.detection_methods = {
            'wallet_analysis': self._analyze_wallet_behavior,
            'token_analysis': self._analyze_token_behavior,
            'social_analysis': self._analyze_social_sentiment,
            'pattern_analysis': self._analyze_suspicious_patterns
        }
    
    def detect_fraud(self, 
                    wallet_data: Optional[Dict] = None,
                    token_data: Optional[Dict] = None,
                    social_data: Optional[Dict] = None) -> Dict:
        """
        Comprehensive fraud detection analysis.
        
        Args:
            wallet_data: Wallet transaction features
            token_data: Token transfer and price data
            social_data: Social sentiment data
            
        Returns:
            Dictionary with fraud detection results
        """
        results = {
            'overall_risk_score': 0,
            'risk_category': 'LOW',
            'fraud_indicators': [],
            'confidence': 0.0,
            'detailed_analysis': {}
        }
        
        # Run individual detection methods
        if wallet_data:
            wallet_results = self._analyze_wallet_behavior(wallet_data)
            results['detailed_analysis']['wallet'] = wallet_results
            results['fraud_indicators'].extend(wallet_results.get('indicators', []))
        
        if token_data:
            token_results = self._analyze_token_behavior(token_data)
            results['detailed_analysis']['token'] = token_results
            results['fraud_indicators'].extend(token_results.get('indicators', []))
        
        if social_data:
            social_results = self._analyze_social_sentiment(social_data)
            results['detailed_analysis']['social'] = social_results
            results['fraud_indicators'].extend(social_results.get('indicators', []))
        
        # Calculate overall risk score
        results['overall_risk_score'] = self._calculate_overall_risk(results)
        results['risk_category'] = self._categorize_risk(results['overall_risk_score'])
        results['confidence'] = self._calculate_confidence(results)
        
        return results
    
    def _analyze_wallet_behavior(self, wallet_data: Dict) -> Dict:
        """Analyze wallet behavior for suspicious patterns."""
        indicators = []
        risk_score = 0
        
        # Rapid transaction detection
        rapid_ratio = wallet_data.get('rapid_transactions_ratio', 0)
        if rapid_ratio > 0.3:
            indicators.append(f"High rapid transaction ratio: {rapid_ratio:.2%}")
            risk_score += 25
        
        # Night activity detection
        night_ratio = wallet_data.get('night_transactions_ratio', 0)
        if night_ratio > 0.6:
            indicators.append(f"High night activity: {night_ratio:.2%}")
            risk_score += 20
        
        # Fee volatility
        fee_volatility = wallet_data.get('fee_volatility', 0)
        if fee_volatility > 2.5:
            indicators.append(f"High fee volatility: {fee_volatility:.2f}")
            risk_score += 15
        
        # Transaction volume patterns
        volume_volatility = wallet_data.get('volume_volatility', 0)
        if volume_volatility > 15:
            indicators.append(f"High volume volatility: {volume_volatility:.2f}")
            risk_score += 10
        
        return {
            'risk_score': min(risk_score, 100),
            'indicators': indicators,
            'suspicious_patterns': len(indicators)
        }
    
    def _analyze_token_behavior(self, token_data: Dict) -> Dict:
        """Analyze token behavior for scam indicators."""
        indicators = []
        risk_score = 0
        
        # Large transfer concentration
        large_transfer_ratio = token_data.get('large_transfer_ratio', 0)
        if large_transfer_ratio > 0.8:
            indicators.append(f"High large transfer concentration: {large_transfer_ratio:.2%}")
            risk_score += 30
        
        # Transfer value volatility
        value_std = token_data.get('value_std', 0)
        avg_value = token_data.get('avg_transfer_value', 1)
        if avg_value > 0 and value_std / avg_value > 5:
            indicators.append(f"High transfer value volatility: {value_std/avg_value:.2f}")
            risk_score += 20
        
        # Transfer frequency patterns
        total_transfers = token_data.get('total_transfers', 0)
        if total_transfers > 1000:  # Very active token
            indicators.append(f"Very high transfer activity: {total_transfers} transfers")
            risk_score += 15
        
        return {
            'risk_score': min(risk_score, 100),
            'indicators': indicators,
            'suspicious_patterns': len(indicators)
        }
    
    def _analyze_social_sentiment(self, social_data: Dict) -> Dict:
        """Analyze social sentiment for manipulation indicators."""
        indicators = []
        risk_score = 0
        
        # Sentiment ratio
        sentiment_ratio = social_data.get('sentiment_ratio', 1.0)
        if sentiment_ratio > 10:  # Excessive positive sentiment
            indicators.append(f"Excessive positive sentiment: {sentiment_ratio:.2f}")
            risk_score += 25
        elif sentiment_ratio < 0.1:  # Very negative sentiment
            indicators.append(f"Very negative sentiment: {sentiment_ratio:.2f}")
            risk_score += 30
        
        # Tweet volume
        tweet_volume = social_data.get('tweet_volume', 0)
        if tweet_volume > 1000:  # High social activity
            indicators.append(f"High social activity: {tweet_volume} tweets")
            risk_score += 15
        
        return {
            'risk_score': min(risk_score, 100),
            'indicators': indicators,
            'suspicious_patterns': len(indicators)
        }
    
    def _analyze_suspicious_patterns(self, data: Dict) -> Dict:
        """Analyze for known scam patterns."""
        indicators = []
        risk_score = 0
        
        # Add pattern-based detection here
        # This could include honeypot detection, rug pull patterns, etc.
        
        return {
            'risk_score': min(risk_score, 100),
            'indicators': indicators,
            'suspicious_patterns': len(indicators)
        }
    
    def _calculate_overall_risk(self, results: Dict) -> int:
        """Calculate overall risk score from all analyses."""
        total_score = 0
        total_weight = 0
        
        # Weight different analysis types
        weights = {
            'wallet': 0.4,    # Wallet behavior is most important
            'token': 0.35,    # Token behavior is second
            'social': 0.25    # Social sentiment is least important
        }
        
        for analysis_type, weight in weights.items():
            if analysis_type in results['detailed_analysis']:
                analysis = results['detailed_analysis'][analysis_type]
                total_score += analysis.get('risk_score', 0) * weight
                total_weight += weight
        
        if total_weight > 0:
            return int(total_score / total_weight)
        return 0
    
    def _categorize_risk(self, risk_score: int) -> str:
        """Categorize risk based on score."""
        if risk_score >= 70:
            return 'HIGH'
        elif risk_score >= 40:
            return 'MEDIUM'
        else:
            return 'LOW'
    
    def _calculate_confidence(self, results: Dict) -> float:
        """Calculate confidence in the analysis."""
        # More indicators = higher confidence
        total_indicators = len(results['fraud_indicators'])
        max_indicators = 10  # Assume max 10 indicators for full confidence
        
        confidence = min(total_indicators / max_indicators, 1.0)
        
        # Boost confidence if multiple analysis types agree
        analysis_types = len(results['detailed_analysis'])
        if analysis_types >= 2:
            confidence = min(confidence + 0.2, 1.0)
        
        return round(confidence, 2)


class HeuristicDetector:
    """
    Rule-based fraud detection using heuristics.
    """
    
    def __init__(self):
        self.heuristics = [
            self._honeypot_detection,
            self._rug_pull_detection,
            self._pump_and_dump_detection,
            self._bot_activity_detection
        ]
    
    def apply_heuristics(self, data: Dict) -> List[Dict]:
        """Apply all heuristics to the data."""
        results = []
        
        for heuristic in self.heuristics:
            result = heuristic(data)
            if result:
                results.append(result)
        
        return results
    
    def _honeypot_detection(self, data: Dict) -> Optional[Dict]:
        """Detect potential honeypot tokens."""
        # Honeypot detection logic would go here
        # This is a placeholder for now
        return None
    
    def _rug_pull_detection(self, data: Dict) -> Optional[Dict]:
        """Detect potential rug pull patterns."""
        # Rug pull detection logic would go here
        # This is a placeholder for now
        return None
    
    def _pump_and_dump_detection(self, data: Dict) -> Optional[Dict]:
        """Detect pump and dump patterns."""
        # Pump and dump detection logic would go here
        # This is a placeholder for now
        return None
    
    def _bot_activity_detection(self, data: Dict) -> Optional[Dict]:
        """Detect bot-like activity patterns."""
        wallet_data = data.get('wallet', {})
        
        # Check for bot indicators
        rapid_ratio = wallet_data.get('rapid_transactions_ratio', 0)
        night_ratio = wallet_data.get('night_transactions_ratio', 0)
        
        if rapid_ratio > 0.5 and night_ratio > 0.7:
            return {
                'type': 'BOT_ACTIVITY',
                'confidence': 0.8,
                'description': 'High rapid transactions with night activity suggests bot behavior',
                'risk_level': 'HIGH'
            }
        
        return None


# Convenience functions
def detect_fraud_comprehensive(wallet_data: Optional[Dict] = None,
                             token_data: Optional[Dict] = None,
                             social_data: Optional[Dict] = None) -> Dict:
    """Convenience function for comprehensive fraud detection."""
    detector = FraudDetector()
    return detector.detect_fraud(wallet_data, token_data, social_data)


def apply_fraud_heuristics(data: Dict) -> List[Dict]:
    """Convenience function for applying heuristics."""
    detector = HeuristicDetector()
    return detector.apply_heuristics(data) 