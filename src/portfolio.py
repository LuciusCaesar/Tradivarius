import market
from dataclasses import dataclass


@dataclass
class Portfolio:
    """
    A portfolio is
    - a collection of products and their quantities
    - cash amount available
    """

    label: int | str
    cash: int
    composition: dict
    marketDataProvider: market.MarketDataProvider
    # def __init__(
    #     self,
    #     label: int | str,
    #     cash: int = 0,
    #     composition: dict = {},
    #     marketDataProvider=market.MarketDataProvider(),
    # ):
    #     """
    #     Initializes a new instance of the Portfolio class.

    #     Parameters:
    #         id (int | str): The unique identifier of the portfolio.
    #         cash (int, optional): The initial cash amount in the portfolio. Defaults to 0.
    #         composition (dict, optional): The initial composition of the portfolio. Defaults to an empty dictionary.
    #         marketDataProvider (MarketDataProvider, optional): The market data provider for retrieving market prices. Defaults to a new instance of the MarketDataProvider class.

    #     Returns:
    #         None
    #     """
    #     self.label = label
    #     self.cash = cash
    #     self.composition = composition
    #     self.marketDataProvider = marketDataProvider

    @property
    def universe(self) -> list:
        """
        Returns the list of products in the portfolio.

        Returns:
            list: The list of products in the portfolio.
        """
        return list(self.composition.keys())

    @property
    def value(self) -> float:
        """
        Calculate the total value of the portfolio.

        Returns:
            float: The total value of the portfolio, which is the sum of the cash amount and the value of the composition.
        """
        return self.cash + self.composition_value

    @property
    def composition_value(self) -> float:
        """
        Calculates the total value of the portfolio's composition by multiplying the quantity of each product
        in the portfolio with its current market price.
        Warning: it doesn't take into account the cash

        Returns:
            float: The total value of the portfolio's composition.
        """
        return sum(
            [
                quantity * self.marketDataProvider.get_price(product)
                for product, quantity in self.composition.items()
            ]
        )
