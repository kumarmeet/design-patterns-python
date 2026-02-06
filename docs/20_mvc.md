# 🎛️ MVC (Model-View-Controller) Pattern

## What Is It? (Explain Like I'm 10)

Imagine a **restaurant**:
- 👨‍🍳 **Kitchen (Model)** — Cooks the food (handles the data)
- 🍽️ **Plate Presentation (View)** — How the food looks on the plate (what users see)
- 🧑‍🍳 **Waiter (Controller)** — Takes your order and tells the kitchen what to cook (handles user actions)

The kitchen doesn't know how the food is presented. The waiter connects everything together.

That's MVC — separating **data**, **display**, and **control logic** into three parts.

---

## 📖 Simple Definition

> MVC separates an application into three components:
> - **Model**: Data and business logic
> - **View**: User interface / presentation
> - **Controller**: Handles user input and coordinates Model and View

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🍽️ Restaurant | Kitchen (Model) → Waiter (Controller) → Plate (View) |
| 📺 TV System | Signal/Data (Model) → Remote (Controller) → Screen (View) |
| 🏥 Hospital | Medical records (Model) → Doctor (Controller) → Patient report (View) |
| 🎭 Theater | Script (Model) → Director (Controller) → Stage performance (View) |

---

## ✅ When to Use

- **Web applications** — Django, Flask, Rails, ASP.NET
- **Desktop applications** — Separating business logic from UI
- **API backends** — Model handles data, Controller handles routes
- **When teams work in parallel** — Frontend devs work on View, backend on Model
- **When UI might change** — Same data, different views (web, mobile, CLI)

---

## ❌ When NOT to Use

- **Very simple scripts** — MVC is overkill for a 50-line script
- **When there's no UI** — Background services don't need a View
- **Tightly coupled systems** — If Model and View are inseparable, MVC adds unnecessary layers

---

## 🔧 How It Works

```
    User Action
        │
        ▼
  ┌──────────────┐
  │  Controller   │ ← Handles user input
  └──────┬───────┘
         │ Updates
         ▼
  ┌──────────────┐
  │    Model      │ ← Data & business logic
  └──────┬───────┘
         │ Notifies
         ▼
  ┌──────────────┐
  │    View       │ ← Displays data
  └──────────────┘
```

---

## 💻 Code Example

```python
from design_patterns.architectural.mvc import TaskModel, TaskView, TaskController

model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

# User actions go through the Controller
controller.create_task("Build API", "REST endpoints", "high")
controller.create_task("Write tests", "Pytest", "medium")
controller.start_task(1)
controller.complete_task(1)

# View displays the data
controller.show_all_tasks()
controller.show_stats()
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Architectural |
| **Intent** | Separate data, display, and control logic |
| **Key Benefit** | Clear separation, parallel development |
| **Key Risk** | Overhead for simple applications |
| **Use When** | Web apps, desktop apps, team projects |
| **Avoid When** | Simple scripts, no UI involved |
