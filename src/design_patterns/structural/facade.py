"""
Facade Pattern
===============
Provides a simple interface to a complex subsystem.
Hides the complicated stuff behind an easy-to-use door.

Real-World Example: Online Shopping "Place Order" Button
When you click "Place Order," a LOT happens behind the scenes:
inventory check, payment, shipping, email confirmation.
But YOU just click one button. That button is the Facade!
"""

from __future__ import annotations

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Complex subsystem classes (the messy behind-the-scenes stuff)
# ---------------------------------------------------------------------------


class InventoryService:
    """Manages product stock levels."""

    def __init__(self) -> None:
        self._stock: dict[str, int] = {
            "LAPTOP-001": 10,
            "PHONE-002": 25,
            "HEADPHONE-003": 50,
        }

    def check_stock(self, product_id: str, quantity: int) -> bool:
        available = self._stock.get(product_id, 0)
        return available >= quantity

    def reserve_stock(self, product_id: str, quantity: int) -> bool:
        if self.check_stock(product_id, quantity):
            self._stock[product_id] -= quantity
            return True
        return False

    def get_stock(self, product_id: str) -> int:
        return self._stock.get(product_id, 0)


class PaymentService:
    """Handles payment processing."""

    def validate_card(self, card_number: str) -> bool:
        # Simple validation: card number should be 16 digits
        return len(card_number.replace(" ", "")) == 16

    def charge(self, card_number: str, amount: float) -> dict:
        if not self.validate_card(card_number):
            return {"success": False, "error": "Invalid card number"}
        return {
            "success": True,
            "transaction_id": f"TXN-{abs(hash(card_number)) % 10000:04d}",
            "amount": amount,
        }

    def refund(self, transaction_id: str) -> dict:
        return {"success": True, "message": f"Refund issued for {transaction_id}"}


class ShippingService:
    """Manages shipping and delivery."""

    def calculate_shipping(self, address: str, weight: float) -> float:
        # Simple shipping calculation
        base_cost = 5.99
        per_kg = 2.50
        return base_cost + (weight * per_kg)

    def create_shipment(self, address: str, product_id: str) -> dict:
        return {
            "tracking_id": f"SHIP-{abs(hash(address)) % 100000:05d}",
            "status": "processing",
            "destination": address,
        }


class EmailService:
    """Sends email notifications."""

    def send_order_confirmation(self, email: str, order_id: str) -> str:
        return f"📧 Confirmation sent to {email} for order {order_id}"

    def send_shipping_notification(self, email: str, tracking_id: str) -> str:
        return f"📧 Shipping update sent to {email} — Tracking: {tracking_id}"


class FraudDetectionService:
    """Checks for fraudulent transactions."""

    def check_transaction(self, amount: float, card_number: str) -> bool:
        # Flag transactions over $10,000 as suspicious
        return amount <= 10_000


# ---------------------------------------------------------------------------
# The FACADE — one simple interface for all that complexity
# ---------------------------------------------------------------------------


@dataclass
class OrderResult:
    """Simple result of placing an order."""
    success: bool
    order_id: str = ""
    tracking_id: str = ""
    total: float = 0.0
    message: str = ""


class OnlineStoreFacade:
    """
    Facade for the online shopping system.

    Real-life analogy:
        Think of a hotel concierge. You say "I want to go sightseeing."
        Behind the scenes, they book a taxi, buy tickets, plan the route,
        and pack your lunch. But YOU just made one simple request!

    Without the facade, you'd have to:
        1. Check inventory manually
        2. Validate the card yourself
        3. Run fraud detection
        4. Process payment
        5. Create shipment
        6. Send emails

    With the facade, you just call: place_order()
    """

    def __init__(self) -> None:
        self._inventory = InventoryService()
        self._payment = PaymentService()
        self._shipping = ShippingService()
        self._email = EmailService()
        self._fraud = FraudDetectionService()
        self._order_counter = 0

    def place_order(
        self,
        product_id: str,
        quantity: int,
        card_number: str,
        shipping_address: str,
        email: str,
    ) -> OrderResult:
        """
        Place an order — this single method orchestrates everything.
        """
        self._order_counter += 1
        order_id = f"ORD-{self._order_counter:04d}"
        price_per_unit = 99.99  # Simplified pricing

        print(f"\n  🛒 Processing Order {order_id}...")

        # Step 1: Check inventory
        if not self._inventory.check_stock(product_id, quantity):
            return OrderResult(False, order_id, message="❌ Out of stock")
        print(f"    ✅ Stock available ({self._inventory.get_stock(product_id)} in stock)")

        # Step 2: Calculate total
        total = price_per_unit * quantity
        shipping = self._shipping.calculate_shipping(shipping_address, quantity * 0.5)
        total += shipping
        print(f"    💰 Total: ${total:.2f} (incl. ${shipping:.2f} shipping)")

        # Step 3: Fraud check
        if not self._fraud.check_transaction(total, card_number):
            return OrderResult(False, order_id, message="🚨 Transaction flagged as suspicious")
        print("    🔍 Fraud check passed")

        # Step 4: Process payment
        payment_result = self._payment.charge(card_number, total)
        if not payment_result["success"]:
            return OrderResult(False, order_id, message=f"❌ Payment failed: {payment_result['error']}")
        print(f"    💳 Payment successful: {payment_result['transaction_id']}")

        # Step 5: Reserve inventory
        self._inventory.reserve_stock(product_id, quantity)
        print(f"    📦 Stock reserved")

        # Step 6: Create shipment
        shipment = self._shipping.create_shipment(shipping_address, product_id)
        print(f"    🚚 Shipment created: {shipment['tracking_id']}")

        # Step 7: Send confirmation email
        email_result = self._email.send_order_confirmation(email, order_id)
        print(f"    {email_result}")

        return OrderResult(
            success=True,
            order_id=order_id,
            tracking_id=shipment["tracking_id"],
            total=total,
            message="✅ Order placed successfully!",
        )


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Facade pattern demonstration."""
    print("=" * 60)
    print("  FACADE PATTERN DEMO")
    print("=" * 60)

    print("\n🏪 Example: Online Store — Place Order")
    print("-" * 40)

    store = OnlineStoreFacade()

    # Successful order
    result1 = store.place_order(
        product_id="LAPTOP-001",
        quantity=1,
        card_number="4111 1111 1111 1111",
        shipping_address="123 Main St, New York, NY",
        email="alice@example.com",
    )
    print(f"\n  Result: {result1.message}")
    print(f"  Order ID: {result1.order_id}")
    print(f"  Tracking: {result1.tracking_id}")
    print(f"  Total: ${result1.total:.2f}")

    # Failed order (bad card)
    result2 = store.place_order(
        product_id="PHONE-002",
        quantity=1,
        card_number="1234",  # Too short!
        shipping_address="456 Oak Ave, Los Angeles, CA",
        email="bob@example.com",
    )
    print(f"\n  Result: {result2.message}")


if __name__ == "__main__":
    demo()
