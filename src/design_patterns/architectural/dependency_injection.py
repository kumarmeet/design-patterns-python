"""
Dependency Injection (DI) Pattern
==================================
Provides dependencies from outside rather than creating them internally.
Objects receive their dependencies instead of constructing them.

Real-World Example: Email Service
Think of it like a restaurant. The chef (your class) doesn't go to the farm
to pick vegetables. The vegetables (dependencies) are DELIVERED to the kitchen.
The chef just cooks with whatever ingredients arrive.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Real-World Example 1: Notification Service with DI
# ---------------------------------------------------------------------------


class MessageSender(ABC):
    """Interface for sending messages — the DEPENDENCY."""

    @abstractmethod
    def send(self, recipient: str, subject: str, body: str) -> str:
        ...


class EmailSender(MessageSender):
    """Real email sender (would use SMTP in production)."""

    def send(self, recipient: str, subject: str, body: str) -> str:
        return f"📧 Email sent to {recipient}: [{subject}] {body}"


class SMSSender(MessageSender):
    """Real SMS sender (would use Twilio in production)."""

    def send(self, recipient: str, subject: str, body: str) -> str:
        return f"📱 SMS sent to {recipient}: {subject} — {body}"


class MockSender(MessageSender):
    """
    Fake sender for TESTING — doesn't actually send anything!

    This is the MAGIC of DI: in tests, you inject this fake sender
    instead of the real one. No real emails are sent during tests!
    """

    def __init__(self) -> None:
        self.sent_messages: list[dict] = []

    def send(self, recipient: str, subject: str, body: str) -> str:
        self.sent_messages.append({
            "recipient": recipient,
            "subject": subject,
            "body": body,
        })
        return f"🧪 MOCK: Would send to {recipient}: [{subject}]"


class NotificationService:
    """
    Service that sends notifications.

    WITHOUT DI (Bad ❌):
        def __init__(self):
            self.sender = EmailSender()  # Hardcoded! Can't change or test!

    WITH DI (Good ✅):
        def __init__(self, sender: MessageSender):
            self.sender = sender  # Injected! Flexible and testable!

    Real-life analogy:
        Think of a car engine. Without DI, the engine is welded to one specific
        type of fuel tank. With DI, you can swap fuel tanks (gasoline, diesel,
        electric) without redesigning the engine!
    """

    def __init__(self, sender: MessageSender) -> None:
        # The sender is INJECTED — not created here!
        self._sender = sender

    def send_welcome(self, user_email: str, user_name: str) -> str:
        return self._sender.send(
            user_email,
            "Welcome!",
            f"Hi {user_name}, welcome to our platform!",
        )

    def send_password_reset(self, user_email: str) -> str:
        return self._sender.send(
            user_email,
            "Password Reset",
            "Click here to reset your password: https://example.com/reset",
        )

    def send_order_confirmation(self, user_email: str, order_id: str) -> str:
        return self._sender.send(
            user_email,
            f"Order Confirmed — {order_id}",
            f"Your order {order_id} has been confirmed!",
        )


# ---------------------------------------------------------------------------
# Real-World Example 2: Service Container (Simple DI Container)
# ---------------------------------------------------------------------------


class ServiceContainer:
    """
    A simple dependency injection container.

    Real-life analogy:
        Think of a toolbox. Instead of each worker bringing their own tools,
        there's a shared toolbox (container) where everyone gets their tools.
        The toolbox decides WHICH specific tool to give each worker.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}
        self._factories: dict[str, Any] = {}

    def register_singleton(self, name: str, instance: Any) -> None:
        """Register a single shared instance (singleton)."""
        self._services[name] = instance

    def register_factory(self, name: str, factory: Any) -> None:
        """Register a factory that creates new instances each time."""
        self._factories[name] = factory

    def resolve(self, name: str) -> Any:
        """Get a service by name."""
        if name in self._services:
            return self._services[name]
        if name in self._factories:
            return self._factories[name]()
        raise ValueError(f"Service '{name}' not registered")

    def list_services(self) -> list[str]:
        all_services = set(self._services.keys()) | set(self._factories.keys())
        return sorted(all_services)


# ---------------------------------------------------------------------------
# Real-World Example 3: Database Layer with DI
# ---------------------------------------------------------------------------


