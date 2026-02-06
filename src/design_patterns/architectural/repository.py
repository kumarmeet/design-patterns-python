"""
Repository Pattern
===================
Abstracts data access logic from business logic.
Provides a collection-like interface for accessing domain objects.

Real-World Example: User Management System
Think of it like a library. You don't go into the warehouse to find books yourself.
You ask the librarian (repository), and they find the book for you.
You don't need to know WHERE or HOW the book is stored.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import TypeVar, Generic

T = TypeVar("T")


# ---------------------------------------------------------------------------
# Domain Models
# ---------------------------------------------------------------------------


@dataclass
class User:
    """User domain model."""
    id: int | None = None
    username: str = ""
    email: str = ""
    full_name: str = ""
    is_active: bool = True
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self) -> str:
        status = "✅" if self.is_active else "❌"
        return f"{status} User(id={self.id}, username='{self.username}', email='{self.email}')"


@dataclass
class Product:
    """Product domain model."""
    id: int | None = None
    name: str = ""
    price: float = 0.0
    stock: int = 0
    category: str = ""

    def __str__(self) -> str:
        return f"📦 Product(id={self.id}, name='{self.name}', price=${self.price:.2f}, stock={self.stock})"


# ---------------------------------------------------------------------------
# Repository Interface (Abstract)
# ---------------------------------------------------------------------------


class Repository(ABC, Generic[T]):
    """
    Generic repository interface — defines standard data operations.

    Real-life analogy:
        Think of this as a librarian's job description.
        Every librarian (regardless of the library) must be able to:
        - Find a book by ID
        - Find all books
        - Add a new book
        - Update a book's info
        - Remove a book

        HOW they do it depends on the library system (shelves, digital, etc.)
    """

    @abstractmethod
    def find_by_id(self, id: int) -> T | None:
        """Find an entity by its ID."""
        ...

    @abstractmethod
    def find_all(self) -> list[T]:
        """Get all entities."""
        ...

    @abstractmethod
    def add(self, entity: T) -> T:
        """Add a new entity."""
        ...

    @abstractmethod
    def update(self, entity: T) -> T:
        """Update an existing entity."""
        ...

    @abstractmethod
    def delete(self, id: int) -> bool:
        """Delete an entity by ID."""
        ...


# ---------------------------------------------------------------------------
# In-Memory Repository Implementation
# ---------------------------------------------------------------------------


class InMemoryUserRepository(Repository[User]):
    """
    In-memory user repository — stores users in a dictionary.

    Real-life analogy:
        A small notebook where the librarian writes down book information.
        Fast and easy, but the data is lost when you close the notebook (restart app).
    """

    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._next_id = 1

    def find_by_id(self, id: int) -> User | None:
        return self._users.get(id)

    def find_all(self) -> list[User]:
        return list(self._users.values())

    def add(self, user: User) -> User:
        user.id = self._next_id
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def update(self, user: User) -> User:
        if user.id and user.id in self._users:
            self._users[user.id] = user
            return user
        raise ValueError(f"User with id {user.id} not found")

    def delete(self, id: int) -> bool:
        if id in self._users:
            del self._users[id]
            return True
        return False

    # Custom query methods
    def find_by_username(self, username: str) -> User | None:
        for user in self._users.values():
            if user.username == username:
                return user
        return None

    def find_by_email(self, email: str) -> User | None:
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def find_active_users(self) -> list[User]:
        return [u for u in self._users.values() if u.is_active]


class InMemoryProductRepository(Repository[Product]):
    """In-memory product repository."""

    def __init__(self) -> None:
        self._products: dict[int, Product] = {}
        self._next_id = 1

    def find_by_id(self, id: int) -> Product | None:
        return self._products.get(id)

    def find_all(self) -> list[Product]:
        return list(self._products.values())

    def add(self, product: Product) -> Product:
        product.id = self._next_id
        self._products[self._next_id] = product
        self._next_id += 1
        return product

    def update(self, product: Product) -> Product:
        if product.id and product.id in self._products:
            self._products[product.id] = product
            return product
        raise ValueError(f"Product with id {product.id} not found")

    def delete(self, id: int) -> bool:
        if id in self._products:
            del self._products[id]
            return True
        return False

    def find_by_category(self, category: str) -> list[Product]:
        return [p for p in self._products.values() if p.category == category]

    def find_in_stock(self) -> list[Product]:
        return [p for p in self._products.values() if p.stock > 0]

    def find_by_price_range(self, min_price: float, max_price: float) -> list[Product]:
        return [
            p for p in self._products.values()
            if min_price <= p.price <= max_price
        ]


# ---------------------------------------------------------------------------
# Service Layer (uses Repository — doesn't know about storage details!)
# ---------------------------------------------------------------------------


class UserService:
    """
    Business logic layer that uses the repository.

    The service doesn't know HOW users are stored.
    It could be in-memory, PostgreSQL, MongoDB — it doesn't care!
    That's the power of the Repository pattern.
    """

    def __init__(self, user_repo: Repository[User]) -> None:
        self._repo = user_repo

    def register_user(self, username: str, email: str, full_name: str) -> User:
        user = User(username=username, email=email, full_name=full_name)
        return self._repo.add(user)

    def deactivate_user(self, user_id: int) -> User | None:
        user = self._repo.find_by_id(user_id)
        if user:
            user.is_active = False
            return self._repo.update(user)
        return None

    def get_all_users(self) -> list[User]:
        return self._repo.find_all()

    def find_user(self, user_id: int) -> User | None:
        return self._repo.find_by_id(user_id)


class ProductService:
    """Business logic for products."""

    def __init__(self, product_repo: InMemoryProductRepository) -> None:
        self._repo = product_repo

    def add_product(self, name: str, price: float, stock: int, category: str) -> Product:
        product = Product(name=name, price=price, stock=stock, category=category)
        return self._repo.add(product)

    def get_available_products(self) -> list[Product]:
        return self._repo.find_in_stock()

    def search_by_budget(self, budget: float) -> list[Product]:
        return self._repo.find_by_price_range(0, budget)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Repository pattern demonstration."""
    print("=" * 60)
    print("  REPOSITORY PATTERN DEMO")
    print("=" * 60)

    # --- User Repository Example ---
    print("\n👤 Example 1: User Management")
    print("-" * 50)

    user_repo = InMemoryUserRepository()
    user_service = UserService(user_repo)

    # Register users
    print("\n  Registering users:")
    alice = user_service.register_user("alice", "alice@example.com", "Alice Johnson")
    bob = user_service.register_user("bob", "bob@example.com", "Bob Smith")
    charlie = user_service.register_user("charlie", "charlie@example.com", "Charlie Brown")
    print(f"    {alice}")
    print(f"    {bob}")
    print(f"    {charlie}")

    # Deactivate a user
    print("\n  Deactivating Bob's account:")
    user_service.deactivate_user(bob.id)

    # Show all users
    print("\n  All users:")
    for user in user_service.get_all_users():
        print(f"    {user}")

    # Show active users only
    print("\n  Active users only:")
    for user in user_repo.find_active_users():
        print(f"    {user}")

    # --- Product Repository Example ---
    print("\n\n📦 Example 2: Product Catalog")
    print("-" * 50)

    product_repo = InMemoryProductRepository()
    product_service = ProductService(product_repo)

    # Add products
    print("\n  Adding products:")
    products = [
        ("Laptop", 999.99, 5, "Electronics"),
        ("Keyboard", 79.99, 20, "Electronics"),
        ("Notebook", 4.99, 100, "Stationery"),
        ("Pen", 1.99, 200, "Stationery"),
        ("Headphones", 149.99, 0, "Electronics"),  # Out of stock!
        ("Monitor", 349.99, 8, "Electronics"),
    ]

    for name, price, stock, category in products:
        p = product_service.add_product(name, price, stock, category)
        print(f"    {p}")

    # Query products
    print("\n  In-stock products:")
    for p in product_service.get_available_products():
        print(f"    {p}")

    print("\n  Products under $100:")
    for p in product_service.search_by_budget(100):
        print(f"    {p}")

    print("\n  Electronics category:")
    for p in product_repo.find_by_category("Electronics"):
        print(f"    {p}")


if __name__ == "__main__":
    demo()
