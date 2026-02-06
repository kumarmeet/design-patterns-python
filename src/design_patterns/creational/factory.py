"""
Factory Method Pattern
======================
Creates objects without exposing the instantiation logic to the client.
The client just says WHAT it needs, and the factory figures out HOW to make it.

Real-World Example: Payment Processing System
Think of it like ordering food — you tell the waiter "I want pizza,"
and the kitchen decides how to make it. You don't go into the kitchen yourself.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


# ---------------------------------------------------------------------------
# Real-World Example 1: Payment Gateway System
# ---------------------------------------------------------------------------


class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    UPI = "upi"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"


@dataclass
class PaymentResult:
    """Result of processing a payment."""
    success: bool
    transaction_id: str
    message: str


class PaymentProcessor(ABC):
    """Base class for all payment processors."""

    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process a payment and return the result."""
        ...

    @abstractmethod
    def refund(self, transaction_id: str) -> PaymentResult:
        """Refund a previous transaction."""
        ...


class CreditCardProcessor(PaymentProcessor):
    """Handles credit card payments."""

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        # In real life, this would call Stripe/Visa API
        return PaymentResult(
            success=True,
            transaction_id="CC-TXN-001",
            message=f"Credit card charged {currency} {amount:.2f}",
        )

    def refund(self, transaction_id: str) -> PaymentResult:
        return PaymentResult(
            success=True,
            transaction_id=transaction_id,
            message=f"Refund initiated for {transaction_id}",
        )


class UPIProcessor(PaymentProcessor):
    """Handles UPI payments (popular in India)."""

    def process_payment(self, amount: float, currency: str = "INR") -> PaymentResult:
        return PaymentResult(
            success=True,
            transaction_id="UPI-TXN-001",
            message=f"UPI payment of {currency} {amount:.2f} completed",
        )

    def refund(self, transaction_id: str) -> PaymentResult:
        return PaymentResult(
            success=True,
            transaction_id=transaction_id,
            message=f"UPI refund initiated for {transaction_id}",
        )


class PayPalProcessor(PaymentProcessor):
    """Handles PayPal payments."""

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        return PaymentResult(
            success=True,
            transaction_id="PP-TXN-001",
            message=f"PayPal payment of {currency} {amount:.2f} completed",
        )

    def refund(self, transaction_id: str) -> PaymentResult:
        return PaymentResult(
            success=True,
            transaction_id=transaction_id,
            message=f"PayPal refund initiated for {transaction_id}",
        )


class BankTransferProcessor(PaymentProcessor):
    """Handles direct bank transfers."""

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        return PaymentResult(
            success=True,
            transaction_id="BT-TXN-001",
            message=f"Bank transfer of {currency} {amount:.2f} initiated",
        )

    def refund(self, transaction_id: str) -> PaymentResult:
        return PaymentResult(
            success=True,
            transaction_id=transaction_id,
            message=f"Bank transfer refund for {transaction_id}",
        )


class PaymentFactory:
    """
    Factory that creates the right payment processor based on the method.

    Real-life analogy:
        Think of a restaurant kitchen. You tell the waiter "I want a burger."
        The kitchen (factory) knows exactly which chef and recipe to use.
        You never go into the kitchen — you just get your burger!
    """

    _processors: dict[PaymentMethod, type[PaymentProcessor]] = {
        PaymentMethod.CREDIT_CARD: CreditCardProcessor,
        PaymentMethod.UPI: UPIProcessor,
        PaymentMethod.PAYPAL: PayPalProcessor,
        PaymentMethod.BANK_TRANSFER: BankTransferProcessor,
    }

    @classmethod
    def create(cls, method: PaymentMethod) -> PaymentProcessor:
        """Create a payment processor for the given method."""
        processor_class = cls._processors.get(method)
        if processor_class is None:
            raise ValueError(f"Unsupported payment method: {method}")
        return processor_class()

    @classmethod
    def register(cls, method: PaymentMethod, processor: type[PaymentProcessor]) -> None:
        """Register a new payment processor (extensibility!)."""
        cls._processors[method] = processor


# ---------------------------------------------------------------------------
# Real-World Example 2: Notification Service
# ---------------------------------------------------------------------------


class Notification(ABC):
    """Base class for all notification types."""

    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        """Send a notification and return a confirmation."""
        ...


class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"📧 Email sent to {recipient}: {message}"


class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"📱 SMS sent to {recipient}: {message}"


class PushNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"🔔 Push notification sent to {recipient}: {message}"


class SlackNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"💬 Slack message sent to #{recipient}: {message}"


class NotificationFactory:
    """
    Factory for creating notification senders.

    Real-life analogy:
        Think of a post office. You say "I want to send a letter"
        or "I want to send a parcel." The post office handles it differently
        based on what you need — but YOU just drop it off.
    """

    _notifiers: dict[str, type[Notification]] = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
        "slack": SlackNotification,
    }

    @classmethod
    def create(cls, channel: str) -> Notification:
        """Create a notification sender for the given channel."""
        notifier_class = cls._notifiers.get(channel.lower())
        if notifier_class is None:
            raise ValueError(f"Unknown notification channel: {channel}")
        return notifier_class()


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Factory pattern demonstration."""
    print("=" * 60)
    print("  FACTORY PATTERN DEMO")
    print("=" * 60)

    # --- Payment Example ---
    print("\n💳 Example 1: Payment Processing")
    print("-" * 40)

    for method in PaymentMethod:
        processor = PaymentFactory.create(method)
        result = processor.process_payment(99.99)
        print(f"  {method.value}: {result.message}")

    # --- Notification Example ---
    print("\n🔔 Example 2: Notification Service")
    print("-" * 40)

    channels = ["email", "sms", "push", "slack"]
    for channel in channels:
        notifier = NotificationFactory.create(channel)
        result = notifier.send("john@example.com", "Your order has shipped!")
        print(f"  {result}")


if __name__ == "__main__":
    demo()
