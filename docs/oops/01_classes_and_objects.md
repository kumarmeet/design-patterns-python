# 🏗️ Classes and Objects — The Foundation of OOP

## What Are They?

A **class** is a **blueprint** — a template that describes what something looks like and what it can do.

An **object** is a **real thing** built from that blueprint.

### 🍪 Think of It Like This (For a 10-Year-Old)

Imagine you have a **cookie cutter** (that's the class). Every time you press it into dough, you get a **cookie** (that's the object). One cookie cutter can make MANY cookies, and each cookie can have different toppings!

```
Cookie Cutter (CLASS)  →  Cookie 1 (OBJECT): chocolate chips
                       →  Cookie 2 (OBJECT): sprinkles
                       →  Cookie 3 (OBJECT): plain
```

---

## Key Concepts

### 1. **Instance Variables** (Unique to each object)
Every dog has its own name, breed, and age.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name      # Each dog has its OWN name
        self.breed = breed
        self.age = age

buddy = Dog("Buddy", "Golden Retriever", 3)
max_dog = Dog("Max", "German Shepherd", 5)
# buddy.name = "Buddy", max_dog.name = "Max" — different!
```

### 2. **Class Variables** (Shared by ALL objects)
ALL dogs are the same species.

```python
class Dog:
    species = "Canis familiaris"  # Shared by ALL dogs
```

### 3. **Methods** (What objects can DO)
```python
def bark(self):
    return f"{self.name} says: Woof!"
```

### 4. **`__init__`** (The Constructor)
Called automatically when you create a new object. It sets up the initial state.

### 5. **`self`**
Refers to the **specific object** calling the method. When `buddy.bark()` runs, `self` is `buddy`.

### 6. **Static Methods & Class Methods**
- `@staticmethod` — A utility function in the class. No `self` or `cls`.
- `@classmethod` — Gets the class itself (`cls`), often used for alternative constructors.

### 7. **Magic (Dunder) Methods**
Special methods that let your objects work with Python's built-in features:

| Method | What It Does | Example |
|--------|-------------|---------|
| `__str__` | `print(obj)` | "Buddy the dog" |
| `__repr__` | `repr(obj)` | "Dog('Buddy', 'Retriever', 3)" |
| `__eq__` | `obj1 == obj2` | Compare two dogs |
| `__lt__` | `obj1 < obj2` | Sort objects |
| `__len__` | `len(obj)` | Length of a collection |
| `__add__` | `obj1 + obj2` | Add two objects |

---

## Why Learn This?

Classes and objects are the **building blocks** of everything in OOP. Every design pattern you'll learn uses classes and objects. If you don't understand this, nothing else will make sense!

---

## When to Use

✅ **Always** — everything in Python is an object. Use classes when you need to model real-world things with attributes and behaviors.

## When NOT to Use

❌ For simple scripts that just run a few lines of code, you don't need a class. A plain function is fine!

---

## Run the Example

```bash
uv run python -m src.oops_concepts.classes_and_objects
```
