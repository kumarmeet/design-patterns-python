"""
Classes and Objects — The Foundation of OOP
=============================================
Everything in OOP starts here.
A CLASS is a blueprint. An OBJECT is a thing built from that blueprint.

Real-World Analogy:
    A class is like a cookie cutter 🍪
    An object is the actual cookie made from it.
    One cutter → many cookies, each can have different toppings!
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# 1. Basic Class and Object
# ---------------------------------------------------------------------------


class Dog:
    """
    A simple Dog class — a blueprint for creating dog objects.

    Real-life analogy:
        This is like a "Dog Registration Form."
        Every dog has a name, breed, and age.
        Each filled-out form is an OBJECT (a specific dog).
    """

    # Class variable — shared by ALL dogs
    species = "Canis familiaris"

    def __init__(self, name: str, breed: str, age: int) -> None:
        """
        Constructor — called when you create a new dog.
        'self' refers to the specific dog being created.
        """
        # Instance variables — unique to each dog
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self) -> str:
        """Instance method — something the dog can DO."""
        return f"🐕 {self.name} says: Woof! Woof!"

    def describe(self) -> str:
        """Describe this specific dog."""
        return f"🐕 {self.name} is a {self.age}-year-old {self.breed}"

    def birthday(self) -> str:
        """The dog ages by one year."""
        self.age += 1
        return f"🎂 Happy birthday {self.name}! Now {self.age} years old."

    def __str__(self) -> str:
        """What to show when you print() the object."""
        return self.describe()

    def __repr__(self) -> str:
        """Technical representation (for debugging)."""
        return f"Dog(name='{self.name}', breed='{self.breed}', age={self.age})"


# ---------------------------------------------------------------------------
# 2. Class vs Instance Variables
# ---------------------------------------------------------------------------


class BankAccount:
    """
    Demonstrates class vs instance variables.

    Class variable: bank_name — same for ALL accounts.
    Instance variables: owner, balance — unique per account.

    Real-life analogy:
        Every account at "National Bank" shares the bank name,
        but each person has their own balance.
    """

    # Class variable — shared by all accounts
    bank_name = "National Bank"
    total_accounts = 0

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # Instance variables — unique to each account
        self.owner = owner
        self.balance = balance
        self.transactions: list[str] = []

        # Update the class variable
        BankAccount.total_accounts += 1
        self.account_number = BankAccount.total_accounts

    def deposit(self, amount: float) -> str:
        if amount <= 0:
            return "❌ Deposit amount must be positive"
        self.balance += amount
        self.transactions.append(f"+${amount:.2f}")
        return f"✅ Deposited ${amount:.2f}. Balance: ${self.balance:.2f}"

    def withdraw(self, amount: float) -> str:
        if amount > self.balance:
            return f"❌ Insufficient funds. Balance: ${self.balance:.2f}"
        self.balance -= amount
        self.transactions.append(f"-${amount:.2f}")
        return f"✅ Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}"

    def __str__(self) -> str:
        return (
            f"🏦 {self.bank_name} — Account #{self.account_number}\n"
            f"   Owner: {self.owner}\n"
            f"   Balance: ${self.balance:.2f}"
        )


# ---------------------------------------------------------------------------
# 3. Static Methods and Class Methods
# ---------------------------------------------------------------------------


class MathHelper:
    """
    Demonstrates @staticmethod and @classmethod.

    @staticmethod — A function that belongs to the class but doesn't use 'self' or 'cls'.
                    Like a utility function.
    @classmethod  — A method that gets the CLASS itself (not an instance) as its first argument.
                    Used for alternative constructors.
    """

    pi = 3.14159

    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method — no access to class or instance."""
        return a + b

    @staticmethod
    def is_even(n: int) -> bool:
        return n % 2 == 0

    @classmethod
    def circle_area(cls, radius: float) -> float:
        """Class method — has access to class variables via 'cls'."""
        return cls.pi * radius ** 2


class Employee:
    """Alternative constructors using @classmethod."""

    def __init__(self, name: str, role: str, salary: float) -> None:
        self.name = name
        self.role = role
        self.salary = salary

    @classmethod
    def from_string(cls, data_string: str) -> Employee:
        """Create an Employee from a comma-separated string."""
        name, role, salary = data_string.split(",")
        return cls(name.strip(), role.strip(), float(salary.strip()))

    @classmethod
    def intern(cls, name: str) -> Employee:
        """Create an intern with default role and salary."""
        return cls(name, "Intern", 30_000)

    def __str__(self) -> str:
        return f"👤 {self.name} | {self.role} | ${self.salary:,.0f}"


