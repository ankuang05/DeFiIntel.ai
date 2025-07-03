import requests

def get_token_data_solana(token_address):
    url = f"https://api.geckoterminal.com/api/v2/networks/solana/tokens/{token_address}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"GeckoTerminal error: {response.status_code} - {response.text}")
    return response.json()