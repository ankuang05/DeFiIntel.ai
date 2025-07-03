from src.api.helius_api import get_wallet_transactions
from src.api.coingecko_api import get_token_data_solana
from src.api.etherscan_api import get_token_info
from src.api.rugdoc_api import check_token_rugdoc
from src.api.twitter_api import search_tweets

wallet = "YOUR_SOLANA_WALLET"
token_solana = "So11111111111111111111111111111111111111112"
token_eth = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # USDT

print(" Helius:")
print(get_wallet_transactions(wallet)[:1])

print("\n GeckoTerminal:")
print(get_token_data_solana(token_solana))

print("\n Etherscan:")
print(get_token_info(token_eth))

print("\n RugDoc:")
print(check_token_rugdoc(token_eth))

print("\n Twitter (keyword = 'bonk'):")
print(search_tweets("bonk"))
