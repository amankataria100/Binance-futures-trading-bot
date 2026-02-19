import os
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API credentials missing in .env file")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Initialized Binance Futures Testnet client")

    def place_order(self, **kwargs):
        try:
            logger.info(f"Order request: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(str(e))
            raise
