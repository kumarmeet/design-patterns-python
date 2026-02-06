# 🧩 Composition vs Inheritance — "Has-A" vs "Is-A"

## What Is It?

**Composition** means building complex objects by **combining simpler objects**. Instead of saying "A IS A B" (inheritance), you say "A HAS A B" (composition).

### 🧱 Think of It Like This (For a 10-Year-Old)

Think of **LEGO**!
- **Inheritance** is like being born: "I AM my parents' child." You can't choose your parents.
- **Composition** is like building with LEGO: "I HAVE these pieces." You can snap on and swap out pieces anytime!

A robot built with LEGO:
- Snap on **legs** → it can walk
- Snap on **propellers** → it can fly
- Remove legs, add **fins** → now it can swim!

You don't need a new robot for each combination — just swap the parts!

---

## Inheritance vs Composition

| | Inheritance ("Is-A") | Composition ("Has-A") |
|---|---|---|
| **Relationship** | Dog IS AN Animal | Car HAS AN Engine |
| **Coupling** | Tight (hard to change) | Loose (easy to swap) |
| **Flexibility** | Fixed at design time | Changeable at runtime |
| **Reuse** | Reuse by extending | Reuse by combining |
| **Example** | `class Dog(Animal)` | `self.engine = Engine()` |

---

## The Problem with Inheritance

Imagine building robots with different abilities using **inheritance**:

```python
class Walker: ...
class Swimmer: ...
class Flyer: ...
class WalkingSwimmer(Walker, Swimmer): ...
class WalkingFlyer(Walker, Flyer): ...
class SwimmingFlyer(Swimmer, Flyer): ...
class WalkingSwimmingFlyer(Walker, Swimmer, Flyer): ...
# 😱 CLASS EXPLOSION! And adding "Climber" makes it WORSE!
```

## The Solution with Composition

```python
class Robot:
    def __init__(self, name):
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)

robot = Robot("Explorer")
robot.add_ability(WalkAbility())
robot.add_ability(FlyAbility())
# Easy! Add or remove abilities anytime!
```

---

## Real-World Examples

### Computer System
```python
class Computer:
    def __init__(self, cpu, ram, storage, gpu=None):
        self.cpu = cpu          # HAS A CPU
        self.ram = ram          # HAS RAM
        self.storage = storage  # HAS storage
        self.gpu = gpu          # optionally HAS a GPU
```
Upgrade the RAM without replacing the whole computer!

### Notification System
```python
# Instead of: EmailHTMLNotification, EmailPlainNotification,
#             SMSHTMLNotification, SMSPlainNotification... 😱

class NotificationService:
    def __init__(self, formatter, sender):
        self.formatter = formatter   # HAS A formatter
        self.sender = sender         # HAS A sender

# Mix and match ANY formatter with ANY sender!
service = NotificationService(HTMLFormatter(), EmailSender())
```

---

## The Golden Rule

> **Favor composition over inheritance.**

Use inheritance for true "is-a" relationships.
Use composition for "has-a" or "can-do" relationships.

---

## Why Learn This?

Almost all design patterns **prefer composition over inheritance**:
- **Strategy** — compose algorithms
- **Decorator** — compose additional behavior
- **Observer** — compose listeners
- **Builder** — compose complex objects step by step
- **Dependency Injection** — compose dependencies

---

## When to Use Composition

✅ When the relationship is **"has-a"** (Car HAS AN Engine)
✅ When you need to **swap parts at runtime** (change the strategy, add abilities)
✅ When you want **loose coupling** between components
✅ When there are **many combinations** of features

## When to Use Inheritance Instead

✅ When the relationship is truly **"is-a"** (Dog IS AN Animal)
✅ When you need **polymorphism** (treat different types the same way)
✅ When the class hierarchy is **shallow** (1-2 levels deep)

---

## Run the Example

```bash
uv run python -m src.oops_concepts.composition
```
