# DeFiIntel.ai Dashboard

A modern, interactive web dashboard for DeFi fraud detection and analytics.

## Features

- **👛 Wallet Analysis**: Deep analysis of Solana wallet behavior and transaction patterns
- **🪙 Token Analysis**: Market data and transfer analysis for tokens
- **📊 Social Sentiment**: Twitter sentiment analysis for keywords and tokens
- **🤖 ML Predictions**: Machine learning-based fraud risk scoring
- **📈 Interactive Visualizations**: Real-time charts and graphs using Plotly
- **🎯 Risk Assessment**: Comprehensive risk scoring and suspicious pattern detection

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

### 🏠 Dashboard Overview
- Quick analysis tools for wallets and tokens
- System status and API connectivity
- Recent activity summary

### 👛 Wallet Analysis
- **Input**: Solana wallet address
- **Features**:
  - Transaction timeline visualization
  - Risk score calculation
  - Behavioral pattern analysis
  - Fee distribution analysis
  - Bot detection indicators

### 🪙 Token Analysis
- **Input**: Solana token address
- **Features**:
  - Market data display
  - Price and volume charts
  - Token metrics and statistics
  - Transfer pattern analysis

### 📊 Social Sentiment
- **Input**: Keyword or token symbol
- **Features**:
  - Twitter sentiment analysis
  - Positive/negative keyword detection
  - Sentiment visualization
  - Recent tweets display

### 🤖 ML Predictions
- **Input**: Wallet or token address
- **Features**:
  - Machine learning model predictions
  - Fraud risk scoring
  - Feature importance analysis
  - Model confidence metrics

## Usage Examples

### Analyzing a Wallet
1. Navigate to "👛 Wallet Analysis"
2. Enter a Solana wallet address: `4F3qMHdHHuDzxkeX282WQmZRcsjv6ATUThLKDbDHaubj`
3. Click "🔍 Analyze Wallet"
4. Review the risk score, transaction patterns, and visualizations

### Analyzing a Token
1. Navigate to "🪙 Token Analysis"
2. Enter a Solana token address: `So11111111111111111111111111111111111111112`
3. Click "🔍 Analyze Token"
4. View market data, price charts, and token metrics

### Social Sentiment Analysis
1. Navigate to "📊 Social Sentiment"
2. Enter a keyword: `bonk`
3. Click "🔍 Analyze Sentiment"
4. Review sentiment distribution and recent tweets

## Technical Details

### Architecture
- **Frontend**: Streamlit web framework
- **Visualizations**: Plotly interactive charts
- **Data Processing**: Pandas and NumPy
- **ML Models**: Scikit-learn integration
- **APIs**: Custom wrappers for blockchain and social data

### Data Sources
- **Solana**: Helius API for wallet transactions
- **Ethereum**: Etherscan API for token transfers
- **Market Data**: GeckoTerminal API for token prices
- **Social**: Twitter API for sentiment analysis

### Risk Indicators
- Rapid transaction patterns
- Unusual fee distributions
- Night-time activity
- High-volume transactions
- Bot-like behavior patterns

## Troubleshooting

### Common Issues

1. **API Connection Errors**
   - Check your `.env` file has correct API keys
   - Verify API key permissions and rate limits

2. **No Data Found**
   - Ensure wallet/token addresses are correct
   - Check if the address has recent activity

3. **Dashboard Won't Start**
   - Install requirements: `pip install -r app/requirements.txt`
   - Check Python version (3.8+ required)

### Performance Tips
- Use smaller transaction limits for faster analysis
- The dashboard caches results for better performance
- Large datasets may take longer to process

## Contributing

To add new features to the dashboard:
1. Modify `streamlit_app.py` to add new pages or functionality
2. Update `requirements.txt` if new dependencies are needed
3. Test with different wallet/token addresses
4. Update this README with new features

## Next Steps

Future enhancements planned:
- Real-time data updates
- Advanced ML model integration
- Multi-chain support (Ethereum, Polygon, etc.)
- Alert system for suspicious activity
- Export functionality for reports 