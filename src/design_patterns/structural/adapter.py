"""
Adapter Pattern
================
Allows incompatible interfaces to work together.
Acts as a translator between two systems that speak different "languages."

Real-World Example: Payment Gateway Integration
Think of a travel power adapter — your Indian plug doesn't fit a US socket,
so you use an adapter in between. The adapter makes them work together!
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Real-World Example 1: Payment Gateway Integration
# ---------------------------------------------------------------------------

@dataclass
class PaymentResponse:
    """Unified payment response our app expects."""
    success: bool
    amount: float
    currency: str
    transaction_id: str
    provider: str


class PaymentGateway(ABC):
    """The interface OUR application expects for payment processing."""

    @abstractmethod
    def charge(self, amount: float, currency: str) -> PaymentResponse:
        ...

    @abstractmethod
    def get_status(self, transaction_id: str) -> str:
        ...


# --- External payment services (we CAN'T change these!) ---


class StripeAPI:
    """Stripe's API — uses its own method names and response format."""

    def create_charge(self, amount_cents: int, cur: str) -> dict:
        return {
            "id": "ch_stripe_123",
            "status": "succeeded",
            "amount": amount_cents,
            "currency": cur,
        }

    def retrieve_charge(self, charge_id: str) -> dict:
        return {"id": charge_id, "status": "succeeded"}


class PayPalSDK:
    """PayPal's SDK — completely different interface from Stripe."""

    def make_payment(self, total: float, currency_code: str) -> dict:
        return {
            "payment_id": "PAY-paypal-456",
            "state": "approved",
            "total": total,
            "currency": currency_code,
        }

    def check_payment(self, payment_id: str) -> str:
        return "approved"


class RazorpayClient:
    """Razorpay's API — yet another different interface."""

    def create_order(self, amount_paise: int, currency: str) -> dict:
        return {
            "order_id": "order_razorpay_789",
            "status": "paid",
            "amount": amount_paise,
            "currency": currency,
        }

    def fetch_order(self, order_id: str) -> dict:
        return {"order_id": order_id, "status": "paid"}


# --- Adapters: Make external services fit OUR interface ---


class StripeAdapter(PaymentGateway):
    """
    Adapter that makes Stripe's API work with our PaymentGateway interface.

    Real-life analogy:
        Stripe speaks "French" and our app speaks "English."
        This adapter translates between them!
    """

    def __init__(self) -> None:
        self._stripe = StripeAPI()

    def charge(self, amount: float, currency: str = "usd") -> PaymentResponse:
        amount_cents = int(amount * 100)  # Stripe uses cents!
        result = self._stripe.create_charge(amount_cents, currency)
        return PaymentResponse(
            success=result["status"] == "succeeded",
            amount=amount,
            currency=currency,
            transaction_id=result["id"],
            provider="Stripe",
        )

    def get_status(self, transaction_id: str) -> str:
        result = self._stripe.retrieve_charge(transaction_id)
        return result["status"]


class PayPalAdapter(PaymentGateway):
    """Adapter that makes PayPal's SDK work with our PaymentGateway interface."""

    def __init__(self) -> None:
        self._paypal = PayPalSDK()

    def charge(self, amount: float, currency: str = "USD") -> PaymentResponse:
        result = self._paypal.make_payment(amount, currency)
        return PaymentResponse(
            success=result["state"] == "approved",
            amount=amount,
            currency=currency,
            transaction_id=result["payment_id"],
            provider="PayPal",
        )

    def get_status(self, transaction_id: str) -> str:
        return self._paypal.check_payment(transaction_id)


class RazorpayAdapter(PaymentGateway):
    """Adapter that makes Razorpay's API work with our PaymentGateway interface."""

    def __init__(self) -> None:
        self._razorpay = RazorpayClient()

    def charge(self, amount: float, currency: str = "INR") -> PaymentResponse:
        amount_paise = int(amount * 100)  # Razorpay uses paise!
        result = self._razorpay.create_order(amount_paise, currency)
        return PaymentResponse(
            success=result["status"] == "paid",
            amount=amount,
            currency=currency,
            transaction_id=result["order_id"],
            provider="Razorpay",
        )

    def get_status(self, transaction_id: str) -> str:
        result = self._razorpay.fetch_order(transaction_id)
        return result["status"]


# ---------------------------------------------------------------------------
# Real-World Example 2: Legacy CSV System to Modern JSON API
# ---------------------------------------------------------------------------


class LegacyCSVExporter:
    """Old system that only exports data as CSV strings."""

    def export_data(self) -> str:
        return "name,age,city\nAlice,30,NYC\nBob,25,LA\nCharlie,35,Chicago"


class ModernJSONAPI(ABC):
    """Our new system expects data in JSON-like format (list of dicts)."""

    @abstractmethod
    def get_data(self) -> list[dict[str, str]]:
        ...


class CSVToJSONAdapter(ModernJSONAPI):
    """
    Adapts the old CSV exporter to work as a modern JSON API.

    Real-life analogy:
        Grandma has a recipe written on a paper card.
        You type it into your phone's recipe app.
        The recipe is the same — just in a new format!
    """

    def __init__(self, csv_exporter: LegacyCSVExporter) -> None:
        self._csv_exporter = csv_exporter

    def get_data(self) -> list[dict[str, str]]:
        csv_string = self._csv_exporter.export_data()
        lines = csv_string.strip().split("\n")
        headers = lines[0].split(",")
        return [
            dict(zip(headers, line.split(",")))
            for line in lines[1:]
        ]


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Adapter pattern demonstration."""
    print("=" * 60)
    print("  ADAPTER PATTERN DEMO")
    print("=" * 60)

    # --- Payment Gateway Example ---
    print("\n💳 Example 1: Payment Gateway Adapters")
    print("-" * 40)

    gateways: list[PaymentGateway] = [
        StripeAdapter(),
        PayPalAdapter(),
        RazorpayAdapter(),
    ]

    # Same code works with ALL gateways — thanks to the adapter!
    for gateway in gateways:
        result = gateway.charge(49.99)
        print(f"  {result.provider}: {result.transaction_id} — "
              f"{'✅' if result.success else '❌'} ${result.amount:.2f}")

    # --- CSV to JSON Adapter Example ---
    print("\n📊 Example 2: Legacy CSV → Modern JSON Adapter")
    print("-" * 40)

    legacy_system = LegacyCSVExporter()
    adapter = CSVToJSONAdapter(legacy_system)

    print("  Original CSV:")
    print(f"    {legacy_system.export_data()}")
    print("\n  Converted to JSON:")
    for record in adapter.get_data():
        print(f"    {record}")


if __name__ == "__main__":
    demo()
