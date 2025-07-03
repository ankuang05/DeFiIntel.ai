import requests
from src.utils.config import CONFIG

API_KEY = CONFIG['ETHERSCAN_API_KEY']
BASE_URL = "https://api.etherscan.io/api"

def get_token_info(token_address):
    url = f"{BASE_URL}?module=token&action=tokeninfo&contractaddress={token_address}&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()