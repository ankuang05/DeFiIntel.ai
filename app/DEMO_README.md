# DeFiIntel.ai Dashboard Demo

Welcome to the DeFiIntel.ai fraud detection dashboard demo! This guide will help you quickly set up and run the dashboard for demonstration purposes.

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```bash
cd app
python run_demo.py
```

This script will:
- ✅ Check and install required dependencies
- 🔧 Set up environment variables
- 🚀 Launch the dashboard automatically

### Option 2: Manual Setup
```bash
cd app
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 📊 What You'll See

The dashboard includes several key features:

### 1. **Wallet Analysis**
- Analyze wallet transaction patterns
- Detect suspicious behavior
- Risk scoring and categorization

### 2. **Token Analysis** 
- Token transfer analysis
- Value concentration metrics
- Fraud detection indicators

### 3. **Social Sentiment**
- Twitter sentiment analysis
- Community sentiment tracking
- Social risk indicators

### 4. **ML Predictions**
- Machine learning fraud detection
- Anomaly detection
- Confidence scoring

## 🎯 Demo Data

For demonstration purposes, you can use these sample addresses:

### Solana Wallets:
- `4F3qMHdHHuDzxkeX282WQmZRcsjv6ATUThLKDbDHaubj` (Active wallet)
- `So11111111111111111111111111111111111111112` (SOL token)

### Ethereum Tokens:
- `0xdAC17F958D2ee523a2206206994597C13D831ec7` (USDT)
- `0xA0b86a33E6441b8C4C8C8C8C8C8C8C8C8C8C8C8C` (Sample token)

## 🔧 Configuration

### API Keys (Optional for Demo)
The demo will work with placeholder API keys, but for full functionality, you can add real API keys to the `.env` file:

```env
HELIUS_API_KEY=your_helius_key
ETHERSCAN_API_KEY=your_etherscan_key
TWITTER_BEARER_TOKEN=your_twitter_token
COINGECKO_API_KEY=your_coingecko_key
```

### Available APIs:
- **Helius**: Solana blockchain data
- **Etherscan**: Ethereum blockchain data  
- **Twitter**: Social sentiment analysis
- **CoinGecko**: Token price and market data

## 🎨 Features Demonstrated

### Modern UI/UX
- Clean, minimalistic design
- Responsive layout
- Smooth animations
- Professional styling

### Real-time Analytics
- Live data fetching
- Interactive charts
- Dynamic risk scoring
- Real-time updates

### Fraud Detection
- Multi-factor risk analysis
- Behavioral pattern detection
- Anomaly identification
- Confidence scoring

## 🛠️ Troubleshooting

### Common Issues:

1. **Port already in use**
   ```bash
   streamlit run streamlit_app.py --server.port 8502
   ```

2. **Missing dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Import errors**
   ```bash
   # Make sure you're in the app directory
   cd app
   python run_demo.py
   ```

### Getting Help:
- Check the console output for error messages
- Ensure all dependencies are installed
- Verify you're running from the correct directory

## 📈 Demo Flow

1. **Start the dashboard** - Run the demo script
2. **Explore the interface** - Navigate through different sections
3. **Try wallet analysis** - Enter a wallet address
4. **Test token analysis** - Analyze a token contract
5. **Check social sentiment** - View Twitter sentiment data
6. **Review ML predictions** - See fraud detection results

## 🎉 Next Steps

After the demo:
- Explore the codebase in `src/` directory
- Check out the frontend in `frontend/` directory
- Review the API integrations
- Consider adding real API keys for full functionality

---

**Happy demoing! 🚀**

For questions or support, check the main project README or open an issue on GitHub. 