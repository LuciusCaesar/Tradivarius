from market import DevMarketDataProvider, YahooMarketDataProvider
from portfolio import Portfolio
from trading import DevTradingProvider


def optimize_sharp_ratio(initial_portfolio: Portfolio) -> Portfolio:
    """
    Optimizes the composition of an initial portfolio by setting new quantities of each product
    in such a way that the total value of the portfolio is unchanged but the Sharp ratio gets better.

    Args:
        initial_portfolio (Portfolio): The initial portfolio to optimize.

    Returns:
        Portfolio: The optimized portfolio with same list of products but with new quantities.
    """
    print("*** Optimize Portfolio: Sharp Ratio optimization ***")

    def optimize(portfolio_composition: dict) -> dict:
        print(
            "-- WARNING: Portfolio optimization: fake implementation --> TO BE CHANGED"
        )
        # TODO: this is hard-coded quantity !!!
        return {x: 30 for x in portfolio_composition.keys()}

    return Portfolio(
        label=initial_portfolio.label,
        cash=initial_portfolio.cash,
        composition=optimize(initial_portfolio.composition),
        marketDataProvider=initial_portfolio.marketDataProvider,
    )


def main():
    # Connect to a Market Data Provider
    # market_data_provider = DevMarketDataProvider()
    market_data_provider = YahooMarketDataProvider()
    trading_provider = DevTradingProvider()

    # Create a portfolio
    initial_portfolio = Portfolio(
        label="Testing Portfolio",
        cash=1000,
        composition={"AAPL": 100, "MSFT": 100},
        marketDataProvider=market_data_provider,
    )

    print("Initial Portfolio: ", initial_portfolio)
    print("Initial Portfolio Value: ", initial_portfolio.value)

    # Define the order to place
    # then place these orders
    # and returns the updated portfolio according to the result of the actual transactions
    # Note: in principle, the total value of the portfolio should not change (a lot) through this operation: sold value = bought value
    # only the sharp-ratio should get better
    target_portfolio = optimize_sharp_ratio(initial_portfolio)

    # Place the orders and returns the updated portfolio
    final_portfolio = trading_provider.make_trade_oders(
        initial_portfolio,
        trading_provider.create_trade_orders(initial_portfolio, target_portfolio),
    )

    print("Final Portfolio: ", final_portfolio)
    print("Final Portfolio Value: ", final_portfolio.value)


if __name__ == "__main__":
    main()
