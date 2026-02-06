"""
Strategy Pattern
=================
Defines a family of algorithms and makes them interchangeable.
The algorithm can be selected at runtime without changing the client code.

Real-World Example: Pricing & Discount Engine
Think of it like choosing how to get to work — you can drive, take a bus,
or ride a bike. The DESTINATION is the same, but the STRATEGY (how you get there)
can be swapped easily.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Real-World Example 1: Pricing & Discount Engine
# ---------------------------------------------------------------------------


class DiscountStrategy(ABC):
    """
    Strategy interface for calculating discounts.

    Real-life analogy:
        Think of a store that has different coupons.
        Each coupon calculates the discount differently,
        but they all answer the same question: "How much do I save?"
    """

    @abstractmethod
    def calculate_discount(self, original_price: float) -> float:
        """Return the discount amount (not the final price)."""
        ...

    @abstractmethod
    def get_name(self) -> str:
        ...


class NoDiscount(DiscountStrategy):
    """No discount — pay full price."""

    def calculate_discount(self, original_price: float) -> float:
        return 0.0

    def get_name(self) -> str:
        return "No Discount"


class PercentageDiscount(DiscountStrategy):
    """Percentage-based discount (e.g., 20% off)."""

    def __init__(self, percentage: float) -> None:
        self._percentage = min(percentage, 100)  # Cap at 100%

    def calculate_discount(self, original_price: float) -> float:
        return original_price * (self._percentage / 100)

    def get_name(self) -> str:
        return f"{self._percentage}% Off"


class FlatDiscount(DiscountStrategy):
    """Fixed amount discount (e.g., $10 off)."""

    def __init__(self, amount: float) -> None:
        self._amount = amount

    def calculate_discount(self, original_price: float) -> float:
        return min(self._amount, original_price)  # Can't discount more than price

    def get_name(self) -> str:
        return f"${self._amount:.2f} Off"


class BuyOneGetOneFree(DiscountStrategy):
    """Buy one get one free — 50% off."""

    def calculate_discount(self, original_price: float) -> float:
        return original_price * 0.5

    def get_name(self) -> str:
        return "Buy 1 Get 1 Free"


class SeasonalDiscount(DiscountStrategy):
    """Seasonal sale discount with tiered pricing."""

    def __init__(self, season: str) -> None:
        self._season = season
        self._rates = {
            "summer": 15,
            "winter": 25,
            "black_friday": 40,
            "clearance": 60,
        }

    def calculate_discount(self, original_price: float) -> float:
        rate = self._rates.get(self._season.lower(), 0)
        return original_price * (rate / 100)

    def get_name(self) -> str:
        return f"{self._season.title()} Sale"


@dataclass
class CartItem:
    name: str
    price: float
    quantity: int = 1


class ShoppingCart:
    """
    Shopping cart that uses a discount strategy.
    The strategy can be changed at any time!
    """

    def __init__(self, discount_strategy: DiscountStrategy | None = None) -> None:
        self._items: list[CartItem] = []
        self._strategy = discount_strategy or NoDiscount()

    def add_item(self, item: CartItem) -> None:
        self._items.append(item)

    def set_discount_strategy(self, strategy: DiscountStrategy) -> None:
        """Change the discount strategy at runtime."""
        self._strategy = strategy

    def get_subtotal(self) -> float:
        return sum(item.price * item.quantity for item in self._items)

    def get_discount(self) -> float:
        return self._strategy.calculate_discount(self.get_subtotal())

    def get_total(self) -> float:
        return self.get_subtotal() - self.get_discount()

    def print_receipt(self) -> None:
        print(f"  {'Item':<25} {'Qty':>4} {'Price':>10}")
        print(f"  {'-'*25} {'-'*4} {'-'*10}")
        for item in self._items:
            total = item.price * item.quantity
            print(f"  {item.name:<25} {item.quantity:>4} ${total:>8.2f}")
        print(f"  {'':>25} {'':>4} {'-'*10}")
        print(f"  {'Subtotal:':<30} ${self.get_subtotal():>8.2f}")
        print(f"  {'Discount (' + self._strategy.get_name() + '):':<30} -${self.get_discount():>7.2f}")
        print(f"  {'TOTAL:':<30} ${self.get_total():>8.2f}")


# ---------------------------------------------------------------------------
# Real-World Example 2: Sorting Strategies
# ---------------------------------------------------------------------------


class SortStrategy(ABC):
    """Strategy for sorting data."""

    @abstractmethod
    def sort(self, data: list) -> list:
        ...

    @abstractmethod
    def get_name(self) -> str:
        ...


class AlphabeticalSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data, key=str)

    def get_name(self) -> str:
        return "Alphabetical"


class PriceLowToHigh(SortStrategy):
    def sort(self, data: list[CartItem]) -> list[CartItem]:
        return sorted(data, key=lambda x: x.price)

    def get_name(self) -> str:
        return "Price: Low → High"


class PriceHighToLow(SortStrategy):
    def sort(self, data: list[CartItem]) -> list[CartItem]:
        return sorted(data, key=lambda x: x.price, reverse=True)

    def get_name(self) -> str:
        return "Price: High → Low"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Strategy pattern demonstration."""
    print("=" * 60)
    print("  STRATEGY PATTERN DEMO")
    print("=" * 60)

    # --- Shopping Cart Example ---
    print("\n🛒 Example 1: Shopping Cart with Different Discounts")
    print("-" * 50)

    cart = ShoppingCart()
    cart.add_item(CartItem("Wireless Headphones", 79.99))
    cart.add_item(CartItem("Phone Case", 19.99))
    cart.add_item(CartItem("USB-C Cable", 12.99, quantity=2))

    # No discount
    print("\n  📋 No Discount:")
    cart.set_discount_strategy(NoDiscount())
    cart.print_receipt()

    # 20% off coupon
    print("\n  📋 With 20% Off Coupon:")
    cart.set_discount_strategy(PercentageDiscount(20))
    cart.print_receipt()

    # Black Friday sale
    print("\n  📋 Black Friday Sale:")
    cart.set_discount_strategy(SeasonalDiscount("black_friday"))
    cart.print_receipt()

    # Flat $15 off
    print("\n  📋 $15 Off Coupon:")
    cart.set_discount_strategy(FlatDiscount(15))
    cart.print_receipt()

    # --- Sorting Example ---
    print("\n\n📊 Example 2: Sorting Products")
    print("-" * 50)

    products = [
        CartItem("Laptop", 999.99),
        CartItem("Mouse", 29.99),
        CartItem("Keyboard", 79.99),
        CartItem("Monitor", 399.99),
        CartItem("Webcam", 59.99),
    ]

    strategies: list[SortStrategy] = [
        PriceLowToHigh(),
        PriceHighToLow(),
    ]

    for strategy in strategies:
        sorted_items = strategy.sort(products)
        print(f"\n  Sorted by: {strategy.get_name()}")
        for item in sorted_items:
            print(f"    {item.name}: ${item.price:.2f}")


if __name__ == "__main__":
    demo()
