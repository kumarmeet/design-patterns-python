# 🧬 Inheritance — Reusing and Extending Code

## What Is It?

Inheritance lets a new class (**child**) get all the features of an existing class (**parent**), and then add or modify its own features.

### 👨‍👩‍👧 Think of It Like This (For a 10-Year-Old)

You inherit features from your parents — maybe your mom's eye color or your dad's height. But you also have your **OWN unique qualities** — like your favorite hobby.

In programming:
- A **Dog** class inherits from an **Animal** class.
- All animals have a name and can make a sound.
- But a Dog specifically barks, and a Cat specifically meows.

```
        Animal (Parent)
       /       \
    Dog         Cat (Children)
   barks       meows
```

---

## Types of Inheritance

### 1. **Single Inheritance**
One child, one parent.
```python
class Animal:
    def speak(self): ...

class Dog(Animal):       # Dog inherits from Animal
    def speak(self):
        return "Woof!"
```

### 2. **Multi-Level Inheritance**
Grandparent → Parent → Child
```python
class Vehicle:           # Grandparent
    ...

class Car(Vehicle):      # Parent
    ...

class ElectricCar(Car):  # Child
    ...
```

### 3. **Multiple Inheritance**
One child, multiple parents.
```python
class Flyer: ...
class Swimmer: ...

class Duck(Flyer, Swimmer):   # Duck can fly AND swim
    ...
```

---

## Key Concepts

### `super()`
Calls the parent's method. Essential for extending (not replacing) behavior.
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent's __init__
        self.breed = breed       # Add new attribute
```

### Method Overriding
Child provides its OWN version of a parent method.
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):        # OVERRIDES parent's speak()
        return "Woof!"
```

### `isinstance()` and `issubclass()`
```python
isinstance(dog, Animal)      # True — dog IS an Animal
issubclass(Dog, Animal)      # True — Dog IS a subclass of Animal
```

### Method Resolution Order (MRO)
When using multiple inheritance, Python follows a specific order to find methods:
```python
class D(B, C):  # MRO: D → B → C → A
    ...
print(D.__mro__)  # Shows the order
```

---

## Why Learn This?

Inheritance is used in almost EVERY design pattern. The **Template Method**, **Strategy**, **Factory**, and **Observer** patterns all rely on inheritance. Understanding it is essential!

---

## When to Use

✅ When there's a true **"is-a"** relationship (Dog IS AN Animal)
✅ When you want to **share common code** across related classes
✅ When you need **polymorphism** (different classes, same interface)

## When NOT to Use

❌ When the relationship is **"has-a"** (Car HAS AN Engine) — use **Composition** instead
❌ When the inheritance tree gets too deep (3+ levels is a warning sign)
❌ When you're inheriting just to reuse code, not because of a real "is-a" relationship
❌ Avoid multiple inheritance unless you really need it — it can get confusing

---

## Run the Example

```bash
uv run python -m src.oops_concepts.inheritance
```
