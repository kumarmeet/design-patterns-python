# 🧠 Strategy Pattern

## What Is It? (Explain Like I'm 10)

Imagine you want to go to school. You can:
- 🚗 Drive (fast but expensive)
- 🚌 Take the bus (cheap but slow)
- 🚲 Ride a bike (free but tiring)

The **destination is the same**, but the **strategy** (how you get there) is different. You can **switch strategies** any day you want!

That's the Strategy pattern — swappable algorithms for the same problem.

---

## 📖 Simple Definition

> The Strategy pattern defines a **family of algorithms**, encapsulates each one, and makes them **interchangeable**. The algorithm can be selected at runtime without modifying the client code.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🚗🚌🚲 Getting to School | Same destination, different travel methods |
| 💳🏦📱 Paying a Bill | Cash, credit card, or mobile payment |
| 📊 Sorting a List | Alphabetical, by price, by date, by popularity |
| 🎮 Game Difficulty | Easy, Medium, Hard — same game, different rules |

---

## ✅ When to Use

- **Multiple ways to do the same thing** — Sorting, filtering, pricing, discounts
- **Business rules that change often** — Discount strategies, tax calculations
- **Removing complex if/else chains** — Instead of 10 `if` statements, use 10 strategies
- **A/B testing** — Try different algorithms and compare results
- **Payment processing** — Different payment methods with the same checkout flow

---

## ❌ When NOT to Use

- **When there's only one algorithm** — No need for strategy if there's only one way
- **When the algorithm never changes** — If it's always the same, hardcode it
- **When clients don't need to choose** — If the choice is automatic, a simple factory is enough

---

## 🔧 How It Works

```
ShoppingCart
    │
    ├── set_discount_strategy(NoDiscount)      → $125.96
    ├── set_discount_strategy(Percentage(20%))  → $100.77
    ├── set_discount_strategy(BlackFriday)      → $75.58
    └── set_discount_strategy(FlatDiscount(15)) → $110.96

Same cart, same items — different strategy = different price!
```

---

## 💻 Code Example

```python
from design_patterns.behavioral.strategy import (
    ShoppingCart, CartItem,
    PercentageDiscount, FlatDiscount, SeasonalDiscount
)

cart = ShoppingCart()
cart.add_item(CartItem("Headphones", 79.99))
cart.add_item(CartItem("Phone Case", 19.99))

# Switch strategies at runtime!
cart.set_discount_strategy(PercentageDiscount(20))
print(f"20% off: ${cart.get_total():.2f}")

cart.set_discount_strategy(FlatDiscount(15))
print(f"$15 off: ${cart.get_total():.2f}")

cart.set_discount_strategy(SeasonalDiscount("black_friday"))
print(f"Black Friday: ${cart.get_total():.2f}")
```

---

## 🆚 Strategy vs If/Else

```python
# ❌ WITHOUT Strategy (hard to maintain)
if discount_type == "percentage":
    total = price * 0.8
elif discount_type == "flat":
    total = price - 15
elif discount_type == "bogo":
    total = price * 0.5
# Adding new discount = modifying this code!

# ✅ WITH Strategy (clean and extensible)
cart.set_discount_strategy(my_strategy)
total = cart.get_total()
# Adding new discount = create a new strategy class!
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Interchangeable algorithms |
| **Key Benefit** | Eliminates complex conditionals, easy to add new algorithms |
| **Key Risk** | Over-engineering for simple cases |
| **Use When** | Multiple algorithms for the same problem |
| **Avoid When** | Only one algorithm exists |
