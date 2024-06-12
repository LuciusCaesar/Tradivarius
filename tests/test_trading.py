from portfolio import Portfolio
from trading import TradeOrder, TradingProvider
from market import DevMarketDataProvider


def test_create_orders():
    initial_portfolio = Portfolio(
        label="Testing Portfolio",
        cash=1000,
        composition={"AAPL": 100, "MSFT": 100},
        marketDataProvider=DevMarketDataProvider(),
    )

    target_portfolio = Portfolio(
        label="Testing Portfolio",
        cash=1000,
        composition={"AAPL": 30, "MSFT": 110},
        marketDataProvider=DevMarketDataProvider(),
    )

    trade_orders = TradingProvider().create_trade_orders(
        initial_portfolio, target_portfolio
    )

    assert len(trade_orders) == 2
    assert TradeOrder("AAPL", -70) in trade_orders
    assert TradeOrder("MSFT", 10) in trade_orders


def test_create_orders_with_zero_delta():
    initial_portfolio = Portfolio(
        label="Testing Portfolio",
        cash=1000,
        composition={"AAPL": 100, "MSFT": 100},
        marketDataProvider=DevMarketDataProvider(),
    )

    target_portfolio = Portfolio(
        label="Testing Portfolio",
        cash=1000,
        composition={"AAPL": 100, "MSFT": 100},
        marketDataProvider=DevMarketDataProvider(),
    )

    trade_orders = TradingProvider().create_trade_orders(
        initial_portfolio, target_portfolio
    )

    assert len(trade_orders) == 0
