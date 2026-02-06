# 🎭 Polymorphism — Same Interface, Different Behavior

## What Is It?

**"Poly"** = many, **"morph"** = forms. Polymorphism means ONE interface can work with MANY different types of objects.

### 📺 Think of It Like This (For a 10-Year-Old)

Imagine a **universal remote control**. It has a "PLAY" button:
- Press it on a **DVD player** → plays a movie
- Press it on a **music player** → plays a song
- Press it on a **game console** → starts a game

**Same button**, **different behavior** depending on the device. That's polymorphism!

---

## Types of Polymorphism in Python

### 1. **Method Overriding** (Runtime Polymorphism)
Different classes implement the same method differently.

```python
class Circle:
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def area(self):
        return self.width * self.height

# Same method name, different calculation!
shapes = [Circle(5), Rectangle(10, 6)]
for shape in shapes:
    print(shape.area())  # Each calculates differently
```

### 2. **Duck Typing** (Python's Superpower)
> "If it walks like a duck and quacks like a duck, it IS a duck."

Python doesn't check the TYPE — it checks if the METHOD exists.

```python
class Duck:
    def quack(self): return "Quack!"

class Person:
    def quack(self): return "I'm quacking like a duck!"

# Both work because both have quack()!
for thing in [Duck(), Person()]:
    print(thing.quack())
```

### 3. **Operator Overloading**
Make `+`, `-`, `==`, `<` work with YOUR objects.

```python
class Money:
    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __gt__(self, other):
        return self.amount > other.amount

price = Money(29.99)
tax = Money(5.40)
total = price + tax  # Uses __add__!
```

---

## Why Learn This?

Polymorphism is the **heart** of design patterns! Nearly every pattern uses it:
- **Strategy** — swap algorithms at runtime
- **Factory** — create different objects through one interface
- **Observer** — notify different listeners through the same method
- **Command** — execute different commands through `execute()`

Without polymorphism, you'd need endless `if/elif/else` chains!

---

## When to Use

✅ When you want to **write code that works with multiple types** without knowing the specific type
✅ When you need to **add new types later** without changing existing code
✅ When you want to **eliminate long if/elif chains** that check types

## When NOT to Use

❌ When there's only ONE type — polymorphism adds unnecessary complexity
❌ When types don't share a meaningful common interface
❌ Don't use duck typing if type safety is critical (consider `ABC` instead)

---

## Run the Example

```bash
uv run python -m src.oops_concepts.polymorphism
```
