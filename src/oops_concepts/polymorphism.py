"""
Polymorphism — Same Interface, Different Behavior
====================================================
"Poly" = many, "morph" = forms. Polymorphism means ONE interface
can work with MANY different types.

Real-World Analogy:
    A universal remote control 📺 has a "PLAY" button.
    Press it on a DVD player → plays a DVD.
    Press it on a music player → plays a song.
    Press it on a game console → starts a game.
    SAME button, DIFFERENT behavior based on the device.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
import math


# ---------------------------------------------------------------------------
# 1. Method Overriding (Runtime Polymorphism)
# ---------------------------------------------------------------------------


class Shape(ABC):
    """
    Base class for shapes.
    Each shape MUST implement area() and perimeter().
    The METHOD is the same, but the BEHAVIOR is different for each shape.

    Real-life analogy:
        Every shape can answer "What's your area?" and "What's your perimeter?"
        But a circle calculates it differently from a rectangle.
    """

    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...

    @abstractmethod
    def describe(self) -> str:
        ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def describe(self) -> str:
        return f"⭕ Circle (radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def describe(self) -> str:
        return f"🟦 Rectangle ({self.width}×{self.height})"


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def describe(self) -> str:
        return f"🔺 Triangle (sides: {self.a}, {self.b}, {self.c})"


def print_shape_info(shape: Shape) -> None:
    """
    This function works with ANY shape — it doesn't care if it's a circle,
    rectangle, or triangle. That's the power of polymorphism!
    """
    print(f"  {shape.describe()}")
    print(f"    Area: {shape.area():.2f}")
    print(f"    Perimeter: {shape.perimeter():.2f}")


# ---------------------------------------------------------------------------
# 2. Duck Typing (Python's Superpower)
# ---------------------------------------------------------------------------


class Duck:
    """A real duck."""
    def quack(self) -> str:
        return "🦆 Quack quack!"

    def swim(self) -> str:
        return "🦆 Swimming in the pond"


class Person:
    """A person pretending to be a duck."""
    def quack(self) -> str:
        return "🧑 I'm quacking like a duck!"

    def swim(self) -> str:
        return "🧑 I'm swimming like a duck!"


class RubberDuck:
    """A rubber duck toy."""
    def quack(self) -> str:
        return "🛁 Squeak squeak!"

    def swim(self) -> str:
        return "🛁 Floating in the bathtub"


def make_it_quack(thing) -> None:
    """
    Duck typing: "If it quacks like a duck, it IS a duck."

    We don't check the TYPE — we just call the method.
    If it has a quack() method, it works! If not, it fails.
    Python doesn't care about the class — only about the METHODS.
    """
    print(f"  {thing.quack()}")
    print(f"  {thing.swim()}")


# ---------------------------------------------------------------------------
# 3. Operator Overloading (Polymorphism with operators)
# ---------------------------------------------------------------------------


class Money:
    """
    A money class that supports + and comparison operators.

    Real-life analogy:
        $10 + $20 = $30. Python doesn't know how to add Money objects
        by default — we teach it using __add__, __eq__, etc.
    """

    def __init__(self, amount: float, currency: str = "USD") -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract {self.currency} and {other.currency}")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor: float) -> Money:
        return Money(self.amount * factor, self.currency)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other: Money) -> bool:
        return self.amount < other.amount

    def __gt__(self, other: Money) -> bool:
        return self.amount > other.amount

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:,.2f}"

    def __repr__(self) -> str:
        return f"Money({self.amount}, '{self.currency}')"


# ---------------------------------------------------------------------------
# 4. Real-World Example: Payment Processors
# ---------------------------------------------------------------------------


class PaymentProcessor(ABC):
    """
    Every payment processor must implement process() — but each does it differently.
    The checkout function doesn't care WHICH processor — it just calls process().
    """

    @abstractmethod
    def process(self, amount: float) -> str:
        ...

    @abstractmethod
    def get_name(self) -> str:
        ...


class CreditCardPayment(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"💳 Charged ${amount:.2f} to credit card"

    def get_name(self) -> str:
        return "Credit Card"


class PayPalPayment(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"🅿️  Sent ${amount:.2f} via PayPal"

    def get_name(self) -> str:
        return "PayPal"


class CryptoPayment(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"₿ Transferred ${amount:.2f} in Bitcoin"

    def get_name(self) -> str:
        return "Crypto"


def checkout(processor: PaymentProcessor, amount: float) -> str:
    """
    Polymorphic function — works with ANY payment processor.
    """
    return f"  [{processor.get_name()}] {processor.process(amount)}"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Polymorphism demonstration."""
    print("=" * 60)
    print("  POLYMORPHISM — Same Interface, Different Behavior")
    print("=" * 60)

    # --- Method Overriding ---
    print("\n📐 1. Method Overriding (Shapes)")
    print("-" * 40)
    shapes: list[Shape] = [
        Circle(5),
        Rectangle(10, 6),
        Triangle(3, 4, 5),
    ]
    # Same function call, different behavior!
    for shape in shapes:
        print_shape_info(shape)

    # --- Duck Typing ---
    print("\n\n🦆 2. Duck Typing")
    print("-" * 40)
    print("  'If it quacks like a duck, it IS a duck!'\n")
    things = [Duck(), Person(), RubberDuck()]
    for thing in things:
        make_it_quack(thing)
        print()

    # --- Operator Overloading ---
    print("\n💰 3. Operator Overloading")
    print("-" * 40)
    price = Money(29.99)
    tax = Money(5.40)
    total = price + tax
    print(f"  Price: {price}")
    print(f"  Tax: {tax}")
    print(f"  Total (price + tax): {total}")
    print(f"  Double: {total * 2}")
    print(f"  price > tax? {price > tax}")
    print(f"  price == Money(29.99)? {price == Money(29.99)}")

    # --- Payment Processors ---
    print("\n\n💳 4. Payment Processors (Real-World)")
    print("-" * 40)
    processors: list[PaymentProcessor] = [
        CreditCardPayment(),
        PayPalPayment(),
        CryptoPayment(),
    ]
    # Same checkout function, different processors!
    for processor in processors:
        print(checkout(processor, 99.99))


if __name__ == "__main__":
    demo()
