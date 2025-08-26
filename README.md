# DeFiIntel.ai

**DeFiIntel.ai** is an open-source, modular analytics and intelligence platform for detecting fraud, scams, and suspicious activity in the cryptocurrency and DeFi space. It leverages on-chain data, social sentiment, and machine learning to help users, researchers, and developers analyze memecoins, wallets, and token launches across multiple blockchains.

## 🚀 Features

- **🔍 Multi-Chain Analysis**: Support for Solana and Ethereum with extensible architecture
- **📊 Real-Time Analytics**: Live data from Helius, Etherscan, GeckoTerminal, and Twitter APIs
- **🤖 Machine Learning**: Advanced fraud detection using Random Forest and Isolation Forest models
- **📈 Interactive Dashboard**: Modern Streamlit interface with real-time visualizations
- **🎯 Risk Scoring**: Comprehensive risk assessment with multiple indicators
- **🔧 Modular Design**: Easy to extend with new blockchains and data sources

## 🏗️ Architecture

```
defiintel-ai/
├── app/                 # Streamlit dashboard application
├── frontend/            # Next.js marketing website
├── src/
│   ├── api/            # API integrations (Helius, Etherscan, etc.)
│   ├── features/       # Feature engineering modules
│   ├── models/         # Machine learning models
│   └── utils/          # Configuration and utilities
├── data/               # Data storage and caching
├── notebooks/          # Jupyter notebooks for analysis
└── tests/              # Test suites and validation
```

## 🛠️ Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- API keys for Helius, Etherscan, and Twitter

### Installation

```bash
# Clone the repository
git clone https://github.com/ankuang05/DeFiIntel.ai.git
cd DeFiIntel.ai

# Install Python dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd frontend
npm install
cd ..

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Running the Dashboard

```bash
# Start the Streamlit dashboard
streamlit run app/streamlit_app.py

# Or use the launcher script
python app/run_dashboard.py
```

### Running the Frontend

```bash
# Start the Next.js frontend
cd frontend
npm run dev
```

## 📊 Dashboard Features

### Wallet Analysis
- Transaction pattern analysis
- Risk scoring and visualization
- Behavioral anomaly detection
- Fee distribution analysis

### Token Analysis
- Market data integration
- Transfer pattern analysis
- Price and volume charts
- Token metrics dashboard

### Social Sentiment
- Twitter sentiment analysis
- Keyword monitoring
- Sentiment visualization
- Real-time social data

### Machine Learning Predictions
- Fraud risk scoring
- Multiple model types (Random Forest, Isolation Forest)
- Feature importance analysis
- Confidence metrics

## 🔧 Development Roadmap

- [x] Phase 1: Core API integrations (Helius, Etherscan, Twitter)
- [x] Phase 2: Feature engineering and data processing
- [x] Phase 3: Machine learning models and risk scoring
- [x] Phase 4: Interactive dashboard and visualizations
- [x] Phase 5: Advanced analytics and reporting features

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines for details on:
- Code style and standards
- Testing requirements
- Pull request process
- Issue reporting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Helius for Solana blockchain data
- Etherscan for Ethereum blockchain data
- GeckoTerminal for market data
- Twitter for social sentiment data

## 📞 Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/ankuang05/DeFiIntel.ai/issues)
- **Discussions**: [Join community discussions](https://github.com/ankuang05/DeFiIntel.ai/discussions)
- **Project**: [View project on GitHub](https://github.com/ankuang05/DeFiIntel.ai)

## ⭐ Star History

If you find this project helpful, please consider giving it a star! ⭐

---

**Built with ❤️ by the DeFiIntel.ai community**

