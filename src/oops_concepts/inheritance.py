"""
Inheritance — Reusing and Extending Code
==========================================
Inheritance lets a new class (child) get all the features of an
existing class (parent), and then add or modify its own.

Real-World Analogy:
    You inherit features from your parents — eye color, height.
    But you also have your OWN unique qualities.
    A child class "inherits" from a parent class the same way.
"""

from __future__ import annotations

from datetime import datetime


# ---------------------------------------------------------------------------
# 1. Basic Inheritance
# ---------------------------------------------------------------------------


class Animal:
    """
    Parent (Base) class — every animal has a name and can make sounds.

    Real-life analogy:
        "Animal" is a general category. It defines what ALL animals have in common.
        Every animal has a name and can make a sound — but the specific sound
        depends on the type of animal.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def speak(self) -> str:
        return f"{self.name} makes a sound"

    def describe(self) -> str:
        return f"🐾 {self.name}, age {self.age}"

    def __str__(self) -> str:
        return self.describe()


class Dog(Animal):
    """Child class — inherits from Animal, adds dog-specific features."""

    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)  # Call parent's __init__
        self.breed = breed

    def speak(self) -> str:
        """Override: Dogs bark instead of generic sound."""
        return f"🐕 {self.name} says: Woof! Woof!"

    def fetch(self, item: str) -> str:
        """New method — only dogs can fetch."""
        return f"🐕 {self.name} fetches the {item}!"

    def describe(self) -> str:
        return f"🐕 {self.name}, {self.breed}, age {self.age}"


class Cat(Animal):
    """Child class — inherits from Animal, adds cat-specific features."""

    def __init__(self, name: str, age: int, indoor: bool = True) -> None:
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self) -> str:
        return f"🐱 {self.name} says: Meow!"

    def purr(self) -> str:
        return f"🐱 {self.name} is purring... prrrrr"


class Bird(Animal):
    """Child class — adds flying ability."""

    def __init__(self, name: str, age: int, can_fly: bool = True) -> None:
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self) -> str:
        return f"🐦 {self.name} says: Tweet tweet!"

    def fly(self) -> str:
        if self.can_fly:
            return f"🐦 {self.name} is flying high!"
        return f"🐧 {self.name} can't fly, but can swim!"


# ---------------------------------------------------------------------------
# 2. Multi-Level Inheritance
# ---------------------------------------------------------------------------


class Vehicle:
    """Grandparent class."""

    def __init__(self, brand: str, year: int) -> None:
        self.brand = brand
        self.year = year

    def start(self) -> str:
        return f"🚗 {self.brand} engine started"

    def __str__(self) -> str:
        return f"{self.brand} ({self.year})"


class Car(Vehicle):
    """Parent class — inherits from Vehicle."""

    def __init__(self, brand: str, year: int, doors: int = 4) -> None:
        super().__init__(brand, year)
        self.doors = doors

    def honk(self) -> str:
        return f"🚗 {self.brand}: Beep beep!"


class ElectricCar(Car):
    """
    Child class — inherits from Car, which inherits from Vehicle.
    This is MULTI-LEVEL inheritance: ElectricCar → Car → Vehicle.
    """

    def __init__(self, brand: str, year: int, battery_kwh: int) -> None:
        super().__init__(brand, year)
        self.battery_kwh = battery_kwh

    def start(self) -> str:
        """Override: Electric cars are silent!"""
        return f"⚡ {self.brand} silently powers on"

    def charge(self) -> str:
        return f"🔋 {self.brand}: Charging {self.battery_kwh} kWh battery..."


# ---------------------------------------------------------------------------
# 3. Method Resolution Order (MRO) & super()
# ---------------------------------------------------------------------------


class A:
    def greet(self) -> str:
        return "Hello from A"


class B(A):
    def greet(self) -> str:
        return "Hello from B"


class C(A):
    def greet(self) -> str:
        return "Hello from C"


class D(B, C):
    """
    Multiple inheritance — D inherits from BOTH B and C.
    Python uses MRO (Method Resolution Order) to decide which method to call.
    MRO for D: D → B → C → A
    """
    pass


# ---------------------------------------------------------------------------
# 4. Real-World Example: Employee Hierarchy
# ---------------------------------------------------------------------------


class Employee:
    """Base employee class."""

    def __init__(self, name: str, employee_id: str, base_salary: float) -> None:
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.hire_date = datetime.now().strftime("%Y-%m-%d")

    def calculate_pay(self) -> float:
        """Base pay calculation."""
        return self.base_salary

    def get_role(self) -> str:
        return "Employee"

    def __str__(self) -> str:
        return f"👤 {self.name} ({self.get_role()}) — ${self.calculate_pay():,.2f}/year"


class Developer(Employee):
    """Developer with tech stack bonus."""

    def __init__(self, name: str, employee_id: str, base_salary: float,
                 tech_stack: list[str] | None = None) -> None:
        super().__init__(name, employee_id, base_salary)
        self.tech_stack = tech_stack or []

    def calculate_pay(self) -> float:
        # Bonus for each technology skill
        skill_bonus = len(self.tech_stack) * 2000
        return self.base_salary + skill_bonus

    def get_role(self) -> str:
        return "Developer"

    def code(self, feature: str) -> str:
        return f"💻 {self.name} is coding: {feature}"


class Manager(Employee):
    """Manager with team bonus."""

    def __init__(self, name: str, employee_id: str, base_salary: float) -> None:
        super().__init__(name, employee_id, base_salary)
        self.team: list[Employee] = []

    def add_to_team(self, employee: Employee) -> None:
        self.team.append(employee)

    def calculate_pay(self) -> float:
        # Bonus for managing people
        management_bonus = len(self.team) * 5000
        return self.base_salary + management_bonus

    def get_role(self) -> str:
        return f"Manager (team of {len(self.team)})"


class SeniorDeveloper(Developer):
    """Senior developer — multi-level inheritance from Developer → Employee."""

    def __init__(self, name: str, employee_id: str, base_salary: float,
                 tech_stack: list[str] | None = None,
                 mentees: int = 0) -> None:
        super().__init__(name, employee_id, base_salary, tech_stack)
        self.mentees = mentees

    def calculate_pay(self) -> float:
        base = super().calculate_pay()  # Get Developer's calculation
        mentee_bonus = self.mentees * 3000
        return base + mentee_bonus

    def get_role(self) -> str:
        return "Senior Developer"

    def mentor(self, junior_name: str) -> str:
        return f"🎓 {self.name} is mentoring {junior_name}"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Inheritance demonstration."""
    print("=" * 60)
    print("  INHERITANCE — Reusing and Extending Code")
    print("=" * 60)

    # --- Basic Inheritance ---
    print("\n🐾 1. Basic Inheritance")
    print("-" * 40)
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 5)
    bird = Bird("Tweety", 2)
    penguin = Bird("Pingu", 4, can_fly=False)

    animals: list[Animal] = [dog, cat, bird, penguin]
    for animal in animals:
        print(f"  {animal.describe()}")
        print(f"    {animal.speak()}")

    print(f"\n  Dog-only: {dog.fetch('ball')}")
    print(f"  Cat-only: {cat.purr()}")
    print(f"  Bird-only: {bird.fly()}")
    print(f"  Penguin: {penguin.fly()}")

    # --- isinstance and issubclass ---
    print(f"\n  isinstance(dog, Animal)? {isinstance(dog, Animal)}")  # True
    print(f"  isinstance(dog, Dog)? {isinstance(dog, Dog)}")  # True
    print(f"  isinstance(dog, Cat)? {isinstance(dog, Cat)}")  # False
    print(f"  issubclass(Dog, Animal)? {issubclass(Dog, Animal)}")  # True

    # --- Multi-Level Inheritance ---
    print("\n\n🚗 2. Multi-Level Inheritance")
    print("-" * 40)
    tesla = ElectricCar("Tesla Model 3", 2024, 75)
    print(f"  {tesla}")
    print(f"  {tesla.start()}")    # ElectricCar's version
    print(f"  {tesla.honk()}")     # Inherited from Car
    print(f"  {tesla.charge()}")   # ElectricCar's own method

    # --- MRO ---
    print("\n\n🔍 3. Method Resolution Order (MRO)")
    print("-" * 40)
    d = D()
    print(f"  d.greet() = {d.greet()}")  # "Hello from B" (B comes first in MRO)
    print(f"  MRO: {[cls.__name__ for cls in D.__mro__]}")

    # --- Employee Hierarchy ---
    print("\n\n👔 4. Employee Hierarchy")
    print("-" * 40)
    dev = Developer("Alice", "DEV-001", 100_000, ["Python", "React", "Docker"])
    senior = SeniorDeveloper("Bob", "DEV-002", 130_000, ["Python", "Go", "K8s", "AWS"], mentees=3)
    mgr = Manager("Charlie", "MGR-001", 120_000)
    mgr.add_to_team(dev)
    mgr.add_to_team(senior)

    employees: list[Employee] = [dev, senior, mgr]
    for emp in employees:
        print(f"  {emp}")

    print(f"\n  {dev.code('user authentication')}")
    print(f"  {senior.mentor('Alice')}")


if __name__ == "__main__":
    demo()
