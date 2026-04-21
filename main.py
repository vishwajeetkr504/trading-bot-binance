import argparse
from client import get_client
from logger import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        logger.info(f"Placing order: {symbol} {side} {order_type} {quantity}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        print("\n Order Placed Successfully!")
        print(order)

        logger.info(f"Order Response: {order}")

    except Exception as e:
        print("\n Error:", str(e))
        logger.error(str(e))


def main():
    parser = argparse.ArgumentParser(description="Trading Bot")

    parser.add_argument("--symbol", required=True, help="BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    if args.type == "LIMIT" and not args.price:
        print(" LIMIT order requires --price")
        return

    place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )


if __name__ == "__main__":
    main()