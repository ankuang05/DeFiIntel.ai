import requests
from src.utils.config import CONFIG

API_KEY = CONFIG['ETHERSCAN_API_KEY']
BASE_URL = "https://api.etherscan.io/api"

def get_token_transfers(token_address, address=None, startblock=0, endblock=99999999, sort="asc"):
    # Fetch ERC20 token transfer events for a contract (token_address)
    url = f"{BASE_URL}?module=account&action=tokentx&contractaddress={token_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={API_KEY}"
    if address:
        url += f"&address={address}"
    response = requests.get(url)
    return response.json()