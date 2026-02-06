# 🧱 Decorator Pattern

## What Is It? (Explain Like I'm 10)

Imagine you have a **plain ice cream cone** 🍦. You can add **chocolate sauce**, then **sprinkles**, then **whipped cream** on top. Each layer ADDS something new, but the ice cream underneath stays the same.

That's the Decorator pattern! You **wrap** an object with extra features, like adding layers to an ice cream cone.

---

## 📖 Simple Definition

> The Decorator pattern adds **new behavior** to objects dynamically by wrapping them in decorator objects. Each decorator adds one specific behavior without changing the original object.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🍦 Ice Cream Toppings | Plain cone → add chocolate → add sprinkles → add cherry |
| ☕ Coffee Add-ons | Basic coffee → add milk → add sugar → add whipped cream |
| 🎁 Gift Wrapping | Gift → wrapping paper → ribbon → bow |
| 🧅 Onion Layers | Each layer wraps around the previous one |

---

## ✅ When to Use

- **Middleware in web frameworks** — Logging → Auth → Rate Limiting → Handler
- **Stream processing** — FileStream → BufferedStream → EncryptedStream
- **Feature toggles** — Enable/disable features by adding/removing decorators
- **Logging and monitoring** — Wrap any service with logging without changing it
- **Data transformation** — Compress → Encrypt → Encode data

---

## ❌ When NOT to Use

- **When you need to remove a specific layer** — Decorators are stacked; removing a middle one is hard
- **When order matters a lot** — The stacking order can cause confusing behavior
- **Too many small decorators** — Makes debugging difficult (where did this behavior come from?)
- **When inheritance is simpler** — If you only need one variation, subclassing is cleaner

---

## 🔧 How It Works

```
coffee = BasicCoffee()                    → "Basic Coffee" = $2.00

coffee = MilkDecorator(coffee)            → "Basic Coffee + Milk" = $2.50

coffee = SugarDecorator(coffee)           → "Basic Coffee + Milk + Sugar" = $2.75

coffee = WhippedCreamDecorator(coffee)    → "Basic Coffee + Milk + Sugar + Whipped Cream" = $3.50

Each decorator WRAPS the previous one and adds its own behavior.
```

---

## 💻 Code Example

```python
from design_patterns.structural.decorator import (
    BasicCoffee, MilkDecorator, SugarDecorator, WhippedCreamDecorator
)

# Start with basic coffee
coffee = BasicCoffee()

# Add toppings (decorators)
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
coffee = WhippedCreamDecorator(coffee)

print(coffee.get_description())  # "Basic Coffee + Milk + Sugar + Whipped Cream"
print(f"${coffee.get_cost():.2f}")  # "$3.50"
```

---

## 🆚 Decorator vs Inheritance

| Feature | Decorator | Inheritance |
|---------|-----------|-------------|
| Adds behavior | At runtime | At compile time |
| Combinations | Mix and match freely | Need a class for each combo |
| Flexibility | ✅ Very flexible | ❌ Rigid |
| Complexity | Can be confusing with many layers | Simple with few variants |

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Structural |
| **Intent** | Add behavior dynamically without modifying objects |
| **Key Benefit** | Flexible feature composition |
| **Key Risk** | Too many layers = hard to debug |
| **Use When** | Adding optional features in various combinations |
| **Avoid When** | You need simple, static behavior |
