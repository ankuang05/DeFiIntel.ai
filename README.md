# DeFiIntel.ai

**DeFiIntel.ai** is an open-source, modular analytics and intelligence platform for detecting fraud, scams, and suspicious activity in the cryptocurrency and DeFi space. It leverages on-chain data, social sentiment, and machine learning to help users, researchers, and developers analyze memecoins, wallets, and token launches across multiple blockchains.

## Features
- **Multi-Source Data Integration:**
  - Solana (Helius API) - Wallet transactions and behavior
  - Ethereum (Etherscan API) - Token transfers and patterns
  - GeckoTerminal (Solana token stats) - Price and market data
  - Twitter (social sentiment) - Social media analysis
  - (Planned) RugDoc and other scam label sources
- **Fraud Detection Engine:**
  - Wallet behavior analysis (rapid transactions, night activity, fee patterns)
  - Token transfer analysis (value concentration, address diversity, temporal patterns)
  - Social sentiment analysis (manipulation detection, volume analysis)
  - Heuristic-based detection (rule-based fraud indicators)
  - Machine learning models (Random Forest, Isolation Forest)
- **Feature Engineering:**
  - Automated feature extraction from transaction data
  - Risk scoring algorithms
  - Behavioral pattern recognition
- **Modular Architecture:**
  - Reusable API wrappers
  - Extensible detection methods
  - Ready for dashboard and AI agent integration
- **Interactive Dashboard:**
  - Streamlit web interface for real-time analysis
  - Interactive visualizations with Plotly
  - Multi-page navigation (wallet, token, sentiment, ML)
  - Risk scoring and pattern detection visualization

## Project Structure
```
defiintel-ai/
├── src/
│   ├── api/           # API wrappers (helius, etherscan, coingecko, etc.)
│   ├── features/       # Feature engineering scripts
│   ├── models/         # ML models and heuristics
│   ├── agent/          # AI agent (planned for future release)
│   └── utils/          # Config and helpers
├── app/                # Streamlit/FastAPI frontend
├── data/               # Datasets (not tracked by git)
├── notebooks/          # Jupyter notebooks for EDA and prototyping
├── test_api.py         # Script to test all API integrations
├── requirements.txt    # Python dependencies
├── .env                # API keys (not tracked by git)
├── .gitignore          # Files/folders to ignore
└── README.md           # Project documentation
```

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/ankuang05/DeFiIntel.ai.git
   cd DeFiIntel.ai
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up your `.env` file:**
   Create a `.env` file in the project root with the following content:
   ```env
   HELIUS_API_KEY=your_helius_api_key_here
   ETHERSCAN_API_KEY=your_etherscan_api_key_here
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
   ```
   - Get your API keys from [Helius](https://www.helius.xyz), [Etherscan](https://etherscan.io/myapikey), and [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard).

## Usage
- Test all API integrations:
  ```sh
  python test_api.py
  ```
- Run the interactive dashboard:
  ```sh
  pip install -r app/requirements.txt
  python app/run_dashboard.py
  ```
- Explore and analyze data in Jupyter notebooks (see `notebooks/`)
- Test fraud detection pipeline:
  ```sh
  python test_fraud_detection.py
  ```
- Extend with new APIs, features, or models as needed

## Roadmap
- [x] Phase 1: Project setup & API integration
- [x] Phase 2: Exploratory Data Analysis (EDA) & feature engineering
- [x] Phase 3: Scam/fraud detection logic (heuristics & ML)
- [x] Phase 4: Streamlit/FastAPI dashboard
- [ ] Phase 5: LLM-powered chatbot/agent (planned for future release)
- [ ] Phase 6: Documentation, deployment, and demo

## Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## AI Agent Status
The LLM-powered DeFi intelligence agent is planned for a future release. Public LLM APIs require payment for production use, making it infeasible for an open-source project to provide free access to all users. The current focus is on the powerful fraud detection features that are already working and ready for public use.