# ---------------------------------------------------------------------------
# 4. Magic / Dunder Methods
# ---------------------------------------------------------------------------


class ShoppingItem:
    """
    Demonstrates special (dunder) methods.

    These methods let your objects work with Python's built-in operations:
        __str__   → print(item)
        __repr__  → repr(item)
        __eq__    → item1 == item2
        __lt__    → item1 < item2 (for sorting)
        __add__   → item1 + item2
        __len__   → len(cart)
    """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: ${self.price:.2f}"

    def __repr__(self) -> str:
        return f"ShoppingItem('{self.name}', {self.price})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ShoppingItem):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __lt__(self, other: ShoppingItem) -> bool:
        return self.price < other.price

    def __add__(self, other: ShoppingItem) -> float:
        return self.price + other.price


class ShoppingCart:
    """Cart that uses dunder methods."""

    def __init__(self) -> None:
        self.items: list[ShoppingItem] = []

    def add(self, item: ShoppingItem) -> None:
        self.items.append(item)

    def __len__(self) -> int:
        return len(self.items)

    def __contains__(self, item: ShoppingItem) -> bool:
        return item in self.items

    def __iter__(self):
        return iter(self.items)

    def __str__(self) -> str:
        if not self.items:
            return "🛒 Cart is empty"
        lines = ["🛒 Shopping Cart:"]
        for item in self.items:
            lines.append(f"   • {item}")
        total = sum(i.price for i in self.items)
        lines.append(f"   Total: ${total:.2f}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Classes & Objects demonstration."""
    print("=" * 60)
    print("  CLASSES AND OBJECTS — OOP Foundation")
    print("=" * 60)

    # --- Basic Class ---
    print("\n🐕 1. Basic Class & Object")
    print("-" * 40)
    buddy = Dog("Buddy", "Golden Retriever", 3)
    max_dog = Dog("Max", "German Shepherd", 5)

    print(f"  {buddy}")
    print(f"  {max_dog}")
    print(f"  {buddy.bark()}")
    print(f"  {buddy.birthday()}")
    print(f"  Species (class var): {Dog.species}")
    print(f"  buddy is max? {buddy is max_dog}")  # False — different objects!

    # --- Class vs Instance Variables ---
    print("\n\n🏦 2. Class vs Instance Variables")
    print("-" * 40)
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 500)

    print(f"  {acc1}")
    print(f"  {acc1.deposit(200)}")
    print(f"  {acc1.withdraw(50)}")
    print(f"\n  {acc2}")
    print(f"  Total accounts: {BankAccount.total_accounts}")

    # --- Static & Class Methods ---
    print("\n\n🔧 3. Static & Class Methods")
    print("-" * 40)
    print(f"  MathHelper.add(3, 7) = {MathHelper.add(3, 7)}")
    print(f"  MathHelper.is_even(4) = {MathHelper.is_even(4)}")
    print(f"  Circle area (r=5) = {MathHelper.circle_area(5):.2f}")

    emp1 = Employee.from_string("Alice, Senior Dev, 120000")
    emp2 = Employee.intern("Bob")
    print(f"  {emp1}")
    print(f"  {emp2}")

    # --- Dunder Methods ---
    print("\n\n✨ 4. Magic / Dunder Methods")
    print("-" * 40)
    apple = ShoppingItem("Apple", 1.50)
    banana = ShoppingItem("Banana", 0.75)
    laptop = ShoppingItem("Laptop", 999.99)

    print(f"  str: {apple}")
    print(f"  repr: {repr(apple)}")
    print(f"  apple == apple? {apple == ShoppingItem('Apple', 1.50)}")
    print(f"  apple < laptop? {apple < laptop}")
    print(f"  apple + banana = ${apple + banana:.2f}")

    cart = ShoppingCart()
    cart.add(apple)
    cart.add(banana)
    cart.add(laptop)
    print(f"\n  len(cart) = {len(cart)}")
    print(f"  apple in cart? {apple in cart}")
    print(f"\n{cart}")


if __name__ == "__main__":
    demo()
