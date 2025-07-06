"""
Token Feature Engineering for Fraud Detection
Extracts features from token transfer data to identify suspicious behavior.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class TokenFeatureExtractor:
    """
    Extracts fraud detection features from token transfer data.
    """
    
    def __init__(self):
        self.features = {}
    
    def extract_features(self, transfers: List[Dict]) -> Dict[str, float]:
        """
        Extract comprehensive fraud detection features from token transfers.
        
        Args:
            transfers: List of token transfer dictionaries from Etherscan API
            
        Returns:
            Dictionary of feature names and values
        """
        if not transfers:
            return self._get_empty_features()
        
        # Convert to DataFrame
        df = pd.DataFrame(transfers)
        
        # Extract features
        self._extract_basic_features(df)
        self._extract_value_features(df)
        self._extract_temporal_features(df)
        self._extract_address_features(df)
        self._extract_risk_features(df)
        
        return self.features
    
    def _extract_basic_features(self, df: pd.DataFrame):
        """Extract basic transfer statistics."""
        self.features['total_transfers'] = len(df)
        self.features['unique_days'] = self._get_unique_days(df)
        self.features['avg_transfers_per_day'] = self.features['total_transfers'] / max(self.features['unique_days'], 1)
        
        # Transfer directions
        if 'from' in df.columns and 'to' in df.columns:
            # Count unique addresses
            unique_from = df['from'].nunique()
            unique_to = df['to'].nunique()
            self.features['unique_senders'] = unique_from
            self.features['unique_receivers'] = unique_to
            self.features['address_diversity'] = (unique_from + unique_to) / (2 * self.features['total_transfers'])
    
    def _extract_value_features(self, df: pd.DataFrame):
        """Extract value-related features."""
        if 'value' not in df.columns:
            return
        
        # Convert value to numeric
        values_series = pd.to_numeric(df['value'], errors='coerce')
        values = values_series.dropna()
        
        if len(values) == 0:
            return
        
        self.features['avg_transfer_value'] = values.mean()
        self.features['value_std'] = values.std()
        self.features['min_transfer_value'] = values.min()
        self.features['max_transfer_value'] = values.max()
        
        # Value distribution features
        self.features['value_volatility'] = values.std() / values.mean() if values.mean() > 0 else 0
        
        # Large transfer detection
        value_95th = values.quantile(0.95)
        large_transfers = values[values > value_95th]
        self.features['large_transfer_ratio'] = len(large_transfers) / len(values)
        
        # Small transfer detection (dust)
        value_5th = values.quantile(0.05)
        small_transfers = values[values < value_5th]
        self.features['dust_transfer_ratio'] = len(small_transfers) / len(values)
        
        # Transfer value concentration
        total_value = values.sum()
        if total_value > 0:
            # Gini coefficient approximation for value concentration
            sorted_values = np.sort(values)
            n = len(sorted_values)
            cumsum = np.cumsum(sorted_values)
            gini = (n + 1 - 2 * np.sum(cumsum) / cumsum[-1]) / n
            self.features['value_concentration'] = gini
    
    def _extract_temporal_features(self, df: pd.DataFrame):
        """Extract time-based features."""
        if 'timeStamp' not in df.columns:
            return
        
        # Convert timestamp
        df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
        df = df.sort_values('timeStamp')
        
        # Time differences
        time_diffs = df['timeStamp'].diff().dt.total_seconds()
        self.features['avg_time_between_transfers'] = time_diffs.mean() if not time_diffs.empty else 0
        self.features['min_time_between_transfers'] = time_diffs.min() if not time_diffs.empty else 0
        
        # Rapid transfer detection
        rapid_transfers = time_diffs[time_diffs < 300]  # Less than 5 minutes
        self.features['rapid_transfers_ratio'] = len(rapid_transfers) / len(df)
        
        # Hour-based features
        df['hour'] = df['timeStamp'].dt.hour
        
        # Night activity (10 PM - 6 AM)
        night_hours = [22, 23, 0, 1, 2, 3, 4, 5, 6]
        night_transfers = df[df['hour'].isin(night_hours)]
        self.features['night_transfers_ratio'] = len(night_transfers) / len(df)
        
        # Peak hour activity (9 AM - 5 PM)
        peak_hours = list(range(9, 18))
        peak_transfers = df[df['hour'].isin(peak_hours)]
        self.features['peak_hour_ratio'] = len(peak_transfers) / len(df)
    
    def _extract_address_features(self, df: pd.DataFrame):
        """Extract address-related features."""
        if 'from' not in df.columns or 'to' not in df.columns:
            return
        
        # Address reuse patterns
        from_counts = df['from'].value_counts()
        to_counts = df['to'].value_counts()
        
        # Top sender/receiver concentration
        top_sender_ratio = from_counts.iloc[0] / len(df) if len(from_counts) > 0 else 0
        top_receiver_ratio = to_counts.iloc[0] / len(df) if len(to_counts) > 0 else 0
        
        self.features['top_sender_concentration'] = top_sender_ratio
        self.features['top_receiver_concentration'] = top_receiver_ratio
        
        # Address diversity
        self.features['sender_diversity'] = from_counts.nunique() / len(df)
        self.features['receiver_diversity'] = to_counts.nunique() / len(df)
        
        # Self-transfers (same address sending to itself)
        self_transfers = df[df['from'] == df['to']]
        self.features['self_transfer_ratio'] = len(self_transfers) / len(df)
    
    def _extract_risk_features(self, df: pd.DataFrame):
        """Extract risk indicators."""
        # Combine multiple risk factors
        risk_score = 0
        
        # High rapid transfer ratio
        if self.features.get('rapid_transfers_ratio', 0) > 0.3:
            risk_score += 25
        
        # High night activity
        if self.features.get('night_transfers_ratio', 0) > 0.6:
            risk_score += 20
        
        # High value concentration
        if self.features.get('value_concentration', 0) > 0.8:
            risk_score += 30
        
        # Low address diversity
        if self.features.get('address_diversity', 1) < 0.1:
            risk_score += 20
        
        # High large transfer ratio
        if self.features.get('large_transfer_ratio', 0) > 0.5:
            risk_score += 15
        
        # High self-transfer ratio
        if self.features.get('self_transfer_ratio', 0) > 0.2:
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
        """Get number of unique days with transfers."""
        if 'timeStamp' not in df.columns:
            return 1
        
        try:
            timestamps = pd.to_datetime(df['timeStamp'], unit='s')
            unique_days = timestamps.dt.date.nunique()
            return max(unique_days, 1)
        except:
            return 1
    
    def _get_empty_features(self) -> Dict[str, float]:
        """Return empty feature set."""
        return {
            'total_transfers': 0,
            'unique_days': 1,
            'avg_transfers_per_day': 0,
            'unique_senders': 0,
            'unique_receivers': 0,
            'address_diversity': 0,
            'avg_transfer_value': 0,
            'value_std': 0,
            'min_transfer_value': 0,
            'max_transfer_value': 0,
            'value_volatility': 0,
            'large_transfer_ratio': 0,
            'dust_transfer_ratio': 0,
            'value_concentration': 0,
            'avg_time_between_transfers': 0,
            'min_time_between_transfers': 0,
            'rapid_transfers_ratio': 0,
            'night_transfers_ratio': 0,
            'peak_hour_ratio': 0,
            'top_sender_concentration': 0,
            'top_receiver_concentration': 0,
            'sender_diversity': 0,
            'receiver_diversity': 0,
            'self_transfer_ratio': 0,
            'risk_score': 0,
            'risk_category': 'LOW'
        }


def extract_token_features(transfers: List[Dict]) -> Dict[str, float]:
    """
    Convenience function to extract token features.
    
    Args:
        transfers: List of transfer dictionaries
        
    Returns:
        Dictionary of extracted features
    """
    extractor = TokenFeatureExtractor()
    return extractor.extract_features(transfers) 