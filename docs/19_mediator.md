# 🗼 Mediator Pattern

## What Is It? (Explain Like I'm 10)

Imagine an **airport control tower**. Airplanes DON'T talk to each other directly. Instead, every plane talks to the **control tower**, and the tower tells each plane what to do.

Without the tower, 50 planes would have to coordinate with each other — chaos! With the tower, they only communicate through ONE central place.

That's the Mediator pattern — a **central coordinator** so objects don't need to know about each other.

---

## 📖 Simple Definition

> The Mediator pattern defines an object that **encapsulates how a set of objects interact**. It promotes **loose coupling** by preventing objects from referring to each other directly.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| ✈️ Airport Control Tower | Planes communicate through the tower, not directly |
| 💬 Group Chat | Messages go through the chat room, not person-to-person |
| 🏠 Smart Home Hub | Devices communicate through the hub (e.g., Google Home) |
| 🏫 Teacher in a Classroom | Students raise hands and speak through the teacher |

---

## ✅ When to Use

- **Chat systems** — Messages routed through a central chat room
- **Smart home automation** — One event triggers coordinated responses
- **UI dialog boxes** — Components communicate through the dialog (not directly)
- **Air traffic control** — Coordinating multiple entities
- **Workflow orchestration** — Central coordinator for multi-step processes

---

## ❌ When NOT to Use

- **Two objects communicating** — Direct communication is simpler
- **When the mediator becomes a god object** — If it grows too large, it defeats the purpose
- **Simple event handling** — Observer pattern might be simpler

---

## 🆚 Mediator vs Observer

| Feature | Mediator | Observer |
|---------|----------|----------|
| Communication | Through central hub | Broadcast to all subscribers |
| Knowledge | Mediator knows all participants | Subject doesn't know observer details |
| Coordination | Complex multi-way logic | Simple one-to-many notification |
| Use case | Smart home, chat rooms | Notifications, events |

---

## 💻 Code Example

```python
from design_patterns.behavioral.mediator import (
    ChatRoom, ChatUser, SmartHomeController
)

# Chat Room: users communicate through the mediator
room = ChatRoom("Python Devs")
alice = ChatUser("Alice")
bob = ChatUser("Bob")

room.add_user(alice)
room.add_user(bob)

alice.send("Hello!")  # Bob receives it through the room

# Smart Home: devices coordinate through the controller
home = SmartHomeController()
home.motion_sensor.detect_motion()  # Lights ON, Camera recording starts
home.door_lock.lock()               # Lights OFF, Thermostat to eco mode
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Centralize complex communication |
| **Key Benefit** | Loose coupling, clear coordination |
| **Key Risk** | Mediator can become a god object |
| **Use When** | Many objects need coordinated interaction |
| **Avoid When** | Simple direct communication suffices |
