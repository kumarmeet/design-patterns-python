"""
SOLID Principles — 5 Rules for Clean OOP Design
==================================================
SOLID is an acronym for 5 principles that help you write code that's
easy to maintain, extend, and test. These are the FOUNDATION of design patterns.

    S — Single Responsibility Principle
    O — Open/Closed Principle
    L — Liskov Substitution Principle
    I — Interface Segregation Principle
    D — Dependency Inversion Principle
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ===========================================================================
# S — SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ===========================================================================
# A class should have only ONE reason to change.
# Each class should do ONE thing and do it well.
#
# Real-life analogy:
#     A chef cooks food. A waiter serves food. A cashier handles payments.
#     You don't want ONE person doing ALL three — if cooking rules change,
#     you'd have to modify the cashier's job too! Keep responsibilities separate.
# ===========================================================================


# ❌ BAD: One class doing EVERYTHING
class BadUserManager:
    """This class does WAY too much — registration, email, AND database."""

    def register(self, username: str, email: str, password: str) -> str:
        # Validation logic
        if "@" not in email:
            return "Invalid email"
        # Database logic
        # db.save(username, email, password)
        # Email logic
        # smtp.send(email, "Welcome!")
        return f"Registered {username}, saved to DB, sent email"


# ✅ GOOD: Each class has ONE responsibility
class UserValidator:
    """Validates user data — that's its ONLY job."""

    def validate(self, username: str, email: str, password: str) -> list[str]:
        errors = []
        if len(username) < 3:
            errors.append("Username must be at least 3 characters")
        if "@" not in email:
            errors.append("Invalid email address")
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        return errors


class UserRepository:
    """Saves/loads users — that's its ONLY job."""

    def __init__(self) -> None:
        self._users: dict[str, dict] = {}

    def save(self, username: str, email: str) -> str:
        self._users[username] = {"email": email}
        return f"💾 Saved {username} to database"

    def find(self, username: str) -> dict | None:
        return self._users.get(username)


class WelcomeEmailSender:
    """Sends welcome emails — that's its ONLY job."""

    def send(self, email: str, username: str) -> str:
        return f"📧 Welcome email sent to {email}"


class UserRegistrationService:
    """Coordinates the registration process using the single-responsibility classes."""

    def __init__(self) -> None:
        self._validator = UserValidator()
        self._repo = UserRepository()
        self._emailer = WelcomeEmailSender()

    def register(self, username: str, email: str, password: str) -> str:
        errors = self._validator.validate(username, email, password)
        if errors:
            return f"❌ Validation failed: {', '.join(errors)}"

        self._repo.save(username, email)
        self._emailer.send(email, username)
        return f"✅ {username} registered successfully!"


# ===========================================================================
# O — OPEN/CLOSED PRINCIPLE (OCP)
# ===========================================================================
# Classes should be OPEN for extension but CLOSED for modification.
# You can ADD new behavior without CHANGING existing code.
#
# Real-life analogy:
#     A phone can install new apps (open for extension)
#     without modifying the operating system (closed for modification).
# ===========================================================================


# ❌ BAD: Must modify this function every time a new shape is added
def bad_calculate_area(shape_type: str, **kwargs) -> float:
    if shape_type == "circle":
        return 3.14 * kwargs["radius"] ** 2
    elif shape_type == "rectangle":
        return kwargs["width"] * kwargs["height"]
    # Adding triangle means MODIFYING this function!
    return 0


# ✅ GOOD: Add new shapes WITHOUT modifying existing code
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class OCPCircle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class OCPRectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# Adding a new shape? Just create a new class! No existing code changes.
class OCPTriangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


def total_area(shapes: list[Shape]) -> float:
    """Works with ANY shape — now and in the future!"""
    return sum(s.area() for s in shapes)


# ===========================================================================
# L — LISKOV SUBSTITUTION PRINCIPLE (LSP)
# ===========================================================================
# Child classes should be replaceable for their parent classes
# without breaking the program.
#
# Real-life analogy:
#     If you order a "car" and they give you a Tesla, Civic, or BMW,
#     all should DRIVE the same way. A child class that breaks expectations
#     violates LSP. Imagine if a "FlyingCar" was substituted but it doesn't
#     have wheels — that would break the program!
# ===========================================================================


# ❌ BAD: Penguin violates LSP — it inherits fly() but can't actually fly!
class BadBird:
    def fly(self) -> str:
        return "Flying!"


class BadPenguin(BadBird):
    def fly(self) -> str:
        raise NotImplementedError("Penguins can't fly!")  # 💥 Breaks LSP!


# ✅ GOOD: Separate flyers from non-flyers
class LSPBird(ABC):
    @abstractmethod
    def move(self) -> str:
        ...


class FlyingBird(LSPBird):
    def move(self) -> str:
        return "🐦 Flying through the sky"


class SwimmingBird(LSPBird):
    def move(self) -> str:
        return "🐧 Swimming in the ocean"


def make_bird_move(bird: LSPBird) -> str:
    """Works with ANY bird — no surprises!"""
    return bird.move()


# ===========================================================================
# I — INTERFACE SEGREGATION PRINCIPLE (ISP)
# ===========================================================================
# Don't force a class to implement methods it doesn't need.
# Many small, specific interfaces are better than one large, general interface.
#
# Real-life analogy:
#     A printer shouldn't be forced to implement a scanner interface.
#     A simple printer just prints. A multifunction device prints AND scans.
# ===========================================================================


