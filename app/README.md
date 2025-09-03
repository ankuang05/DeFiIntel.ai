# DeFiIntel.ai Dashboard

A modern, interactive web dashboard for DeFi fraud detection and analytics.

## Features

- **Wallet Analysis**: Deep analysis of Solana wallet behavior and transaction patterns
- **Token Analysis**: Market data and transfer analysis for tokens
- **Social Sentiment**: Twitter sentiment analysis for keywords and tokens
- **ML Predictions**: ML based fraud risk scoring
- **Interactive Visualizations**: Charts and graphs using Plotly
- **Risk Assessment**: Comprehensive risk scoring and suspicious pattern detection

## Quick Start

### 1. Install Dependencies
```bash
pip install -r app/requirements.txt
```

### 2. Set Up Environment Variables
Make sure your `.env` file in the project root contains:
```env
HELIUS_API_KEY=your_helius_api_key_here
ETHERSCAN_API_KEY=your_etherscan_api_key_here
TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
```

### 3. Run the Dashboard
```bash
# Option 1: Using the launcher script
python app/run_dashboard.py

# Option 2: Direct streamlit command
streamlit run app/streamlit_app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

## Dashboard Sections

### Dashboard Overview
- Quick analysis tools for wallets and tokens
- System status and API connectivity
- Recent activity summary

### Wallet Analysis
  - Transaction timeline visualization
  - Risk score calculation
  - Behavioral pattern analysis
  - Fee distribution analysis
  - Bot detection indicators

### Token Analysis
  - Market data display
  - Price and volume charts
  - Token metrics and statistics
  - Transfer pattern analysis

### Social Sentiment
  - Twitter sentiment analysis
  - Positive/negative keyword detection
  - Sentiment visualization
  - Recent tweets display

### ML Predictions
  - Machine learning model predictions
  - Fraud risk scoring
  - Feature importance analysis
  - Model confidence metrics

Future enhancements planned:
- Real-time data updates
- Advanced ML model integration
- Alert system for suspicious activity
- Export functionality for reports 