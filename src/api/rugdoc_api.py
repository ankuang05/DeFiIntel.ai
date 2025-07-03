import requests

def check_token_rugdoc(token_address):
    # Simulated endpoint or scraper
    url = f"https://rugdoc.io/api/projects/{token_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"status": "unknown"}