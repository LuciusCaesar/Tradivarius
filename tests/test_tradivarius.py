from tradivarius import Portfolio, optimize_sharp_ratio
from market import FakeMarketDataProvider


def test_portfolio_value(mocker):
    cash = 1000
    quantity = 100
    price = 30

    marketDataProvider = FakeMarketDataProvider()
    mocker.patch.object(marketDataProvider, "get_price", return_value=price)

    portfolio = Portfolio(
        label="Testing Portfolio",
        cash=cash,
        composition={"AAPL": quantity},
        marketDataProvider=marketDataProvider,
    )

    assert portfolio.value == cash + quantity * price


def test_optimization_doesnt_change_portfolio_value(mocker):
    # Note: due to rounding, it's possible that value isn't strictly equal.
    # This would still be an attention point:
    # - a continuous drift in one direction wouldn't be acceptable.
    # - it should anyway be a "small" difference (small is to be defined): if it's happens a lot, it would result in a big total cash leak
    marketDataProvider = FakeMarketDataProvider()
    initial_portfolio = Portfolio(
        label="Testing Portfolio",
        cash=1000,
        composition={"AAPL": 100, "MSFT": 100},
        marketDataProvider=marketDataProvider,
    )

    mocker.patch.object(marketDataProvider, "get_price", return_value=30)

    final_portfolio = optimize_sharp_ratio(initial_portfolio)

    assert initial_portfolio.value == final_portfolio.value


def test_optimization_keeps_same_universe():
    initial_portfolio = Portfolio(
        label="Testing Portfolio",
        cash=1000,
        composition={"AAPL": 100, "MSFT": 100},
        marketDataProvider=FakeMarketDataProvider(),
    )

    final_portfolio = optimize_sharp_ratio(initial_portfolio)

    assert initial_portfolio.universe == final_portfolio.universe
