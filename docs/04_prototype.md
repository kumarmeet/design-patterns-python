# 📋 Prototype Pattern

## What Is It? (Explain Like I'm 10)

Imagine you have a **coloring page** that's perfectly drawn. Instead of drawing it again from scratch, you **photocopy** it! Now you have an exact copy, and you can color each copy differently.

That's the Prototype pattern — **clone** an existing object instead of creating a new one from scratch.

---

## 📖 Simple Definition

> The Prototype pattern creates new objects by **copying (cloning)** existing ones. This is useful when creating an object is expensive or complex, but copying it is cheap.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📄 Photocopying | Copy a document and edit the copy |
| 🧬 Cell Division | A cell splits into two identical cells, which then grow differently |
| 📝 Document Templates | Start from a template, customize for each use |
| 🎮 Game Enemies | Clone a base enemy and tweak health, speed, color |

---

## ✅ When to Use

- **Document templates** — Clone a template and customize per user
- **Game development** — Clone enemy/character templates with slight variations
- **Configuration presets** — Clone a default config and adjust specific values
- **When object creation is expensive** — Cloning is faster than constructing from scratch
- **When objects have many default values** — Clone the defaults, change only what differs

---

## ❌ When NOT to Use

- **Simple objects** — If creating a new object is easy, cloning is overkill
- **Objects with circular references** — Deep copying can cause infinite loops
- **When objects should be unique** — If each instance must be different, start from scratch
- **Immutable objects** — No need to clone if objects can't be modified

---

## ⚠️ Deep Copy vs Shallow Copy

```
Shallow Copy:                    Deep Copy:
Original ──► [list] ◄── Copy    Original ──► [list_A]
  Both point to SAME list!       Copy ──► [list_B]  (independent!)
```

**Always use deep copy** when your object contains lists, dicts, or other mutable objects!

---

## 💻 Code Example

```python
from design_patterns.creational.prototype import GameCharacter

# Create a template
goblin = GameCharacter(
    name="Goblin", health=50, attack=8,
    abilities=["slash"], equipment={"weapon": "sword"}
)

# Clone and customize
warrior = goblin.clone()
warrior.name = "Goblin Warrior"
warrior.health = 80

# They're independent!
print(warrior.name)     # "Goblin Warrior"
print(goblin.name)      # "Goblin" (unchanged!)
print(warrior is goblin) # False
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Creational |
| **Intent** | Create objects by cloning existing ones |
| **Key Benefit** | Fast creation of similar objects |
| **Key Risk** | Deep copy issues with complex objects |
| **Use When** | Creating objects is expensive, or you need many similar objects |
| **Avoid When** | Objects are simple or must be unique |
