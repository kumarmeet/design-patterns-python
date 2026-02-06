# 🎭 Abstraction — Hiding Complexity

## What Is It?

Abstraction means showing only the **essential features** and **hiding the implementation details**. Users interact with a simple interface without knowing the complex stuff happening behind the scenes.

### 🚗 Think of It Like This (For a 10-Year-Old)

When you drive a car:
- You use the **steering wheel**, **gas pedal**, and **brake** (simple interface)
- You **DON'T** need to know how the engine, transmission, or fuel injection works (hidden complexity)

The car **abstracts away** all that complexity behind a simple interface!

---

## How It Works in Python

Python uses **Abstract Base Classes (ABC)** from the `abc` module:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Every shape MUST implement this."""
        ...

    @abstractmethod
    def perimeter(self):
        """Every shape MUST implement this."""
        ...
```

### Rules:
1. **Cannot be instantiated** — `Shape()` raises `TypeError`!
2. **Subclasses MUST implement** all `@abstractmethod` methods
3. **Can have concrete methods** that are shared by all subclasses

---

## Key Concepts

### 1. **Abstract Classes**
Define WHAT to do, not HOW to do it.

```python
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self): ...

    @abstractmethod
    def execute(self, query): ...

    # Concrete method — shared by ALL
    def health_check(self):
        return self.execute("SELECT 1")
```

### 2. **Multiple Interfaces**
A class can implement multiple abstract classes:

```python
class Report(Printable, Saveable, Exportable):
    # Must implement ALL abstract methods from ALL three!
    ...
```

### 3. **Abstract + Concrete Methods**
Abstract classes can have BOTH abstract AND regular methods:
- **Abstract methods**: Subclass MUST override
- **Concrete methods**: Shared default behavior

---

## Why Learn This?

Abstraction is the **backbone** of design patterns:
- **Factory Pattern** — returns abstract types
- **Strategy Pattern** — defines abstract algorithm interface
- **Template Method** — abstract steps in a concrete template
- **Observer** — abstract listener interface
- **Dependency Injection** — depends on abstractions, not concretions

---

## When to Use

✅ When you want to **define a contract** that all subclasses must follow
✅ When you need a **common interface** for different implementations
✅ When you want to **decouple** code from specific implementations
✅ When building **frameworks** or **libraries** where others provide implementations

## When NOT to Use

❌ When you only have ONE implementation — abstraction adds unnecessary complexity
❌ For simple scripts or utilities — keep it simple
❌ When the interface is likely to change frequently — abstract classes are hard to modify once subclasses depend on them

---

## Run the Example

```bash
uv run python -m src.oops_concepts.abstraction
```
