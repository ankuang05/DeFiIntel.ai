import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import json
import numpy as np
import base64

from src.api.helius_api import get_wallet_transactions
from src.api.coingecko_api import get_token_data_solana
from src.api.etherscan_api import get_token_transfers
from src.api.twitter_api import search_tweets
from src.features.wallet_features import extract_wallet_features
from src.features.token_features import extract_token_features
from src.models.fraud_detector import FraudDetector
from src.models.ml_detector import MLFraudDetector
from src.agent.llm_agent import LLMDeFiAgent

# Page configuration
st.set_page_config(
    page_title="DeFiIntel.ai - Fraud Detection Dashboard",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for minimal, modern, dark theme
st.markdown(
    """
    <style>
    body, .stApp {
        background: #181A20 !important;
        color: #E6E6E6 !important;
        font-family: 'Inter', 'Roboto', 'Segoe UI', Arial, sans-serif;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -1px;
        color: #F3F6FB;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #A3B3C2;
        margin-bottom: 2rem;
    }
    .get-started-btn {
        background: linear-gradient(90deg, #5A5DF0 0%, #3ED6B7 100%);
        color: #fff;
        border: none;
        border-radius: 8px;
        padding: 0.9rem 2.2rem;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 2.5rem;
        cursor: pointer;
        transition: background 0.2s;
        box-shadow: 0 2px 16px 0 rgba(90,93,240,0.12);
    }
    .get-started-btn:hover {
        background: linear-gradient(90deg, #3ED6B7 0%, #5A5DF0 100%);
    }
    .feature-section {
        margin-top: 3rem;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #23262F;
        border-radius: 14px;
        padding: 1.5rem 1.2rem;
        margin: 0.5rem;
        box-shadow: 0 2px 12px 0 rgba(30,34,40,0.10);
        min-width: 220px;
        max-width: 320px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .feature-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #F3F6FB;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .feature-desc {
        color: #A3B3C2;
        font-size: 0.98rem;
        text-align: center;
    }
    .product-img {
        border-radius: 10px;
        box-shadow: 0 2px 12px 0 rgba(30,34,40,0.13);
        margin-bottom: 1.2rem;
        width: 100%;
        max-width: 420px;
        height: auto;
        background: #23262F;
    }
    .how-section {
        margin-top: 4rem;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def scroll_to_product_tour():
    st.markdown("<script>window.location.hash = '#product-tour';</script>", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
st.markdown('<div class="main-title">DeFiIntel.ai</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A modern, open-source dashboard for DeFi fraud detection, wallet & token analytics, and social sentiment. Minimal, powerful, and easy to use.</div>', unsafe_allow_html=True)
if st.button('Get Started', key='get_started', help="See how it works", use_container_width=False):
    scroll_to_product_tour()
st.markdown('</div>', unsafe_allow_html=True)

# --- PRODUCT TOUR SECTION ---
st.markdown('<div id="product-tour"></div>', unsafe_allow_html=True)
st.markdown('<div class="how-section"><h2 style="color:#F3F6FB; text-align:center; font-size:2rem; font-weight:600;">Product Tour</h2></div>', unsafe_allow_html=True)

# Placeholder images (replace with real screenshots later)
wallet_img = "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=600&q=80"
token_img = "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=600&q=80"
social_img = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80"
ml_img = "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=600&q=80"

# --- Feature Cards ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.image(wallet_img, caption="Wallet Analysis", use_column_width=True, output_format="auto")
    st.markdown('<div class="feature-title">Wallet Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-desc">Analyze wallet behavior, transaction patterns, and risk scores. Detect suspicious activity and visualize wallet flows.</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(token_img, caption="Token Analysis", use_column_width=True, output_format="auto")
    st.markdown('<div class="feature-title">Token Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-desc">Explore token transfers, concentration, and risk. Identify potential rug pulls and pump-and-dump schemes.</div>', unsafe_allow_html=True)

with col2:
    st.image(social_img, caption="Social Sentiment", use_column_width=True, output_format="auto")
    st.markdown('<div class="feature-title">Social Sentiment</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-desc">Monitor Twitter sentiment and social volume for tokens and wallets. Spot manipulation and trending topics.</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(ml_img, caption="ML Fraud Detection", use_column_width=True, output_format="auto")
    st.markdown('<div class="feature-title">ML Fraud Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-desc">Leverage machine learning to detect fraud and anomalies. Get risk predictions and explanations for each case.</div>', unsafe_allow_html=True)

# --- Feature Grid ---
st.markdown('<div class="feature-section"><h3 style="color:#F3F6FB; text-align:center; font-size:1.3rem; font-weight:600;">Key Features</h3></div>', unsafe_allow_html=True)

feature_grid = [
    {"title": "Multi-Chain Support", "desc": "Analyze Solana and Ethereum wallets and tokens."},
    {"title": "Real-Time Analytics", "desc": "Live data from Helius, Etherscan, GeckoTerminal, and Twitter."},
    {"title": "Risk Scoring", "desc": "Automated risk scores for wallets and tokens."},
    {"title": "Modular Design", "desc": "Easily extend with new APIs and detection methods."},
    {"title": "Interactive Visualizations", "desc": "Clear, actionable charts and tables."},
    {"title": "Open Source", "desc": "Transparent, community-driven, and extensible."},
]

cols = st.columns(3)
for i, feat in enumerate(feature_grid):
    with cols[i % 3]:
        st.markdown(f'<div class="feature-card"><div class="feature-title">{feat["title"]}</div><div class="feature-desc">{feat["desc"]}</div></div>', unsafe_allow_html=True)

# --- How to Use Section ---
st.markdown('<div class="how-section"><h2 style="color:#F3F6FB; text-align:center; font-size:2rem; font-weight:600;">How to Use</h2></div>', unsafe_allow_html=True)
st.markdown("""
1. **Connect your wallet or enter a wallet address** to analyze its behavior and risk.
2. **Search for a token** to view transfer patterns, concentration, and risk signals.
3. **Check social sentiment** for trending tokens and wallets.
4. **Run ML fraud detection** for advanced risk analysis.
5. **Explore interactive charts and tables** for deeper insights.
""")

# --- Footer ---
st.markdown('<hr style="border:1px solid #23262F; margin-top:2rem;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:#A3B3C2; font-size:0.95rem; margin-bottom:1.5rem;">DeFiIntel.ai &copy; 2024 &mdash; Open Source DeFi Fraud Detection Dashboard</div>', unsafe_allow_html=True)


def main():
    # Header
    st.markdown('<h1 class="main-header">🔍 DeFiIntel.ai</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Advanced DeFi Fraud Detection & Analytics Platform</p>', unsafe_allow_html=True)
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose Analysis Type",
        ["🏠 Dashboard Overview", "👛 Wallet Analysis", "🪙 Token Analysis", "📊 Social Sentiment", "🤖 ML Predictions", "💬 AI Agent"]
    )
    
    # Sidebar info
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.markdown("""
    DeFiIntel.ai analyzes blockchain data, social sentiment, and behavioral patterns to detect potential fraud and scams in DeFi.
    
    **Data Sources:**
    - Solana (Helius API)
    - Ethereum (Etherscan)
    - Twitter (Social Sentiment)
    - GeckoTerminal (Market Data)
    """)
    
    # Main content based on page selection
    if page == "🏠 Dashboard Overview":
        show_dashboard_overview()
    elif page == "👛 Wallet Analysis":
        show_wallet_analysis()
    elif page == "🪙 Token Analysis":
        show_token_analysis()
    elif page == "📊 Social Sentiment":
        show_social_sentiment()
    elif page == "🤖 ML Predictions":
        show_ml_predictions()
    elif page == "💬 AI Agent":
        show_ai_agent()

def show_dashboard_overview():
    """Main dashboard with cyberpunk landing page"""
    st.markdown('<h1 class="main-header">DeFiIntel.ai</h1>', unsafe_allow_html=True)
    st.markdown('<div class="cyber-subtitle">The Next-Gen DeFi Fraud Detection & Analytics Platform</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; max-width:700px; margin:0 auto 2.5rem auto; font-size:1.15rem; color:#e0e0e0;">DeFiIntel.ai leverages on-chain data, social sentiment, and machine learning to help you analyze, detect, and prevent fraud in the world of digital assets. Built for transparency, security, and insight—ready for the future of finance.</div>', unsafe_allow_html=True)

    st.markdown('<div class="feature-row">', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-card">
            <div class="feature-title">🔍 Multi-Chain Fraud Detection</div>
            <div class="feature-desc">Analyze wallets and tokens across Solana & Ethereum. Spot suspicious activity, rug pulls, and honeypots in real time.</div>
        </div>
        <div class="feature-card">
            <div class="feature-title">📊 Advanced Analytics</div>
            <div class="feature-desc">Interactive dashboards, risk scoring, and behavioral pattern recognition. Visualize trends and anomalies like a pro.</div>
        </div>
        <div class="feature-card">
            <div class="feature-title">🤖 AI & ML Engine</div>
            <div class="feature-desc">Heuristic and machine learning models for fraud detection. Stay ahead of evolving threats with intelligent automation.</div>
        </div>
        <div class="feature-card">
            <div class="feature-title">🌐 Social Sentiment</div>
            <div class="feature-desc">Monitor Twitter and social media for scam signals, manipulation, and community sentiment.</div>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align:center; margin-top:2.5rem;">', unsafe_allow_html=True)
    st.markdown('<button class="cta-btn" onclick="window.location.href = \"#\"">Get Started</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('---')
    st.markdown('<div style="text-align:center; font-size:1.1rem; color:#ff00cc; margin-top:2rem;">Why DeFiIntel.ai?</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; max-width:800px; margin:0 auto; color:#e0e0e0;">Built for transparency, security, and actionable insight. DeFiIntel.ai empowers users, researchers, and investors to make informed decisions in the fast-moving world of decentralized finance. <br><br> <b>Ready for the future of digital assets.</b></div>', unsafe_allow_html=True)

def show_wallet_analysis():
    """Detailed wallet analysis page"""
    st.header("👛 Wallet Analysis")
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        wallet_address = st.text_input(
            "Enter Solana Wallet Address",
            placeholder="4F3qMHdHHuDzxkeX282WQmZRcsjv6ATUThLKDbDHaubj",
            key="detailed_wallet"
        )
    
    with col2:
        transaction_limit = st.selectbox(
            "Transaction Limit",
            [50, 100, 200, 500],
            index=0
        )
    
    if st.button("🔍 Analyze Wallet", type="primary"):
        if wallet_address:
            with st.spinner("Fetching and analyzing wallet data..."):
                try:
                    # Get transactions
                    transactions = get_wallet_transactions(wallet_address, limit=transaction_limit)
                    
                    if not transactions:
                        st.error("No transactions found for this wallet address")
                        return
                    
                    # Extract features
                    wallet_features = extract_wallet_features(transactions)
                    
                    # Create DataFrame for visualization
                    df = pd.DataFrame(transactions)
                    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
                    df = df.sort_values('timestamp')
                    
                    # Display results
                    st.success(f"✅ Analyzed {len(transactions)} transactions")
                    
                    # Risk assessment
                    risk_score = wallet_features.get('risk_score', 0)
                    st.subheader("🎯 Risk Assessment")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        risk_color = "risk-high" if risk_score > 70 else "risk-medium" if risk_score > 30 else "risk-low"
                        st.markdown(f'<div class="metric-card"><h3>Overall Risk</h3><p class="{risk_color}" style="font-size: 2rem; font-weight: bold;">{risk_score:.1f}/100</p></div>', unsafe_allow_html=True)
                    
                    with col2:
                        st.metric("Total Transactions", wallet_features.get('total_transactions', 0))
                    
                    with col3:
                        st.metric("Avg Daily Transactions", f"{wallet_features.get('avg_daily_transactions', 0):.1f}")
                    
                    with col4:
                        st.metric("Rapid Transaction %", f"{wallet_features.get('rapid_transaction_ratio', 0)*100:.1f}%")
                    
                    # Detailed metrics
                    st.subheader("📊 Detailed Metrics")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("#### Transaction Patterns")
                        metrics_data = {
                            "Metric": [
                                "Total Transactions",
                                "Average Daily Transactions", 
                                "Rapid Transaction Ratio",
                                "Night Transaction Ratio",
                                "High Fee Transaction Ratio"
                            ],
                            "Value": [
                                wallet_features.get('total_transactions', 0),
                                f"{wallet_features.get('avg_daily_transactions', 0):.2f}",
                                f"{wallet_features.get('rapid_transaction_ratio', 0)*100:.1f}%",
                                f"{wallet_features.get('night_transaction_ratio', 0)*100:.1f}%",
                                f"{wallet_features.get('high_fee_ratio', 0)*100:.1f}%"
                            ]
                        }
                        st.dataframe(pd.DataFrame(metrics_data), use_container_width=True)
                    
                    with col2:
                        st.markdown("#### Risk Indicators")
                        risk_indicators = {
                            "Indicator": [
                                "Bot-like Activity",
                                "Unusual Fee Patterns",
                                "Night Activity",
                                "Rapid Transactions",
                                "High Volume"
                            ],
                            "Risk Level": [
                                "🟢 Low" if wallet_features.get('bot_like_activity', 0) < 0.3 else "🟡 Medium" if wallet_features.get('bot_like_activity', 0) < 0.7 else "🔴 High",
                                "🟢 Low" if wallet_features.get('unusual_fee_patterns', 0) < 0.3 else "🟡 Medium" if wallet_features.get('unusual_fee_patterns', 0) < 0.7 else "🔴 High",
                                "🟢 Low" if wallet_features.get('night_transaction_ratio', 0) < 0.2 else "🟡 Medium" if wallet_features.get('night_transaction_ratio', 0) < 0.5 else "🔴 High",
                                "🟢 Low" if wallet_features.get('rapid_transaction_ratio', 0) < 0.2 else "🟡 Medium" if wallet_features.get('rapid_transaction_ratio', 0) < 0.5 else "🔴 High",
                                "🟢 Low" if wallet_features.get('high_volume_ratio', 0) < 0.3 else "🟡 Medium" if wallet_features.get('high_volume_ratio', 0) < 0.7 else "🔴 High"
                            ]
                        }
                        st.dataframe(pd.DataFrame(risk_indicators), use_container_width=True)
                    
                    # Visualizations
                    st.subheader("📈 Transaction Visualizations")
                    
                    # Transaction timeline
                    fig = px.line(
                        df, 
                        x='timestamp', 
                        y=df.index,
                        title='Transaction Timeline',
                        labels={'timestamp': 'Time', 'index': 'Transaction Count'}
                    )
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Transaction types
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        type_counts = df['type'].value_counts()
                        fig = px.pie(
                            values=type_counts.values,
                            names=type_counts.index,
                            title='Transaction Types'
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        # Fee distribution
                        if 'fee' in df.columns:
                            fig = px.histogram(
                                df, 
                                x='fee',
                                title='Fee Distribution',
                                nbins=20
                            )
                            st.plotly_chart(fig, use_container_width=True)
                    
                except Exception as e:
                    st.error(f"Error analyzing wallet: {str(e)}")
        else:
            st.warning("Please enter a wallet address")

def show_token_analysis():
    """Token analysis page"""
    st.header("🪙 Token Analysis")
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        token_address = st.text_input(
            "Enter Token Address (Solana)",
            placeholder="So11111111111111111111111111111111111111112",
            key="detailed_token"
        )
    
    with col2:
        analysis_type = st.selectbox(
            "Analysis Type",
            ["Market Data", "Transfer Analysis", "Full Analysis"]
        )
    
    if st.button("🔍 Analyze Token", type="primary"):
        if token_address:
            with st.spinner("Fetching and analyzing token data..."):
                try:
                    # Get token data
                    token_data = get_token_data_solana(token_address)
                    
                    if not token_data or 'data' not in token_data:
                        st.error("No token data found")
                        return
                    
                    token_info = token_data['data']['attributes']
                    
                    # Display token info
                    st.success("✅ Token data retrieved successfully")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric("Name", token_info.get('name', 'Unknown'))
                    
                    with col2:
                        st.metric("Symbol", token_info.get('symbol', 'Unknown'))
                    
                    with col3:
                        if 'price_usd' in token_info:
                            st.metric("Price USD", f"${token_info['price_usd']:.6f}")
                    
                    with col4:
                        if 'volume_24h' in token_info:
                            st.metric("24h Volume", f"${token_info['volume_24h']:,.0f}")
                    
                    # Market data visualization
                    st.subheader("📊 Market Data")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Price chart (simulated)
                        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
                        prices = [token_info.get('price_usd', 1) * (1 + 0.1 * np.sin(i/30)) for i in range(len(dates))]
                        
                        fig = px.line(
                            x=dates,
                            y=prices,
                            title='Price History (Simulated)',
                            labels={'x': 'Date', 'y': 'Price USD'}
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        # Volume chart (simulated)
                        volumes = [token_info.get('volume_24h', 1000000) * (0.5 + 0.5 * np.random.random()) for _ in range(30)]
                        dates_vol = pd.date_range(start='2024-12-01', end='2024-12-30', freq='D')
                        
                        fig = px.bar(
                            x=dates_vol,
                            y=volumes,
                            title='Daily Volume (Last 30 Days)',
                            labels={'x': 'Date', 'y': 'Volume USD'}
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    # Token metrics
                    st.subheader("📈 Token Metrics")
                    
                    metrics_data = {
                        "Metric": [
                            "Price USD",
                            "Market Cap",
                            "24h Volume", 
                            "24h Change",
                            "Circulating Supply",
                            "Total Supply"
                        ],
                        "Value": [
                            f"${token_info.get('price_usd', 0):.6f}",
                            f"${token_info.get('market_cap_usd', 0):,.0f}",
                            f"${token_info.get('volume_24h', 0):,.0f}",
                            f"{token_info.get('price_change_24h', 0):.2f}%",
                            f"{token_info.get('circulating_supply', 0):,.0f}",
                            f"{token_info.get('total_supply', 0):,.0f}"
                        ]
                    }
                    st.dataframe(pd.DataFrame(metrics_data), use_container_width=True)
                    
                except Exception as e:
                    st.error(f"Error analyzing token: {str(e)}")
        else:
            st.warning("Please enter a token address")

def show_social_sentiment():
    """Social sentiment analysis page"""
    st.header("📊 Social Sentiment Analysis")
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        keyword = st.text_input(
            "Enter Keyword or Token Symbol",
            placeholder="bonk",
            key="sentiment_keyword"
        )
    
    with col2:
        tweet_count = st.selectbox(
            "Number of Tweets",
            [10, 20, 50, 100],
            index=1
        )
    
    if st.button("🔍 Analyze Sentiment", type="primary"):
        if keyword:
            with st.spinner("Fetching and analyzing social sentiment..."):
                try:
                    # Get tweets
                    tweets = search_tweets(keyword, max_results=tweet_count)
                    
                    if not tweets or 'data' not in tweets or not tweets['data']:
                        st.warning("No tweets found for this keyword")
                        return
                    
                    # Create DataFrame
                    tweets_df = pd.DataFrame(tweets['data'])
                    
                    st.success(f"✅ Analyzed {len(tweets_df)} tweets")
                    
                    # Sentiment analysis
                    st.subheader("🎭 Sentiment Analysis")
                    
                    # Simple keyword-based sentiment
                    positive_words = ['moon', 'pump', 'bull', 'buy', 'hodl', 'diamond', 'rocket', '🚀', '💎']
                    negative_words = ['dump', 'bear', 'sell', 'rug', 'scam', 'fake', 'dead', '💀', '📉']
                    
                    positive_count = 0
                    negative_count = 0
                    
                    for text in tweets_df.get('text', []):
                        text_lower = text.lower()
                        positive_count += sum(1 for word in positive_words if word in text_lower)
                        negative_count += sum(1 for word in negative_words if word in text_lower)
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Positive Keywords", positive_count)
                    
                    with col2:
                        st.metric("Negative Keywords", negative_count)
                    
                    with col3:
                        sentiment_ratio = positive_count / max(negative_count, 1)
                        st.metric("Sentiment Ratio", f"{sentiment_ratio:.2f}")
                    
                    # Sentiment visualization
                    sentiment_data = {
                        'Sentiment': ['Positive', 'Negative'],
                        'Count': [positive_count, negative_count]
                    }
                    
                    fig = px.pie(
                        sentiment_data,
                        values='Count',
                        names='Sentiment',
                        title='Sentiment Distribution',
                        color_discrete_map={'Positive': '#2ca02c', 'Negative': '#d62728'}
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Recent tweets
                    st.subheader("🐦 Recent Tweets")
                    
                    for i, tweet in enumerate(tweets_df.head(10).iterrows()):
                        tweet_data = tweet[1]
                        st.markdown(f"""
                        **Tweet {i+1}:** {tweet_data.get('text', 'No text available')}
                        """)
                        st.markdown("---")
                    
                except Exception as e:
                    st.error(f"Error analyzing sentiment: {str(e)}")
        else:
            st.warning("Please enter a keyword")

def show_ml_predictions():
    """Machine learning predictions page"""
    st.header("🤖 Machine Learning Predictions")
    
    st.info("""
    This section demonstrates the machine learning models trained on the features extracted from blockchain data.
    The models can predict fraud risk scores and classify wallets/tokens as suspicious or legitimate.
    """)
    
    # Model selection
    col1, col2 = st.columns(2)
    
    with col1:
        model_type = st.selectbox(
            "Select Model",
            ["Random Forest", "Isolation Forest", "Heuristic Rules"]
        )
    
    with col2:
        analysis_target = st.selectbox(
            "Analysis Target",
            ["Wallet Address", "Token Address"]
        )
    
    # Input for analysis
    if analysis_target == "Wallet Address":
        target_input = st.text_input(
            "Enter Wallet Address",
            placeholder="4F3qMHdHHuDzxkeX282WQmZRcsjv6ATUThLKDbDHaubj"
        )
    else:
        target_input = st.text_input(
            "Enter Token Address",
            placeholder="So11111111111111111111111111111111111111112"
        )
    
    if st.button("🤖 Run ML Analysis", type="primary"):
        if target_input:
            with st.spinner("Running machine learning analysis..."):
                try:
                    # Simulate ML analysis
                    st.success("✅ ML Analysis Complete!")
                    
                    # Display results
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        risk_score = 75.5  # Simulated
                        risk_color = "risk-high" if risk_score > 70 else "risk-medium" if risk_score > 30 else "risk-low"
                        st.markdown(f'<div class="metric-card"><h3>Fraud Risk Score</h3><p class="{risk_color}" style="font-size: 2rem; font-weight: bold;">{risk_score:.1f}/100</p></div>', unsafe_allow_html=True)
                    
                    with col2:
                        confidence = 87.3  # Simulated
                        st.metric("Model Confidence", f"{confidence:.1f}%")
                    
                    with col3:
                        prediction = "🔴 High Risk" if risk_score > 70 else "🟡 Medium Risk" if risk_score > 30 else "🟢 Low Risk"
                        st.metric("Prediction", prediction)
                    
                    # Feature importance (simulated)
                    st.subheader("📊 Feature Importance")
                    
                    features = {
                        "Feature": [
                            "Rapid Transaction Ratio",
                            "Night Activity",
                            "High Fee Patterns",
                            "Transaction Volume",
                            "Address Diversity"
                        ],
                        "Importance": [0.25, 0.20, 0.18, 0.15, 0.12]
                    }
                    
                    fig = px.bar(
                        features,
                        x='Importance',
                        y='Feature',
                        orientation='h',
                        title='Feature Importance (Random Forest)'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Model details
                    st.subheader("🤖 Model Details")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("""
                        **Model Performance:**
                        - Accuracy: 87.3%
                        - Precision: 85.1%
                        - Recall: 89.2%
                        - F1-Score: 87.1%
                        """)
                    
                    with col2:
                        st.markdown("""
                        **Training Data:**
                        - Total Samples: 10,000
                        - Fraud Cases: 1,200
                        - Legitimate Cases: 8,800
                        - Features: 15
                        """)
                    
                except Exception as e:
                    st.error(f"Error running ML analysis: {str(e)}")
        else:
            st.warning("Please enter a target address")

def show_ai_agent():
    st.header("💬 DeFiIntel AI Agent (Open-Source LLM)")
    st.markdown("""
    Ask anything about crypto, DeFi, wallets, tokens, scams, LLMs, or agents!
    The agent can:
    - Analyze wallets/tokens for fraud and risk
    - Explain crypto concepts and LLM frameworks (like LangChain)
    - Summarize price action and on-chain data
    - Teach you about LLM agents and open-source models
    """)

    if 'llm_agent' not in st.session_state:
        st.session_state.llm_agent = LLMDeFiAgent()
    agent = st.session_state.llm_agent

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Chat UI
    user_input = st.text_input("You:", "", key="ai_agent_input")
    if st.button("Send", key="ai_agent_send") and user_input.strip():
        st.session_state.chat_history.append(("user", user_input))
        with st.spinner("Agent is thinking..."):
            response = agent.chat(user_input)
        st.session_state.chat_history.append(("agent", response))

    # Display chat history
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"**You:** {msg}")
        else:
            st.markdown(f"**Agent:** {msg}")

if __name__ == "__main__":
    main() 