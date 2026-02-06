# 📋 Template Method Pattern

## What Is It? (Explain Like I'm 10)

Think of **making different drinks**:
- Tea: Boil water → Steep tea bag → Pour → Add lemon
- Coffee: Boil water → Brew coffee → Pour → Add sugar & cream
- Hot Chocolate: Boil water → Mix cocoa → Pour → Add marshmallows

The **steps are the same** (boil, brew, pour, add extras), but the **details differ** for each drink.

That's the Template Method — a **recipe template** where the steps are fixed, but specific steps can be customized.

---

## 📖 Simple Definition

> The Template Method pattern defines the **skeleton of an algorithm** in a base class. Subclasses override specific steps without changing the overall structure.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| ☕ Beverage Recipe | Same steps (boil, brew, pour), different details per drink |
| 🏠 Building a House | Same process (foundation, walls, roof), different styles |
| 📝 Tax Filing | Same steps (income, deductions, calculate), different forms |
| 🧪 Lab Experiment | Same procedure (setup, run, measure, cleanup), different experiments |

---

## ✅ When to Use

- **Data processing pipelines** — Read → Validate → Transform → Save (same structure, different formats)
- **Report generation** — Gather data → Format → Render → Export
- **Game AI** — Same turn structure, different strategies per character
- **Testing frameworks** — Setup → Run test → Teardown
- **ETL processes** — Extract → Transform → Load

---

## ❌ When NOT to Use

- **When algorithms are completely different** — If steps don't overlap, don't force a template
- **When you need full flexibility** — Template locks the structure; if clients need to change step ORDER, use Strategy
- **Too many abstract steps** — If every step is abstract, the template is useless

---

## 💻 Code Example

```python
from design_patterns.behavioral.template_method import (
    CSVDataProcessor, JSONDataProcessor
)

# Same process() template, different implementations
csv_proc = CSVDataProcessor()
csv_proc.process("users.csv")  # Read CSV → Validate → Transform → Save

json_proc = JSONDataProcessor()
json_proc.process("products.json")  # Read JSON → Validate → Transform → Save
```

---

## 🆚 Template Method vs Strategy

| Feature | Template Method | Strategy |
|---------|----------------|----------|
| **Structure** | Fixed algorithm skeleton | Interchangeable algorithm |
| **Inheritance** | Uses subclassing | Uses composition |
| **What varies** | Individual steps | The entire algorithm |
| **Flexibility** | Less (structure is locked) | More (swap entire algorithm) |

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Define algorithm skeleton, let subclasses customize steps |
| **Key Benefit** | Code reuse, consistent structure |
| **Key Risk** | Rigid structure, hard to change step order |
| **Use When** | Multiple variations of the same process |
| **Avoid When** | Algorithms are fundamentally different |
