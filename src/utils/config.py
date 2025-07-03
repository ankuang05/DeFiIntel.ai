import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "HELIUS_API_KEY": os.getenv("HELIUS_API_KEY"),
    "ETHERSCAN_API_KEY": os.getenv("ETHERSCAN_API_KEY"),
    "TWITTER_BEARER_TOKEN": os.getenv("TWITTER_BEARER_TOKEN"),
}