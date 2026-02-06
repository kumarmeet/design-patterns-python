# 🏗️ Abstract Factory Pattern

## What Is It? (Explain Like I'm 10)

Imagine you go to **IKEA** and pick a furniture style — "Modern" or "Classic." Once you pick a style, EVERYTHING you get (chair, table, lamp) comes in that style. You don't get a modern chair with a classic table — they all MATCH.

That's the Abstract Factory! It creates **families of related objects** that all work together.

---

## 📖 Simple Definition

> The Abstract Factory pattern provides an interface for creating **families of related objects** without specifying their concrete classes. All objects from one factory are guaranteed to be compatible.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🪑 IKEA Furniture Sets | Pick "Modern" → get modern chair, table, sofa (all matching!) |
| 🎨 Theme Packs | Pick "Dark Mode" → all UI elements become dark |
| 🍔 Fast Food Meals | Pick "Combo #1" → get matching burger, fries, drink |
| 🖥️ OS Widgets | Windows creates Windows-style buttons; Mac creates Mac-style buttons |

---

## ✅ When to Use

- **Cross-platform UIs** — Create matching Web, Mobile, or Desktop components
- **Theme systems** — Dark theme factory creates all dark components; light theme creates light ones
- **Database abstraction** — MySQL factory creates MySQL-specific queries, connections, and pools
- **Game environments** — Forest factory creates forest trees, animals, and terrain; Desert factory creates desert versions

---

## ❌ When NOT to Use

- **When there's only one family** — If you'll only ever have one set of objects, use a simple Factory
- **When products don't need to match** — If components are independent, Abstract Factory is overkill
- **Small applications** — The complexity isn't worth it for simple apps

---

## 🔧 How It Works

```
                    UIFactory (Abstract)
                   /         |          \
          create_button  create_input  create_checkbox
                /            |              \
    WebUIFactory    MobileUIFactory    DesktopUIFactory
        │                  │                  │
    WebButton         MobileButton       DesktopButton
    WebInput          MobileInput        DesktopInput
    WebCheckbox       MobileCheckbox     DesktopCheckbox
```

---

## 💻 Code Example

```python
from design_patterns.creational.abstract_factory import (
    WebUIFactory, MobileUIFactory, build_login_form
)

# Build login form for Web
web_form = build_login_form(WebUIFactory())
# All components are Web-styled!

# Build login form for Mobile — SAME code, different factory!
mobile_form = build_login_form(MobileUIFactory())
# All components are Mobile-styled!
```

---

## 🆚 Factory vs Abstract Factory

| Feature | Factory Method | Abstract Factory |
|---------|---------------|------------------|
| Creates | ONE type of object | FAMILY of related objects |
| Example | Create a Button | Create Button + Input + Checkbox (matching!) |
| Complexity | Simpler | More complex |
| Use when | One product varies | Multiple products must match |

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Creational |
| **Intent** | Create families of related objects |
| **Key Benefit** | Guaranteed compatibility between products |
| **Key Risk** | High complexity for simple cases |
| **Use When** | Multiple related objects must work together |
| **Avoid When** | Products don't need to match, or there's only one family |
