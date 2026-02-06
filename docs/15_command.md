# 🎮 Command Pattern

## What Is It? (Explain Like I'm 10)

Imagine you're using a **text editor** and you:
1. Type "Hello" → you can press **Ctrl+Z** to undo it!
2. Make text bold → **Ctrl+Z** undoes it!
3. Delete a word → **Ctrl+Z** brings it back!

Every action is saved as a **command**. The editor remembers all commands so it can undo and redo them.

That's the Command pattern — turning actions into **objects** that can be stored, undone, and replayed.

---

## 📖 Simple Definition

> The Command pattern turns a **request into an object**, allowing you to parameterize clients with different requests, **queue** them, **log** them, and support **undo/redo** operations.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📝 Ctrl+Z (Undo) | Every action is recorded and can be reversed |
| 🎮 Game Replay | All player actions are saved and can be replayed |
| 📋 Restaurant Order Ticket | Waiter writes order → kitchen executes it later |
| 🏠 Smart Home Remote | Each button stores a command (light on, AC off) |

---

## ✅ When to Use

- **Undo/Redo functionality** — Text editors, graphic design tools
- **Task queuing** — Commands waiting to be executed
- **Macro recording** — Record a sequence of commands and replay them
- **Transaction logging** — Log every action for recovery
- **Smart home automation** — Store and execute device commands

---

## ❌ When NOT to Use

- **Simple, non-reversible actions** — If undo isn't needed, commands add complexity
- **One-time operations** — If the action is fire-and-forget, direct calls are simpler
- **Too many small commands** — Creates class explosion

---

## 💻 Code Example

```python
from design_patterns.behavioral.command import (
    TextDocument, TextEditor, InsertTextCommand, ReplaceTextCommand
)

doc = TextDocument()
editor = TextEditor(doc)

editor.execute(InsertTextCommand(doc, 0, "Hello World"))
editor.execute(ReplaceTextCommand(doc, "World", "Python"))
# doc = "Hello Python"

editor.undo()   # doc = "Hello World"
editor.undo()   # doc = ""
editor.redo()   # doc = "Hello World"
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Encapsulate actions as objects |
| **Key Benefit** | Undo/redo, queuing, logging |
| **Key Risk** | Class explosion with many commands |
| **Use When** | Actions need to be undone, queued, or logged |
| **Avoid When** | Simple one-way actions |
