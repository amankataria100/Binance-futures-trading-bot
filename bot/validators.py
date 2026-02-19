def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M symbols supported (e.g., BTCUSDT).")

def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_MARKET.")

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

def validate_price(price, order_type):
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price must be provided for LIMIT orders.")

def validate_stop_price(stop_price, order_type):
    if order_type == "STOP_MARKET" and (stop_price is None or stop_price <= 0):
        raise ValueError("Stop price required for STOP_MARKET orders.")
