# 💉 Dependency Injection (DI) Pattern

## What Is It? (Explain Like I'm 10)

Imagine a **chef** in a restaurant. The chef needs ingredients (flour, eggs, butter) to cook.

**Without DI**: The chef has to go to the farm, pick the vegetables, milk the cow, and then cook. That's exhausting!

**With DI**: The ingredients are **delivered** to the kitchen. The chef just cooks with whatever arrives. If tomorrow a different farm delivers organic ingredients, the chef's recipe doesn't change at all!

That's DI — your class **receives** what it needs instead of **creating** it internally.

---

## 📖 Simple Definition

> Dependency Injection provides dependencies **from outside** rather than having the object create them internally. This promotes loose coupling, testability, and flexibility.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 👨‍🍳 Chef + Ingredients | Ingredients delivered to kitchen (not grown by chef) |
| 🔌 Electrical Outlets | Appliances use ANY outlet — they don't build their own power plant |
| 🚗 Car + Fuel | Car works with gasoline, diesel, or electric — fuel is "injected" |
| 🧰 Worker + Tools | Tools are provided by the company, not built by the worker |

---

## ✅ When to Use

- **Unit testing** — Inject mock dependencies so tests don't hit real databases/APIs
- **Service-based architectures** — Swap implementations without changing business logic
- **Multi-environment apps** — Different databases for dev, test, prod
- **Framework development** — Spring, NestJS, .NET all use DI heavily
- **When flexibility matters** — Swap email providers, payment gateways, etc.

---

## ❌ When NOT to Use

- **Simple scripts** — DI adds complexity for small programs
- **When there's only one implementation** — If it'll never change, just create it directly
- **Over-injection** — Injecting EVERYTHING (even simple values) is over-engineering

---

## 🔧 The Key Idea

```python
# ❌ WITHOUT DI (tightly coupled)
class NotificationService:
    def __init__(self):
        self.sender = EmailSender()  # Hardcoded! Can't change or test!

# ✅ WITH DI (loosely coupled)
class NotificationService:
    def __init__(self, sender: MessageSender):  # Injected!
        self.sender = sender  # Can be Email, SMS, or MockSender!
```

---

## Three Types of DI

| Type | How It Works | Example |
|------|-------------|---------|
| **Constructor Injection** | Pass dependency in `__init__` | `Service(database=PostgresDB())` |
| **Method Injection** | Pass dependency in a method | `service.process(sender=EmailSender())` |
| **Property Injection** | Set dependency as a property | `service.sender = EmailSender()` |

**Constructor Injection** is the most common and recommended approach.

---

## 💻 Code Example

```python
from design_patterns.architectural.dependency_injection import (
    NotificationService, EmailSender, MockSender
)

# Production: use real email sender
prod_service = NotificationService(EmailSender())
prod_service.send_welcome("alice@example.com", "Alice")

# Testing: inject mock sender — no real emails sent!
mock = MockSender()
test_service = NotificationService(mock)
test_service.send_welcome("test@test.com", "TestUser")
print(len(mock.sent_messages))  # 1 (captured, not actually sent!)
```

---

## 🆚 With vs Without DI

| Without DI ❌ | With DI ✅ |
|---|---|
| Hard to test | Easy to test (inject mocks) |
| Tight coupling | Loose coupling |
| Hard to change implementations | Swap implementations easily |
| Single environment | Multi-environment support |

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Architectural / Creational |
| **Intent** | Provide dependencies from outside |
| **Key Benefit** | Testability, flexibility, loose coupling |
| **Key Risk** | Over-engineering for simple apps |
| **Use When** | Testing is important, multiple implementations exist |
| **Avoid When** | Simple scripts with one implementation |
