import logging
from binance.enums import TIME_IN_FORCE_GTC

logger = logging.getLogger(__name__)

class OrderService:

    def __init__(self, client):
        self.client = client

    def create_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = TIME_IN_FORCE_GTC

        if order_type == "STOP_MARKET":
            params["stopPrice"] = stop_price

        return self.client.place_order(**params)
