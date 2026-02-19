import click
import logging
from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import *
from bot.logging_config import setup_logging

@click.command()
@click.option('--symbol', prompt=True, help='Trading symbol (e.g., BTCUSDT)')
@click.option('--side', prompt=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False))
@click.option('--order_type', prompt=True, type=click.Choice(['MARKET', 'LIMIT', 'STOP_MARKET'], case_sensitive=False))
@click.option('--quantity', prompt=True, type=float)
@click.option('--price', type=float, default=None, help='Required for LIMIT orders')
@click.option('--stop_price', type=float, default=None, help='Required for STOP_MARKET orders')

def main(symbol, side, order_type, quantity, price, stop_price):
    setup_logging()
    logger = logging.getLogger("CLI")

    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)
        validate_stop_price(stop_price, order_type)

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")
        if stop_price:
            print(f"Stop Price: {stop_price}")

        client = BinanceFuturesClient()
        service = OrderService(client)

        response = service.create_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")
        print("\nOrder placed successfully!")

    except Exception as e:
        logger.error(str(e))
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
