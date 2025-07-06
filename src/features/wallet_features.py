"""
Wallet Feature Engineering for Fraud Detection
Extracts features from wallet transaction data to identify suspicious behavior.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class WalletFeatureExtractor:
    """
    Extracts fraud detection features from wallet transaction data.
    """
    
    def __init__(self):
        self.features = {}
    
    def extract_features(self, transactions: List[Dict]) -> Dict[str, float]:
        """
        Extract comprehensive fraud detection features from wallet transactions.
        
        Args:
            transactions: List of transaction dictionaries from Helius API
            
        Returns:
            Dictionary of feature names and values
        """
        if not transactions:
            return self._get_empty_features()
        
        # Convert to DataFrame
        df = pd.DataFrame(transactions)
        
        # Extract features
        self._extract_basic_features(df)
        self._extract_temporal_features(df)
        self._extract_fee_features(df)
        self._extract_behavioral_features(df)
        self._extract_risk_features(df)
        
        return self.features
    
    def _extract_basic_features(self, df: pd.DataFrame):
        """Extract basic transaction statistics."""
        self.features['total_transactions'] = len(df)
        self.features['unique_days'] = self._get_unique_days(df)
        self.features['avg_transactions_per_day'] = self.features['total_transactions'] / max(self.features['unique_days'], 1)
        
        # Transaction types
        if 'type' in df.columns:
            type_counts = df['type'].value_counts()
            self.features['transfer_ratio'] = type_counts.get('TRANSFER', 0) / len(df)
            self.features['swap_ratio'] = type_counts.get('SWAP', 0) / len(df)
    
    def _extract_temporal_features(self, df: pd.DataFrame):
        """Extract time-based features."""
        if 'timestamp' not in df.columns:
            return
        
        # Convert timestamp
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df = df.sort_values('timestamp')
        
        # Time differences
        time_diffs = df['timestamp'].diff().dt.total_seconds()
        self.features['avg_time_between_txns'] = time_diffs.mean() if not time_diffs.empty else 0
        self.features['min_time_between_txns'] = time_diffs.min() if not time_diffs.empty else 0
        
        # Rapid transaction detection
        rapid_txns = time_diffs[time_diffs < 60]  # Less than 1 minute
        self.features['rapid_transactions_ratio'] = len(rapid_txns) / len(df)
        
        # Hour-based features
        df['hour'] = df['timestamp'].dt.hour
        hour_dist = df['hour'].value_counts()
        
        # Night activity (10 PM - 6 AM)
        night_hours = [22, 23, 0, 1, 2, 3, 4, 5, 6]
        night_txns = df[df['hour'].isin(night_hours)]
        self.features['night_transactions_ratio'] = len(night_txns) / len(df)
        
        # Peak hour activity (9 AM - 5 PM)
        peak_hours = list(range(9, 18))
        peak_txns = df[df['hour'].isin(peak_hours)]
        self.features['peak_hour_ratio'] = len(peak_txns) / len(df)
    
    def _extract_fee_features(self, df: pd.DataFrame):
        """Extract fee-related features."""
        if 'fee' not in df.columns:
            return
        
        fees_series = pd.to_numeric(df['fee'], errors='coerce')
        fees = fees_series.dropna()
        
        if len(fees) == 0:
            return
        
        self.features['avg_fee'] = fees.mean()
        self.features['fee_std'] = fees.std()
        self.features['min_fee'] = fees.min()
        self.features['max_fee'] = fees.max()
        
        # Fee volatility (coefficient of variation)
        self.features['fee_volatility'] = fees.std() / fees.mean() if fees.mean() > 0 else 0
        
        # High fee transactions
        fee_95th = fees.quantile(0.95)
        high_fees = fees[fees > fee_95th]
        self.features['high_fee_ratio'] = len(high_fees) / len(fees)
    
    def _extract_behavioral_features(self, df: pd.DataFrame):
        """Extract behavioral pattern features."""
        # Transaction volume patterns
        if 'timestamp' in df.columns and 'fee' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
            df['date'] = df['timestamp'].dt.date
            
            # Daily transaction volume
            daily_volume = df.groupby('date').size()
            self.features['daily_volume_std'] = daily_volume.std()
            self.features['max_daily_transactions'] = daily_volume.max()
            
            # Burst activity detection
            if len(daily_volume) > 1:
                volume_changes = daily_volume.diff().abs()
                self.features['volume_volatility'] = volume_changes.mean()
    
    def _extract_risk_features(self, df: pd.DataFrame):
        """Extract risk indicators."""
        # Combine multiple risk factors
        risk_score = 0
        
        # High rapid transaction ratio
        if self.features.get('rapid_transactions_ratio', 0) > 0.2:
            risk_score += 30
        
        # High night activity
        if self.features.get('night_transactions_ratio', 0) > 0.5:
            risk_score += 20
        
        # High fee volatility
        if self.features.get('fee_volatility', 0) > 2.0:
            risk_score += 25
        
        # Low transaction diversity
        if self.features.get('transfer_ratio', 0) > 0.9:
            risk_score += 15
        
        # High volume volatility
        if self.features.get('volume_volatility', 0) > 10:
            risk_score += 10
        
        self.features['risk_score'] = min(risk_score, 100)
        
        # Risk categories
        if risk_score >= 70:
            self.features['risk_category'] = 'HIGH'
        elif risk_score >= 40:
            self.features['risk_category'] = 'MEDIUM'
        else:
            self.features['risk_category'] = 'LOW'
    
    def _get_unique_days(self, df: pd.DataFrame) -> int:
        """Get number of unique days with transactions."""
        if 'timestamp' not in df.columns:
            return 1
        
        try:
            timestamps = pd.to_datetime(df['timestamp'], unit='s')
            unique_days = timestamps.dt.date.nunique()
            return max(unique_days, 1)
        except:
            return 1
    
    def _get_empty_features(self) -> Dict[str, float]:
        """Return empty feature set."""
        return {
            'total_transactions': 0,
            'unique_days': 1,
            'avg_transactions_per_day': 0,
            'transfer_ratio': 0,
            'swap_ratio': 0,
            'avg_time_between_txns': 0,
            'min_time_between_txns': 0,
            'rapid_transactions_ratio': 0,
            'night_transactions_ratio': 0,
            'peak_hour_ratio': 0,
            'avg_fee': 0,
            'fee_std': 0,
            'min_fee': 0,
            'max_fee': 0,
            'fee_volatility': 0,
            'high_fee_ratio': 0,
            'daily_volume_std': 0,
            'max_daily_transactions': 0,
            'volume_volatility': 0,
            'risk_score': 0,
            'risk_category': 'LOW'
        }


def extract_wallet_features(transactions: List[Dict]) -> Dict[str, float]:
    """
    Convenience function to extract wallet features.
    
    Args:
        transactions: List of transaction dictionaries
        
    Returns:
        Dictionary of extracted features
    """
    extractor = WalletFeatureExtractor()
    return extractor.extract_features(transactions) 