# 🏛️ SOLID Principles — 5 Rules for Clean OOP Design

## What Is SOLID?

SOLID is an acronym for **5 principles** that help you write code that's easy to maintain, extend, and test. These are the **foundation** of all design patterns.

### 🏠 Think of It Like This (For a 10-Year-Old)

SOLID is like the **rules for building a good LEGO house**:
- Each piece has ONE job (S)
- You can add rooms without breaking the house (O)
- Any door should work in any doorframe (L)
- Don't give a piece more holes than it needs (I)
- Pieces connect through standard connectors, not glue (D)

---

## The 5 Principles

### 📌 S — Single Responsibility Principle (SRP)

> **A class should have only ONE reason to change.**

**Analogy:** A chef cooks food. A waiter serves food. A cashier handles payments. You don't want ONE person doing ALL three!

```python
# ❌ BAD: One class does everything
class UserManager:
    def validate(self): ...    # Validation
    def save_to_db(self): ...  # Database
    def send_email(self): ...  # Email

# ✅ GOOD: Each class has ONE job
class UserValidator: ...       # Only validates
class UserRepository: ...     # Only saves/loads
class EmailSender: ...        # Only sends emails
```

---

### 📌 O — Open/Closed Principle (OCP)

> **Open for extension, closed for modification.**

**Analogy:** A phone can install new apps (extension) without changing the operating system (modification).

```python
# ❌ BAD: Must modify function for each new shape
def calculate_area(shape_type, **kwargs):
    if shape_type == "circle": ...
    elif shape_type == "rectangle": ...
    # Adding triangle means CHANGING this function!

# ✅ GOOD: Add new shapes without touching existing code
class Shape(ABC):
    @abstractmethod
    def area(self): ...

class Circle(Shape): ...     # New shape = new class
class Triangle(Shape): ...   # No existing code changed!
```

---

### 📌 L — Liskov Substitution Principle (LSP)

> **Child classes must be substitutable for parent classes.**

**Analogy:** If you order a "car" and they give you a Tesla, Civic, or BMW, all should DRIVE the same way. A "car" that can't be driven breaks expectations!

```python
# ❌ BAD: Penguin inherits fly() but can't fly!
class Bird:
    def fly(self): return "Flying!"

class Penguin(Bird):
    def fly(self): raise Error("Can't fly!")  # 💥 Breaks!

# ✅ GOOD: Separate capabilities
class FlyingBird(Bird): ...
class SwimmingBird(Bird): ...
```

---

### 📌 I — Interface Segregation Principle (ISP)

> **Don't force a class to implement methods it doesn't need.**

**Analogy:** A printer shouldn't be forced to have a scanner feature. Keep interfaces small and focused.

```python
# ❌ BAD: Simple printer FORCED to implement scan and fax
class Machine(ABC):
    def print(self): ...
    def scan(self): ...
    def fax(self): ...

# ✅ GOOD: Small, focused interfaces
class Printer(ABC):
    def print(self): ...

class Scanner(ABC):
    def scan(self): ...

class SimplePrinter(Printer): ...           # Only prints
class MultiFunctionDevice(Printer, Scanner): ...  # Prints AND scans
```

---

### 📌 D — Dependency Inversion Principle (DIP)

> **Depend on abstractions, not concretions.**

**Analogy:** A lamp plugs into a standard socket. The lamp doesn't know about the power plant, and the power plant doesn't know about the lamp. Both depend on the **plug/socket standard** (abstraction).

```python
# ❌ BAD: Hardcoded dependency
class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # 💥 Locked to MySQL!

# ✅ GOOD: Depend on abstraction
class UserService:
    def __init__(self, db: Database):  # Any database works!
        self.db = db

# Swap databases easily!
service = UserService(PostgreSQLDatabase())
service = UserService(InMemoryDatabase())  # Great for testing!
```

---

## Quick Reference Table

| Principle | Rule | One-Line Summary |
|-----------|------|-----------------|
| **S** | Single Responsibility | One class, one job |
| **O** | Open/Closed | Extend, don't modify |
| **L** | Liskov Substitution | Children should work like parents |
| **I** | Interface Segregation | Small interfaces > fat interfaces |
| **D** | Dependency Inversion | Depend on abstractions |

---

## Why Learn This?

SOLID principles are the **DNA of design patterns**:

| Principle | Related Patterns |
|-----------|-----------------|
| **S** | Facade, Repository, MVC |
| **O** | Strategy, Decorator, Observer |
| **L** | Factory, Template Method |
| **I** | Adapter, Proxy |
| **D** | Dependency Injection, Factory, Strategy |

**If you understand SOLID, design patterns will click naturally!**

---

## Run the Example

```bash
uv run python -m src.oops_concepts.solid_principles
```