# ❌ BAD: One fat interface forces all machines to implement everything
class BadMachine(ABC):
    @abstractmethod
    def print_doc(self, doc: str) -> str: ...

    @abstractmethod
    def scan_doc(self, doc: str) -> str: ...

    @abstractmethod
    def fax_doc(self, doc: str) -> str: ...


# A simple printer is FORCED to implement scan and fax (which it can't do!)


# ✅ GOOD: Small, focused interfaces
class Printer(ABC):
    @abstractmethod
    def print_doc(self, doc: str) -> str:
        ...


class Scanner(ABC):
    @abstractmethod
    def scan_doc(self, doc: str) -> str:
        ...


class FaxMachine(ABC):
    @abstractmethod
    def fax_doc(self, doc: str) -> str:
        ...


class SimplePrinter(Printer):
    """Only implements what it CAN do — printing."""

    def print_doc(self, doc: str) -> str:
        return f"🖨️  Printed: {doc}"


class MultiFunctionDevice(Printer, Scanner, FaxMachine):
    """Implements ALL interfaces because it CAN do everything."""

    def print_doc(self, doc: str) -> str:
        return f"🖨️  Printed: {doc}"

    def scan_doc(self, doc: str) -> str:
        return f"📸 Scanned: {doc}"

    def fax_doc(self, doc: str) -> str:
        return f"📠 Faxed: {doc}"


# ===========================================================================
# D — DEPENDENCY INVERSION PRINCIPLE (DIP)
# ===========================================================================
# High-level modules should NOT depend on low-level modules.
# Both should depend on ABSTRACTIONS (interfaces).
#
# Real-life analogy:
#     A lamp has a plug. The wall has a socket. The plug and socket
#     are the INTERFACE. The lamp doesn't know about the power plant,
#     and the power plant doesn't know about the lamp. Both depend on
#     the standard plug/socket interface.
# ===========================================================================


# ❌ BAD: High-level depends directly on low-level
class BadMySQLDatabase:
    def query(self, sql: str) -> str:
        return f"MySQL: {sql}"


class BadUserService:
    def __init__(self) -> None:
        self.db = BadMySQLDatabase()  # 💥 Hardcoded dependency!

    def get_user(self, user_id: int) -> str:
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")


# ✅ GOOD: Both depend on abstraction
class Database(ABC):
    """Abstraction (interface) — the plug/socket standard."""

    @abstractmethod
    def query(self, statement: str) -> str:
        ...


class MySQLDatabase(Database):
    def query(self, statement: str) -> str:
        return f"🐬 MySQL: {statement}"


class PostgreSQLDatabase(Database):
    def query(self, statement: str) -> str:
        return f"🐘 PostgreSQL: {statement}"


class InMemoryDatabase(Database):
    def query(self, statement: str) -> str:
        return f"🧪 InMemory: {statement}"


class GoodUserService:
    """
    High-level module depends on abstraction (Database), not a specific database.
    You can swap MySQL for PostgreSQL or InMemory WITHOUT changing this class!
    """

    def __init__(self, db: Database) -> None:
        self.db = db  # ✅ Depends on abstraction!

    def get_user(self, user_id: int) -> str:
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the SOLID Principles demonstration."""
    print("=" * 60)
    print("  SOLID PRINCIPLES — 5 Rules for Clean OOP")
    print("=" * 60)

    # --- S: Single Responsibility ---
    print("\n📌 S — Single Responsibility Principle")
    print("-" * 40)
    service = UserRegistrationService()
    print(f"  {service.register('alice', 'alice@example.com', 'password123')}")
    print(f"  {service.register('ab', 'bad-email', 'short')}")

    # --- O: Open/Closed ---
    print("\n\n📌 O — Open/Closed Principle")
    print("-" * 40)
    shapes: list[Shape] = [
        OCPCircle(5),
        OCPRectangle(10, 6),
        OCPTriangle(8, 4),  # Added WITHOUT modifying existing code!
    ]
    for s in shapes:
        print(f"  {type(s).__name__}: area = {s.area():.2f}")
    print(f"  Total area: {total_area(shapes):.2f}")

    # --- L: Liskov Substitution ---
    print("\n\n📌 L — Liskov Substitution Principle")
    print("-" * 40)
    birds: list[LSPBird] = [FlyingBird(), SwimmingBird()]
    for bird in birds:
        print(f"  {make_bird_move(bird)}")

    # --- I: Interface Segregation ---
    print("\n\n📌 I — Interface Segregation Principle")
    print("-" * 40)
    simple = SimplePrinter()
    multi = MultiFunctionDevice()
    print(f"  Simple Printer: {simple.print_doc('report.pdf')}")
    print(f"  Multi Device: {multi.print_doc('report.pdf')}")
    print(f"  Multi Device: {multi.scan_doc('photo.jpg')}")
    print(f"  Multi Device: {multi.fax_doc('contract.pdf')}")

    # --- D: Dependency Inversion ---
    print("\n\n📌 D — Dependency Inversion Principle")
    print("-" * 40)
    # Swap databases without changing the service!
    for db in [MySQLDatabase(), PostgreSQLDatabase(), InMemoryDatabase()]:
        user_service = GoodUserService(db)
        print(f"  {user_service.get_user(42)}")


if __name__ == "__main__":
    demo()
