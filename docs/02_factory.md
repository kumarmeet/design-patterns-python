# 🏭 Factory Method Pattern

## What Is It? (Explain Like I'm 10)

Imagine you go to a **pizza restaurant** and tell the waiter: "I want a Margherita pizza." You don't go into the kitchen to make it yourself. The kitchen (factory) knows the recipe and makes it for you.

That's the Factory pattern! You say **WHAT** you want, and the factory figures out **HOW** to make it.

---

## 📖 Simple Definition

> The Factory Method pattern creates objects without exposing the creation logic to the client. The client specifies WHAT it needs, and the factory decides WHICH class to instantiate.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🍕 Pizza Restaurant | You order "Margherita" — the kitchen knows the recipe |
| 🏭 Car Factory | You order a "sedan" — the factory builds the right model |
| 📮 Post Office | You say "send a package" — they pick the right shipping method |
| 🎮 Game Character Select | You pick "Warrior" — the game creates the right character with stats |

---

## ✅ When to Use

- **Payment Processing** — Different payment methods (Credit Card, UPI, PayPal) but same interface
- **Notification Service** — Send via Email, SMS, or Push — pick one at runtime
- **File Parsers** — Parse PDF, CSV, JSON — the factory picks the right parser
- **Database Connections** — Connect to MySQL, PostgreSQL, or MongoDB based on config
- **UI Component Libraries** — Create buttons, inputs for different themes

---

## ❌ When NOT to Use

- **When there's only one type** — If you'll never have variants, a factory adds unnecessary complexity
- **Simple object creation** — If `MyClass()` is enough, don't wrap it in a factory
- **When types are known at compile time** — If you always know the exact class, just use it directly

---

## 🔧 How It Works

```
Client                    Factory                   Products
  │                         │                         │
  │  "credit_card"          │                         │
  ├────────────────────────►│                         │
  │                         │  Creates                │
  │                         ├────────────────────────►│ CreditCardProcessor
  │                         │                         │
  │  ◄─────────────────────┤  Returns instance        │
  │  processor.charge()     │                         │
```

---

## 💻 Code Example

```python
from design_patterns.creational.factory import PaymentFactory, PaymentMethod

# You just say WHAT you need — the factory handles the rest
processor = PaymentFactory.create(PaymentMethod.CREDIT_CARD)
result = processor.process_payment(99.99)
print(result.message)  # "Credit card charged USD 99.99"

# Switch to PayPal? Just change the argument!
paypal = PaymentFactory.create(PaymentMethod.PAYPAL)
result = paypal.process_payment(49.99)
print(result.message)  # "PayPal payment of USD 49.99 completed"
```

---

## 🆚 Factory vs Direct Instantiation

```python
# ❌ WITHOUT Factory (tight coupling)
if payment_type == "credit_card":
    processor = CreditCardProcessor()
elif payment_type == "paypal":
    processor = PayPalProcessor()
elif payment_type == "upi":
    processor = UPIProcessor()
# Adding new type = modifying this code everywhere!

# ✅ WITH Factory (loose coupling)
processor = PaymentFactory.create(payment_type)
# Adding new type = just register it in the factory!
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Creational |
| **Intent** | Create objects without specifying exact class |
| **Key Benefit** | Loose coupling, easy to extend |
| **Key Risk** | Over-engineering for simple cases |
| **Use When** | Multiple related types with the same interface |
| **Avoid When** | Only one type exists or types never change |
