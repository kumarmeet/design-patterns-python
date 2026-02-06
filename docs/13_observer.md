# 📢 Observer Pattern

## What Is It? (Explain Like I'm 10)

Imagine you **subscribe** to a YouTube channel. When the creator uploads a new video, you get a **notification** automatically! You don't have to keep checking — the notification comes to YOU.

That's the Observer pattern — when something changes, everyone who's interested gets notified automatically.

---

## 📖 Simple Definition

> The Observer pattern defines a **one-to-many** dependency between objects. When one object (the **subject**) changes state, all its dependents (the **observers**) are **notified automatically**.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📺 YouTube Subscriptions | New video → all subscribers get notified |
| 📰 Newspaper Subscription | New paper → delivered to all subscribers |
| 🔔 Phone Notifications | New message → your phone, watch, and laptop all beep |
| 📢 Classroom Announcement | Teacher announces → all students hear it |

---

## ✅ When to Use

- **Event-driven systems** — Something happens → multiple things react
- **Real-time notifications** — Order status, stock prices, chat messages
- **UI data binding** — Data changes → UI updates automatically
- **Logging and monitoring** — Actions trigger log entries across multiple systems
- **Message brokers** — Pub/sub systems (Kafka, RabbitMQ concepts)

---

## ❌ When NOT to Use

- **Simple one-to-one communication** — If only one thing reacts, just call it directly
- **When order matters critically** — Observers are notified in registration order, which may not be guaranteed
- **Memory-sensitive apps** — Forgotten observers can cause memory leaks
- **When updates are very frequent** — Can cause performance issues if observers are slow

---

## 🔧 How It Works

```
       Order (Subject)
         │ status changed!
         │
    ┌────┼────┬──────────┐
    │    │    │          │
    ▼    ▼    ▼          ▼
Customer  Dashboard  Inventory  Delivery
Notifier  Updater    Manager    Tracker
  📧        📊        📦         🚚
```

---

## 💻 Code Example

```python
from design_patterns.behavioral.observer import (
    Order, OrderStatus,
    CustomerNotifier, DashboardUpdater, DeliveryTracker
)

order = Order("ORD-001")

# Subscribe observers
order.subscribe(CustomerNotifier("Alice"))
order.subscribe(DashboardUpdater())
order.subscribe(DeliveryTracker())

# When status changes, ALL observers are notified!
order.update_status(OrderStatus.SHIPPED, "Package on the way")
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Notify multiple objects of state changes |
| **Key Benefit** | Loose coupling, automatic updates |
| **Key Risk** | Memory leaks, unexpected update cascades |
| **Use When** | One change needs to trigger multiple reactions |
| **Avoid When** | Simple one-to-one communication |
