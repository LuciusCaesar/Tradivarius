import csv
import yfinance as yf


class MarketDataProvider:
    def get_price(self, product: str) -> float:
        """
        Get the price of a product.

        Args:
            product (str): The name of the product.

        Returns:
            float: The price of the product.
        """
        pass


class DevMarketDataProvider(MarketDataProvider):
    """A market data provider that retrieves static prices from a CSV file locally
    To be used for dev only
    """

    def __init__(self):
        with open("dev_market_data.csv", "r") as f:
            reader = csv.DictReader(f)
            # for row in reader:
            #     print(row["product"], row["price"])
            self.data = {row["product"]: float(row["price"]) for row in reader}

    def get_price(self, product: str) -> float:
        if self.data[product] is not None:
            return self.data[product]
        else:
            return 0


class FakeMarketDataProvider(MarketDataProvider):
    """A fake market data provider used for testing only
    It doesn't do anything
    """


class YahooMarketDataProvider(MarketDataProvider):
    """A market data provider that retrieves prices from Yahoo Finance"""

    def get_price(self, product: str) -> float:
        product_yf = yf.Ticker(product)
        price = product_yf.info["currentPrice"]
        print("= price = ", product, " = ", price)
        return price
