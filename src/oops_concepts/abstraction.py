"""
Abstraction — Hiding Complexity
==================================
Abstraction means showing only the ESSENTIAL features and hiding the
implementation details. Users interact with a simple interface
without knowing the complex stuff happening behind the scenes.

Real-World Analogy:
    When you drive a car 🚗, you use the steering wheel, gas pedal, and brake.
    You DON'T need to know how the engine, transmission, or fuel injection works.
    The car ABSTRACTS away all that complexity behind a simple interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# 1. Abstract Classes (ABC) — The Contract
# ---------------------------------------------------------------------------


class DatabaseConnection(ABC):
    """
    Abstract class — defines WHAT a database connection must do,
    but NOT HOW to do it. Each database implements it differently.

    Real-life analogy:
        Think of a job description. It says "must be able to read and write data."
        HOW you do it depends on whether you're using PostgreSQL, MongoDB, or SQLite.
        The job description is the ABSTRACT CLASS.
    """

    @abstractmethod
    def connect(self) -> str:
        """Connect to the database."""
        ...

    @abstractmethod
    def execute(self, query: str) -> str:
        """Execute a query."""
        ...

    @abstractmethod
    def disconnect(self) -> str:
        """Disconnect from the database."""
        ...

    # Concrete method — shared by ALL implementations
    def health_check(self) -> str:
        """Check if the connection is alive (same for all databases)."""
        try:
            result = self.execute("SELECT 1")
            return f"✅ Database is healthy: {result}"
        except Exception:
            return "❌ Database is down"


class PostgreSQLConnection(DatabaseConnection):
    """Concrete implementation for PostgreSQL."""

    def connect(self) -> str:
        return "🐘 Connected to PostgreSQL on port 5432"

    def execute(self, query: str) -> str:
        return f"🐘 PostgreSQL executed: {query}"

    def disconnect(self) -> str:
        return "🐘 Disconnected from PostgreSQL"


class MongoDBConnection(DatabaseConnection):
    """Concrete implementation for MongoDB."""

    def connect(self) -> str:
        return "🍃 Connected to MongoDB on port 27017"

    def execute(self, query: str) -> str:
        return f"🍃 MongoDB executed: {query}"

    def disconnect(self) -> str:
        return "🍃 Disconnected from MongoDB"


class SQLiteConnection(DatabaseConnection):
    """Concrete implementation for SQLite."""

    def connect(self) -> str:
        return "📦 Opened SQLite file: database.db"

    def execute(self, query: str) -> str:
        return f"📦 SQLite executed: {query}"

    def disconnect(self) -> str:
        return "📦 Closed SQLite file"


# ---------------------------------------------------------------------------
# 2. Interfaces Using ABC (Multiple Abstract Classes)
# ---------------------------------------------------------------------------


class Printable(ABC):
    """Interface: anything that can be printed/displayed."""

    @abstractmethod
    def to_string(self) -> str:
        ...


class Saveable(ABC):
    """Interface: anything that can be saved."""

    @abstractmethod
    def save(self) -> str:
        ...


class Exportable(ABC):
    """Interface: anything that can be exported."""

    @abstractmethod
    def export(self, format: str) -> str:
        ...


class Report(Printable, Saveable, Exportable):
    """
    A report that implements MULTIPLE interfaces.
    It can be printed, saved, and exported.

    Real-life analogy:
        A document can be printed (Printable), saved to disk (Saveable),
        and exported as PDF/CSV (Exportable). These are different capabilities,
        and the Report class has ALL of them.
    """

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def to_string(self) -> str:
        return f"📄 Report: {self.title}\n   {self.content}"

    def save(self) -> str:
        return f"💾 Saved report '{self.title}' to disk"

    def export(self, format: str) -> str:
        return f"📤 Exported '{self.title}' as {format.upper()}"


# ---------------------------------------------------------------------------
# 3. Real-World Example: Notification System
# ---------------------------------------------------------------------------


class NotificationService(ABC):
    """
    Abstract notification service.
    Defines the TEMPLATE of how notifications work,
    but lets subclasses handle the specifics.
    """

    def send_notification(self, recipient: str, message: str) -> str:
        """Template: validate → format → send → log (concrete steps + abstract steps)."""
        if not self._validate(recipient):
            return f"❌ Invalid recipient: {recipient}"

        formatted = self._format_message(message)
        result = self._send(recipient, formatted)
        self._log(recipient, result)
        return result

    def _validate(self, recipient: str) -> bool:
        """Concrete: basic validation (shared by all)."""
        return len(recipient) > 0

    @abstractmethod
    def _format_message(self, message: str) -> str:
        """Abstract: each channel formats differently."""
        ...

    @abstractmethod
    def _send(self, recipient: str, message: str) -> str:
        """Abstract: each channel sends differently."""
        ...

    def _log(self, recipient: str, result: str) -> None:
        """Concrete: logging is the same for all."""
        print(f"    📝 Log: Sent to {recipient} — {result[:30]}...")


class EmailNotification(NotificationService):
    def _format_message(self, message: str) -> str:
        return f"<html><body><h1>Notification</h1><p>{message}</p></body></html>"

    def _send(self, recipient: str, message: str) -> str:
        return f"📧 Email sent to {recipient}"


class SMSNotification(NotificationService):
    def _format_message(self, message: str) -> str:
        # SMS has character limit
        return message[:160]

    def _send(self, recipient: str, message: str) -> str:
        return f"📱 SMS sent to {recipient}"


class PushNotification(NotificationService):
    def _format_message(self, message: str) -> str:
        return f'{{"title": "Alert", "body": "{message}"}}'

    def _send(self, recipient: str, message: str) -> str:
        return f"🔔 Push notification sent to {recipient}"


# ---------------------------------------------------------------------------
# 4. Why You Can't Instantiate Abstract Classes
# ---------------------------------------------------------------------------


# This would raise an error:
# db = DatabaseConnection()  # TypeError: Can't instantiate abstract class!
# You MUST create a concrete subclass that implements all abstract methods.


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Abstraction demonstration."""
    print("=" * 60)
    print("  ABSTRACTION — Hiding Complexity")
    print("=" * 60)

    # --- Abstract Database Connection ---
    print("\n🗄️  1. Abstract Database Connection")
    print("-" * 40)

    databases: list[DatabaseConnection] = [
        PostgreSQLConnection(),
        MongoDBConnection(),
        SQLiteConnection(),
    ]

    for db in databases:
        print(f"  {db.connect()}")
        print(f"  {db.execute('SELECT * FROM users')}")
        print(f"  {db.health_check()}")
        print(f"  {db.disconnect()}")
        print()

    # Can't create abstract class directly
    print("  Can you create DatabaseConnection directly?")
    try:
        db = DatabaseConnection()  # type: ignore
    except TypeError as e:
        print(f"  ❌ No! {e}")

    # --- Multiple Interfaces ---
    print("\n\n📄 2. Multiple Interfaces (Printable + Saveable + Exportable)")
    print("-" * 40)

    report = Report("Q4 Sales Report", "Revenue increased by 25% this quarter.")
    print(f"  {report.to_string()}")
    print(f"  {report.save()}")
    print(f"  {report.export('pdf')}")
    print(f"  {report.export('csv')}")

    # Check interface compliance
    print(f"\n  Is Report Printable? {isinstance(report, Printable)}")
    print(f"  Is Report Saveable? {isinstance(report, Saveable)}")
    print(f"  Is Report Exportable? {isinstance(report, Exportable)}")

    # --- Notification System ---
    print("\n\n🔔 3. Abstract Notification System")
    print("-" * 40)

    services: list[NotificationService] = [
        EmailNotification(),
        SMSNotification(),
        PushNotification(),
    ]

    for service in services:
        result = service.send_notification("alice@example.com", "Your order has shipped!")
        print(f"  {result}\n")


if __name__ == "__main__":
    demo()
