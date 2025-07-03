import requests
from src.utils.config import CONFIG

BEARER_TOKEN = CONFIG["TWITTER_BEARER_TOKEN"]

def search_tweets(keyword, max_results=10):
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    query = f"https://api.twitter.com/2/tweets/search/recent?query={keyword}&max_results={max_results}"
    response = requests.get(query, headers=headers)
    return response.json()