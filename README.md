# DeFiIntel.ai

**DeFiIntel.ai** is an open-source, modular analytics and intelligence platform for detecting fraud, scams, and suspicious activity in the cryptocurrency and DeFi space. It leverages on-chain data, social sentiment, and machine learning to help users, researchers, and developers analyze memecoins, wallets, and token launches across multiple blockchains.

## Features
- Fetches and aggregates data from:
  - Solana (Helius API)
  - Ethereum (Etherscan API)
  - GeckoTerminal (Solana token stats)
  - Twitter (social sentiment)
  - (Planned) RugDoc and other scam label sources
- Modular API wrappers for easy extension
- Ready for EDA, feature engineering, and ML modeling
- Designed for integration with LLMs and chatbot agents
- (Planned) Streamlit/FastAPI dashboard for interactive analysis

## Project Structure
```
defiintel-ai/
├── src/
│   ├── api/           # API wrappers (helius, etherscan, coingecko, etc.)
│   ├── features/       # Feature engineering scripts
│   ├── models/         # ML models and heuristics
│   └── utils/          # Config and helpers
├── app/                # (Planned) Streamlit/FastAPI frontend
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
- Explore and analyze data in Jupyter notebooks (see `notebooks/`)
- Extend with new APIs, features, or models as needed

## Roadmap
- [x] Phase 1: Project setup & API integration
- [ ] Phase 2: Exploratory Data Analysis (EDA) & feature engineering
- [ ] Phase 3: Scam/fraud detection logic (heuristics & ML)
- [ ] Phase 4: Streamlit/FastAPI dashboard
- [ ] Phase 5: LLM-powered chatbot/agent
- [ ] Phase 6: Documentation, deployment, and demo

## Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

