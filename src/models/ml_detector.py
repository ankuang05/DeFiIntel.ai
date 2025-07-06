"""
Machine Learning Fraud Detection Module
Implements ML models for predictive fraud detection.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os


class MLFraudDetector:
    """
    Machine learning-based fraud detection using ensemble methods.
    """
    
    def __init__(self, model_path: str = "models/fraud_detector.pkl"):
        self.model_path = model_path
        self.rf_model = None
        self.isolation_model = None
        self.scaler = StandardScaler()
        self.is_trained = False
        
        # Load existing model if available
        self._load_model()
    
    def train_model(self, features_df: pd.DataFrame, labels: Optional[List[int]] = None):
        """
        Train the fraud detection model.
        
        Args:
            features_df: DataFrame with extracted features
            labels: Binary labels (1 for fraud, 0 for legitimate)
        """
        print("🤖 Training ML Fraud Detection Model...")
        
        # Prepare features
        feature_columns = self._get_feature_columns()
        X = features_df[feature_columns].fillna(0).astype(float)
        
        # If no labels provided, use unsupervised learning
        if labels is None:
            self._train_unsupervised(X)
        else:
            self._train_supervised(X, labels)
        
        self.is_trained = True
        self._save_model()
        print("✅ Model training complete!")
    
    def _train_supervised(self, X: pd.DataFrame, y: List[int]):
        """Train supervised Random Forest model."""
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        # Train Random Forest
        self.rf_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        )
        
        self.rf_model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.rf_model.predict(X_test)
        print("\n📊 Supervised Model Performance:")
        print(classification_report(y_test, y_pred))
    
    def _train_unsupervised(self, X: pd.DataFrame):
        """Train unsupervised Isolation Forest model."""
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train Isolation Forest
        self.isolation_model = IsolationForest(
            contamination=0.1,  # Assume 10% of data is anomalous
            random_state=42
        )
        
        self.isolation_model.fit(X_scaled)
        print("✅ Unsupervised model training complete!")
    
    def predict_fraud(self, features: Dict[str, float]) -> Dict:
        """
        Predict fraud probability for given features.
        
        Args:
            features: Dictionary of extracted features
            
        Returns:
            Dictionary with prediction results
        """
        if not self.is_trained:
            return {
                'fraud_probability': 0.5,
                'prediction': 'UNKNOWN',
                'confidence': 0.0,
                'model_type': 'UNTRAINED'
            }
        
        # Prepare features
        feature_columns = self._get_feature_columns()
        feature_vector = []
        
        for col in feature_columns:
            feature_vector.append(features.get(col, 0))
        
        X = np.array(feature_vector).reshape(1, -1)
        X_scaled = self.scaler.transform(X)
        
        # Make prediction
        if self.rf_model is not None:
            # Supervised prediction
            fraud_prob = self.rf_model.predict_proba(X_scaled)[0][1]
            prediction = 'FRAUD' if fraud_prob > 0.5 else 'LEGITIMATE'
            confidence = max(fraud_prob, 1 - fraud_prob)
            
            return {
                'fraud_probability': round(fraud_prob, 3),
                'prediction': prediction,
                'confidence': round(confidence, 3),
                'model_type': 'SUPERVISED_RF'
            }
        
        elif self.isolation_model is not None:
            # Unsupervised prediction
            anomaly_score = self.isolation_model.decision_function(X_scaled)[0]
            # Convert to probability (lower score = more anomalous)
            fraud_prob = 1 / (1 + np.exp(anomaly_score))
            prediction = 'FRAUD' if fraud_prob > 0.5 else 'LEGITIMATE'
            confidence = max(fraud_prob, 1 - fraud_prob)
            
            return {
                'fraud_probability': round(fraud_prob, 3),
                'prediction': prediction,
                'confidence': round(confidence, 3),
                'model_type': 'UNSUPERVISED_ISOLATION',
                'anomaly_score': round(anomaly_score, 3)
            }
        
        return {
            'fraud_probability': 0.5,
            'prediction': 'UNKNOWN',
            'confidence': 0.0,
            'model_type': 'NO_MODEL'
        }
    
    def _get_feature_columns(self) -> List[str]:
        """Get list of feature columns for ML model."""
        return [
            'total_transactions',
            'avg_transactions_per_day',
            'rapid_transactions_ratio',
            'night_transactions_ratio',
            'fee_volatility',
            'volume_volatility',
            'total_transfers',
            'large_transfer_ratio',
            'value_concentration',
            'address_diversity',
            'self_transfer_ratio',
            'tweet_volume',
            'sentiment_ratio'
        ]
    
    def _save_model(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        
        model_data = {
            'rf_model': self.rf_model,
            'isolation_model': self.isolation_model,
            'scaler': self.scaler,
            'is_trained': self.is_trained
        }
        
        joblib.dump(model_data, self.model_path)
        print(f"💾 Model saved to {self.model_path}")
    
    def _load_model(self):
        """Load trained model from disk."""
        try:
            if os.path.exists(self.model_path):
                model_data = joblib.load(self.model_path)
                self.rf_model = model_data['rf_model']
                self.isolation_model = model_data['isolation_model']
                self.scaler = model_data['scaler']
                self.is_trained = model_data['is_trained']
                print(f"📂 Model loaded from {self.model_path}")
        except Exception as e:
            print(f"⚠️ Could not load model: {e}")


class FeatureAggregator:
    """
    Aggregates features from multiple sources for ML training.
    """
    
    def __init__(self):
        self.features = []
        self.labels = []
    
    def add_sample(self, wallet_features: Dict, token_features: Dict, 
                  social_features: Dict, label: int = None):
        """
        Add a sample to the training dataset.
        
        Args:
            wallet_features: Wallet behavior features
            token_features: Token transfer features
            social_features: Social sentiment features
            label: Binary label (1 for fraud, 0 for legitimate)
        """
        # Combine all features
        combined_features = {}
        combined_features.update(wallet_features or {})
        combined_features.update(token_features or {})
        combined_features.update(social_features or {})
        
        self.features.append(combined_features)
        
        if label is not None:
            self.labels.append(label)
    
    def get_training_data(self) -> Tuple[pd.DataFrame, Optional[List[int]]]:
        """Get training data as DataFrame and labels."""
        df = pd.DataFrame(self.features)
        
        if self.labels:
            return df, self.labels
        else:
            return df, None
    
    def clear_data(self):
        """Clear all training data."""
        self.features = []
        self.labels = []


# Convenience functions
def create_ml_detector(model_path: str = "models/fraud_detector.pkl") -> MLFraudDetector:
    """Create and return an ML fraud detector instance."""
    return MLFraudDetector(model_path)


def predict_fraud_ml(features: Dict[str, float], 
                    model_path: str = "models/fraud_detector.pkl") -> Dict:
    """Convenience function for ML-based fraud prediction."""
    detector = MLFraudDetector(model_path)
    return detector.predict_fraud(features) 