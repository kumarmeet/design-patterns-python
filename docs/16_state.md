# 🚦 State Pattern

## What Is It? (Explain Like I'm 10)

Think of a **traffic light**:
- When it's 🔴 RED → cars STOP
- When it's 🟢 GREEN → cars GO
- When it's 🟡 YELLOW → cars SLOW DOWN

The traffic light is the SAME object, but its **behavior changes** based on its **color (state)**.

That's the State pattern — an object acts differently depending on what state it's in.

---

## 📖 Simple Definition

> The State pattern allows an object to **change its behavior** when its internal state changes. It appears as if the object changes its class.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🚦 Traffic Light | Red=stop, Green=go, Yellow=slow — same light, different behavior |
| 📱 Phone | Locked=show lock screen, Unlocked=show home screen |
| 🎵 Music Player | Playing=show pause button, Paused=show play button |
| 📦 Order Status | Pending→Processing→Shipped→Delivered — different actions at each stage |

---

## ✅ When to Use

- **Order processing** — Different actions available at each stage
- **Game character states** — Idle, Running, Jumping, Attacking
- **Document workflow** — Draft → Review → Published → Archived
- **Audio/video players** — Playing, Paused, Stopped
- **Vending machines** — No coin → Coin inserted → Dispensing

---

## ❌ When NOT to Use

- **Few states with simple transitions** — A boolean flag might be enough
- **States that rarely change** — If state is mostly static, it's overkill
- **When switch/if-else is readable** — For 2-3 states, simple conditionals work fine

---

## 💻 Code Example

```python
from design_patterns.behavioral.state import OnlineOrder

order = OnlineOrder("ORD-001")

print(order.ship())     # "Can't ship — not processed yet!"
print(order.process())  # "Order is now being processed!"
print(order.ship())     # "Order shipped!"
print(order.cancel())   # "Can't cancel — already in transit!"
print(order.deliver())  # "Order delivered successfully!"
```

---

## 🆚 State vs If/Else

```python
# ❌ WITHOUT State Pattern
if order.status == "pending":
    if action == "ship":
        return "Can't ship yet!"
elif order.status == "processing":
    if action == "ship":
        order.status = "shipped"
# Gets very messy with many states and actions!

# ✅ WITH State Pattern
order.ship()  # Each state knows what to do!
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Change behavior based on internal state |
| **Key Benefit** | Clean state transitions, eliminates complex conditionals |
| **Key Risk** | Too many state classes for simple scenarios |
| **Use When** | Object has distinct states with different behaviors |
| **Avoid When** | Only 2-3 simple states |
