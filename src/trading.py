from portfolio import Portfolio
from dataclasses import dataclass


@dataclass
class TradeOrder:
    product: str
    delta_quantity: int


@dataclass
class Transaction:
    """
    A transaction is a change in quantity of a product for a given price
    The quantity is the delta of the product (positive or negative, respectively to buy or sell)
    The price is the price at which the transaction took place (attention, it is negative for a cash outs, and positive for a cash ins)
    """

    product: str
    quantity: int
    price: float


class TradingProvider:
    def trade(self, product: str, quantity: int):
        pass

    def trades(self, trade_orders: list[TradeOrder]) -> list[Transaction]:
        return [
            self.trade(order.product, order.delta_quantity) for order in trade_orders
        ]

    def create_trade_orders(
        self, initial_portfolio: Portfolio, target_portfolio: Portfolio
    ) -> list[TradeOrder]:
        print("*** create_trade_orders ***")
        initial_composition = initial_portfolio.composition
        target_composition = target_portfolio.composition

        delta_quantities = {
            x: target_composition[x] - initial_composition[x]
            for x in initial_composition
            if target_composition[x]
            != initial_composition[
                x
            ]  # Only creates a trade order when the quantity needs to change
        }

        print(
            "list of products and quantity to trade: (negative = selling, postive = buying)"
        )
        print(delta_quantities)

        return [TradeOrder(x, delta_quantities[x]) for x in delta_quantities.keys()]

    def make_trade_oders(
        self, portfolio: Portfolio, trade_orders: list[TradeOrder]
    ) -> Portfolio:
        print("*** make_trade_orders ***")

        transactions = self.trades(trade_orders)

        for transaction in transactions:
            portfolio.cash += transaction.price
            portfolio.composition[transaction.product] += transaction.quantity

        return portfolio


class DevTradingProvider(TradingProvider):
    def trade(self, product: str, quantity: int):
        # Do something through external platform
        # TODO: not a real implementation
        print("-- WARNING: Trade product: fake implementation --> TO BE CHANGED")
        return Transaction(product, quantity, -1 * quantity)
