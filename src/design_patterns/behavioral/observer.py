"""
Observer Pattern
=================
Defines a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically.

Real-World Example: YouTube Channel Subscriptions
Think of it like subscribing to a YouTube channel. When a new video is uploaded,
ALL subscribers get notified automatically. The channel doesn't need to know
who its subscribers are — it just broadcasts the update.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


# ---------------------------------------------------------------------------
# Real-World Example 1: E-Commerce Order Status Tracker
# ---------------------------------------------------------------------------


class OrderStatus(Enum):
    PLACED = "Order Placed"
    CONFIRMED = "Order Confirmed"
    PREPARING = "Preparing"
    SHIPPED = "Shipped"
    OUT_FOR_DELIVERY = "Out for Delivery"
    DELIVERED = "Delivered"


class OrderObserver(ABC):
    """
    Observer: Something that wants to be notified when an order changes.

    Real-life analogy:
        When you order a pizza, YOU get updates, the RESTAURANT dashboard shows updates,
        and the DELIVERY DRIVER gets updates — all three are observers!
    """

    @abstractmethod
    def update(self, order_id: str, status: OrderStatus, details: str) -> None:
        ...


class CustomerNotifier(OrderObserver):
    """Notifies the customer via email/SMS."""

    def __init__(self, customer_name: str) -> None:
        self.customer_name = customer_name
        self.notifications: list[str] = []

    def update(self, order_id: str, status: OrderStatus, details: str) -> None:
        msg = f"📧 Dear {self.customer_name}, your order {order_id}: {status.value}. {details}"
        self.notifications.append(msg)
        print(f"    {msg}")


class DashboardUpdater(OrderObserver):
    """Updates the admin dashboard in real-time."""

    def __init__(self) -> None:
        self.updates: list[dict] = []

    def update(self, order_id: str, status: OrderStatus, details: str) -> None:
        entry = {"order_id": order_id, "status": status.value, "time": str(datetime.now())}
        self.updates.append(entry)
        print(f"    📊 Dashboard updated: {order_id} → {status.value}")


class InventoryManager(OrderObserver):
    """Adjusts inventory when orders are placed or cancelled."""

    def update(self, order_id: str, status: OrderStatus, details: str) -> None:
        if status == OrderStatus.CONFIRMED:
            print(f"    📦 Inventory: Stock reserved for {order_id}")
        elif status == OrderStatus.DELIVERED:
            print(f"    📦 Inventory: {order_id} completed — stock finalized")


class DeliveryTracker(OrderObserver):
    """Tracks deliveries for the logistics team."""

    def update(self, order_id: str, status: OrderStatus, details: str) -> None:
        if status in (OrderStatus.SHIPPED, OrderStatus.OUT_FOR_DELIVERY, OrderStatus.DELIVERED):
            print(f"    🚚 Delivery Team: {order_id} → {status.value}")


class Order:
    """
    Subject: The order that observers watch.

    When the order status changes, ALL registered observers are notified.
    """

    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        self._status = OrderStatus.PLACED
        self._observers: list[OrderObserver] = []

    def subscribe(self, observer: OrderObserver) -> None:
        """Add an observer."""
        self._observers.append(observer)

    def unsubscribe(self, observer: OrderObserver) -> None:
        """Remove an observer."""
        self._observers.remove(observer)

    def update_status(self, status: OrderStatus, details: str = "") -> None:
        """Change the order status — all observers get notified!"""
        self._status = status
        print(f"\n  🔄 Order {self.order_id} status changed to: {status.value}")
        self._notify_all(details)

    def _notify_all(self, details: str) -> None:
        for observer in self._observers:
            observer.update(self.order_id, self._status, details)


# ---------------------------------------------------------------------------
# Real-World Example 2: Stock Price Monitor
# ---------------------------------------------------------------------------


@dataclass
class StockPrice:
    symbol: str
    price: float
    change: float = 0.0


class StockObserver(ABC):
    @abstractmethod
    def on_price_change(self, stock: StockPrice) -> None:
        ...


class PriceAlertObserver(StockObserver):
    """Sends alert when price crosses a threshold."""

    def __init__(self, name: str, threshold: float, direction: str = "above") -> None:
        self.name = name
        self.threshold = threshold
        self.direction = direction
        self.alerts: list[str] = []

    def on_price_change(self, stock: StockPrice) -> None:
        triggered = (
            (self.direction == "above" and stock.price > self.threshold)
            or (self.direction == "below" and stock.price < self.threshold)
        )
        if triggered:
            alert = f"⚠️  {self.name}: {stock.symbol} is ${stock.price:.2f} ({self.direction} ${self.threshold:.2f})"
            self.alerts.append(alert)
            print(f"    {alert}")


class PortfolioTracker(StockObserver):
    """Tracks portfolio value changes."""

    def __init__(self) -> None:
        self.holdings: dict[str, int] = {}  # symbol -> quantity
        self.prices: dict[str, float] = {}

    def add_holding(self, symbol: str, quantity: int) -> None:
        self.holdings[symbol] = quantity

    def on_price_change(self, stock: StockPrice) -> None:
        self.prices[stock.symbol] = stock.price
        if stock.symbol in self.holdings:
            value = stock.price * self.holdings[stock.symbol]
            print(f"    💼 Portfolio: {self.holdings[stock.symbol]} x {stock.symbol} = ${value:,.2f}")


@dataclass
class StockMarket:
    """Subject: The stock market that notifies observers of price changes."""

    _stocks: dict[str, StockPrice] = field(default_factory=dict)
    _observers: list[StockObserver] = field(default_factory=list)

    def subscribe(self, observer: StockObserver) -> None:
        self._observers.append(observer)

    def update_price(self, symbol: str, new_price: float) -> None:
        old_price = self._stocks.get(symbol, StockPrice(symbol, new_price)).price
        change = new_price - old_price
        stock = StockPrice(symbol, new_price, change)
        self._stocks[symbol] = stock

        direction = "📈" if change >= 0 else "📉"
        print(f"\n  {direction} {symbol}: ${new_price:.2f} ({change:+.2f})")

        for observer in self._observers:
            observer.on_price_change(stock)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Observer pattern demonstration."""
    print("=" * 60)
    print("  OBSERVER PATTERN DEMO")
    print("=" * 60)

    # --- Order Tracking Example ---
    print("\n📦 Example 1: E-Commerce Order Tracking")
    print("-" * 50)

    order = Order("ORD-2024-001")

    # Register observers
    customer = CustomerNotifier("Alice")
    dashboard = DashboardUpdater()
    inventory = InventoryManager()
    delivery = DeliveryTracker()

    order.subscribe(customer)
    order.subscribe(dashboard)
    order.subscribe(inventory)
    order.subscribe(delivery)

    # Simulate order lifecycle
    order.update_status(OrderStatus.CONFIRMED, "Payment received")
    order.update_status(OrderStatus.PREPARING, "Chef is making your food")
    order.update_status(OrderStatus.SHIPPED, "Package picked up by courier")
    order.update_status(OrderStatus.DELIVERED, "Left at front door")

    # --- Stock Market Example ---
    print("\n\n💹 Example 2: Stock Market Monitor")
    print("-" * 50)

    market = StockMarket()

    # Create observers
    high_alert = PriceAlertObserver("High Alert", 200, "above")
    low_alert = PriceAlertObserver("Low Alert", 150, "below")
    portfolio = PortfolioTracker()
    portfolio.add_holding("AAPL", 50)
    portfolio.add_holding("GOOGL", 10)

    market.subscribe(high_alert)
    market.subscribe(low_alert)
    market.subscribe(portfolio)

    # Simulate price changes
    market.update_price("AAPL", 185.50)
    market.update_price("GOOGL", 142.30)
    market.update_price("AAPL", 205.75)
    market.update_price("GOOGL", 148.20)


if __name__ == "__main__":
    demo()