class Database(ABC):
    """Interface for database operations."""

    @abstractmethod
    def save(self, table: str, data: dict) -> str:
        ...

    @abstractmethod
    def find(self, table: str, id: int) -> dict | None:
        ...


class PostgresDatabase(Database):
    def save(self, table: str, data: dict) -> str:
        return f"🐘 PostgreSQL: Saved to '{table}' → {data}"

    def find(self, table: str, id: int) -> dict | None:
        return {"id": id, "source": "PostgreSQL", "table": table}


class SQLiteDatabase(Database):
    def save(self, table: str, data: dict) -> str:
        return f"📦 SQLite: Saved to '{table}' → {data}"

    def find(self, table: str, id: int) -> dict | None:
        return {"id": id, "source": "SQLite", "table": table}


class InMemoryDatabase(Database):
    """In-memory database for testing — no real DB needed!"""

    def __init__(self) -> None:
        self._store: dict[str, list[dict]] = {}

    def save(self, table: str, data: dict) -> str:
        if table not in self._store:
            self._store[table] = []
        self._store[table].append(data)
        return f"🧪 InMemory: Saved to '{table}' → {data}"

    def find(self, table: str, id: int) -> dict | None:
        records = self._store.get(table, [])
        for record in records:
            if record.get("id") == id:
                return record
        return None


class UserService:
    """
    User service that depends on a Database — injected via DI.
    Works with PostgreSQL, SQLite, or InMemory (for tests)!
    """

    def __init__(self, database: Database, notifier: NotificationService) -> None:
        self._db = database
        self._notifier = notifier

    def create_user(self, name: str, email: str) -> str:
        result = self._db.save("users", {"name": name, "email": email})
        notification = self._notifier.send_welcome(email, name)
        return f"{result}\n    {notification}"

    def find_user(self, user_id: int) -> dict | None:
        return self._db.find("users", user_id)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Dependency Injection pattern demonstration."""
    print("=" * 60)
    print("  DEPENDENCY INJECTION PATTERN DEMO")
    print("=" * 60)

    # --- Production Setup ---
    print("\n🏭 Example 1: Production Environment")
    print("-" * 50)

    email_sender = EmailSender()
    notification_service = NotificationService(email_sender)

    print(f"  {notification_service.send_welcome('alice@example.com', 'Alice')}")
    print(f"  {notification_service.send_order_confirmation('alice@example.com', 'ORD-001')}")

    # --- Testing Setup (swap the dependency!) ---
    print("\n\n🧪 Example 2: Testing Environment (Mock Sender)")
    print("-" * 50)

    mock_sender = MockSender()
    test_notification_service = NotificationService(mock_sender)  # Inject mock!

    test_notification_service.send_welcome("test@test.com", "TestUser")
    test_notification_service.send_password_reset("test@test.com")

    print(f"  Messages sent (captured by mock): {len(mock_sender.sent_messages)}")
    for msg in mock_sender.sent_messages:
        print(f"    → To: {msg['recipient']}, Subject: {msg['subject']}")

    # --- Service Container Example ---
    print("\n\n📦 Example 3: Service Container (DI Container)")
    print("-" * 50)

    container = ServiceContainer()

    # Register services
    container.register_singleton("database", PostgresDatabase())
    container.register_singleton("email_sender", EmailSender())
    container.register_factory("notification_service",
                                lambda: NotificationService(container.resolve("email_sender")))

    print(f"  Registered services: {container.list_services()}")

    db = container.resolve("database")
    notifier = container.resolve("notification_service")

    print(f"  {db.save('users', {'name': 'Bob', 'email': 'bob@example.com'})}")
    print(f"  {notifier.send_welcome('bob@example.com', 'Bob')}")

    # --- Full Integration Example ---
    print("\n\n🔗 Example 4: Full Stack with DI")
    print("-" * 50)

    # Production
    print("  Production:")
    prod_db = PostgresDatabase()
    prod_notifier = NotificationService(EmailSender())
    prod_user_service = UserService(prod_db, prod_notifier)
    print(f"    {prod_user_service.create_user('Charlie', 'charlie@example.com')}")

    # Test (swap ALL dependencies!)
    print("\n  Testing:")
    test_db = InMemoryDatabase()
    test_notifier = NotificationService(MockSender())
    test_user_service = UserService(test_db, test_notifier)
    print(f"    {test_user_service.create_user('TestUser', 'test@test.com')}")


if __name__ == "__main__":
    demo()
