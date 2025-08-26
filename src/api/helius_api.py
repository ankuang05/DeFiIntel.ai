import requests
from src.utils.config import CONFIG

API_KEY = CONFIG['HELIUS_API_KEY']
BASE_URL = "https://api.helius.xyz/v0"

def get_wallet_transactions(wallet_address, limit=10):
    url = f"{BASE_URL}/addresses/{wallet_address}/transactions?api-key={API_KEY}&limit={limit}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Helius API error: {response.status_code} - {response.text}")
    return response.json()