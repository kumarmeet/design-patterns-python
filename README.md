# 🎨 Design Patterns & OOP Concepts in Python

A comprehensive collection of **7 OOP concepts** and **21 software design patterns** implemented in Python with **real-world, easy-to-understand examples**. Each topic includes working code and detailed documentation explaining **why, when, and when NOT** to use it.

> 💡 **Philosophy**: Every example is realistic, practical, and explained so simply that even a 10-year-old can understand the concept.

> 📚 **Learning Path**: Start with OOP Concepts first → then move to Design Patterns!

---

## 📦 Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd design-patterns

# Install with uv
uv sync

# List all available topics
uv run python -m examples.runner

# Run an OOP concept
uv run python -m examples.runner classes_and_objects
uv run python -m examples.runner encapsulation
uv run python -m examples.runner solid_principles

# Run a design pattern
uv run python -m examples.runner singleton
uv run python -m examples.runner factory
uv run python -m examples.runner builder

# Run all OOP concepts
uv run python -m examples.runner oops

# Run all patterns in a category
uv run python -m examples.runner creational
uv run python -m examples.runner structural
uv run python -m examples.runner behavioral
uv run python -m examples.runner architectural

# Run ALL demos (OOP + patterns)
uv run python -m examples.runner all
```

---

## 📂 Project Structure

```
design-patterns/
├── pyproject.toml                          # Project config (uv)
├── README.md                               # This file
│
├── src/
│   ├── oops_concepts/                      # 📚 OOP Fundamentals (Start Here!)
│   │   ├── classes_and_objects.py           # The building blocks
│   │   ├── encapsulation.py                # Protecting data
│   │   ├── inheritance.py                  # Reusing & extending code
│   │   ├── polymorphism.py                 # Same interface, different behavior
│   │   ├── abstraction.py                  # Hiding complexity
│   │   ├── composition.py                  # Has-A vs Is-A
│   │   └── solid_principles.py             # 5 rules for clean OOP
│   │
│   └── design_patterns/                    # 🎨 Design Patterns
│       ├── creational/                     # 🏗️ Object creation patterns
│       │   ├── singleton.py                # One instance only
│       │   ├── factory.py                  # Flexible object creation
│       │   ├── abstract_factory.py         # Families of related objects
│       │   ├── builder.py                  # Step-by-step construction
│       │   └── prototype.py                # Clone existing objects
│       │
│       ├── structural/                     # 🧱 Object composition patterns
│       │   ├── adapter.py                  # Make incompatible interfaces work
│       │   ├── decorator.py                # Add behavior dynamically
│       │   ├── facade.py                   # Simplify complex systems
│       │   ├── proxy.py                    # Control access to objects
│       │   ├── composite.py                # Tree structures
│       │   └── bridge.py                   # Separate abstraction & implementation
│       │
│       ├── behavioral/                     # 🧠 Object communication patterns
│       │   ├── strategy.py                 # Swappable algorithms
│       │   ├── observer.py                 # Event-driven notifications
│       │   ├── chain_of_responsibility.py  # Request processing pipeline
│       │   ├── command.py                  # Actions as objects (undo/redo)
│       │   ├── state.py                    # Behavior based on state
│       │   ├── template_method.py          # Algorithm skeleton
│       │   ├── iterator.py                 # Sequential access
│       │   └── mediator.py                 # Centralized communication
│       │
│       └── architectural/                  # 🏛️ System-level patterns
│           ├── mvc.py                      # Model-View-Controller
│           ├── dependency_injection.py     # Loose coupling via DI
│           └── repository.py               # Abstract data access
│
├── docs/                                   # 📖 Detailed documentation
│   ├── oops/                               # OOP concept guides
│   │   ├── 01_classes_and_objects.md
│   │   ├── 02_encapsulation.md
│   │   ├── 03_inheritance.md
│   │   ├── 04_polymorphism.md
│   │   ├── 05_abstraction.md
│   │   ├── 06_composition.md
│   │   └── 07_solid_principles.md
│   │
│   ├── 01_singleton.md                     # Design pattern guides
│   ├── 02_factory.md
│   ├── 03_builder.md
│   ├── 04_prototype.md
│   ├── 05_abstract_factory.md
│   ├── 06_adapter.md
│   ├── 07_decorator.md
│   ├── 08_facade.md
│   ├── 09_proxy.md
│   ├── 10_composite.md
│   ├── 11_bridge.md
│   ├── 12_strategy.md
│   ├── 13_observer.md
│   ├── 14_chain_of_responsibility.md
│   ├── 15_command.md
│   ├── 16_state.md
│   ├── 17_template_method.md
│   ├── 18_iterator.md
│   ├── 19_mediator.md
│   ├── 20_mvc.md
│   ├── 21_dependency_injection.md
│   └── 22_repository.md
│
└── examples/
    └── runner.py                           # Demo runner for everything
```

---

## 📚 Learning Path (Recommended Order)

### Step 1: OOP Concepts — *Master these BEFORE design patterns!*

| # | Concept | What You'll Learn | Doc |
|---|---------|-------------------|-----|
| 1 | **Classes & Objects** | Blueprints, instances, constructors, dunder methods | [📖](docs/oops/01_classes_and_objects.md) |
| 2 | **Encapsulation** | Data protection, properties, access levels | [📖](docs/oops/02_encapsulation.md) |
| 3 | **Inheritance** | Code reuse, method overriding, MRO, super() | [📖](docs/oops/03_inheritance.md) |
| 4 | **Polymorphism** | Duck typing, method overriding, operator overloading | [📖](docs/oops/04_polymorphism.md) |
| 5 | **Abstraction** | Abstract classes, interfaces, hiding complexity | [📖](docs/oops/05_abstraction.md) |
| 6 | **Composition** | Has-A vs Is-A, building with parts, flexibility | [📖](docs/oops/06_composition.md) |
| 7 | **SOLID Principles** | 5 rules: SRP, OCP, LSP, ISP, DIP | [📖](docs/oops/07_solid_principles.md) |

### Step 2: Design Patterns

#### 🏗️ Creational Patterns — *How objects are created*

| # | Pattern | Purpose | Real-World Example |
|---|---------|---------|-------------------|
| 1 | [Singleton](docs/01_singleton.md) | One instance only | App Config, Logger |
| 2 | [Factory Method](docs/02_factory.md) | Flexible object creation | Payment Gateways, Notifications |
| 3 | [Builder](docs/03_builder.md) | Step-by-step construction | HTTP Requests, Pizza Orders |
| 4 | [Prototype](docs/04_prototype.md) | Clone existing objects | Document Templates, Game Characters |
| 5 | [Abstract Factory](docs/05_abstract_factory.md) | Families of related objects | Cross-Platform UI Components |

#### 🧱 Structural Patterns — *How objects are composed*

| # | Pattern | Purpose | Real-World Example |
|---|---------|---------|-------------------|
| 6 | [Adapter](docs/06_adapter.md) | Make incompatible interfaces work | Stripe/PayPal/Razorpay Integration |
| 7 | [Decorator](docs/07_decorator.md) | Add behavior dynamically | Coffee Shop, Web Middleware |
| 8 | [Facade](docs/08_facade.md) | Simplify complex systems | Online Store "Place Order" |
| 9 | [Proxy](docs/09_proxy.md) | Control access to objects | Internet Filter, API Cache |
| 10 | [Composite](docs/10_composite.md) | Tree structures | File System, Company Org Chart |
| 11 | [Bridge](docs/11_bridge.md) | Separate abstraction & implementation | Notifications × Channels |

#### 🧠 Behavioral Patterns — *How objects communicate*

| # | Pattern | Purpose | Real-World Example |
|---|---------|---------|-------------------|
| 12 | [Strategy](docs/12_strategy.md) | Swappable algorithms | Pricing/Discount Engine |
| 13 | [Observer](docs/13_observer.md) | Event-driven notifications | Order Tracking, Stock Prices |
| 14 | [Chain of Responsibility](docs/14_chain_of_responsibility.md) | Request processing pipeline | Expense Approval, Auth Pipeline |
| 15 | [Command](docs/15_command.md) | Actions as objects | Text Editor Undo/Redo |
| 16 | [State](docs/16_state.md) | Behavior based on state | Order Processing, Audio Player |
| 17 | [Template Method](docs/17_template_method.md) | Algorithm skeleton | Data Processing Pipeline |
| 18 | [Iterator](docs/18_iterator.md) | Sequential access | Music Playlist, Pagination |
| 19 | [Mediator](docs/19_mediator.md) | Centralized communication | Chat Room, Smart Home |

#### 🏛️ Architectural Patterns — *How systems are organized*

| # | Pattern | Purpose | Real-World Example |
|---|---------|---------|-------------------|
| 20 | [MVC](docs/20_mvc.md) | Separate data, UI, and control | Task Management App |
| 21 | [Dependency Injection](docs/21_dependency_injection.md) | Loose coupling via DI | Notification Service, DB Layer |
| 22 | [Repository](docs/22_repository.md) | Abstract data access | User Management, Product Catalog |

---

## 🎯 How to Use This Project

### 📖 As a Learning Resource
1. **Start with OOP concepts** in `docs/oops/` — master these fundamentals first
2. Then move to **design patterns** in `docs/` — each one builds on OOP concepts
3. Read the docs, then study the code, then run the demos

### 💻 Run the Demos
```bash
# Run any individual topic
uv run python -m examples.runner classes_and_objects
uv run python -m examples.runner solid_principles
uv run python -m examples.runner singleton

# Or run each file directly
uv run python src/oops_concepts/classes_and_objects.py
uv run python src/oops_concepts/solid_principles.py
uv run python src/design_patterns/creational/singleton.py
```

### 🧪 Import in Your Projects
```python
from design_patterns.creational import PaymentFactory, HttpRequestBuilder
from design_patterns.behavioral import ShoppingCart, PercentageDiscount
from design_patterns.structural import OnlineStoreFacade
```

---

## 🧰 Tech Stack

- **Python 3.12+**
- **uv** — Fast Python package manager
- **No external dependencies** — Pure Python implementations

---

## 📌 Quick Reference: When to Use What?

### OOP Concept → Design Pattern Connection

| OOP Concept | Patterns That Use It |
|---|---|
| **Encapsulation** | Singleton, Proxy, Facade |
| **Inheritance** | Template Method, Strategy, Factory |
| **Polymorphism** | Strategy, Observer, Command, Factory |
| **Abstraction** | All patterns! (ABC is everywhere) |
| **Composition** | Decorator, Strategy, Observer, Bridge |
| **SOLID Principles** | Every well-designed pattern follows SOLID |

### Problem → Pattern Guide

| Problem | Pattern |
|---------|---------|
| Need exactly one shared instance | **Singleton** |
| Create objects based on a condition | **Factory** |
| Create families of matching objects | **Abstract Factory** |
| Build complex objects step by step | **Builder** |
| Clone and customize existing objects | **Prototype** |
| Make incompatible APIs work together | **Adapter** |
| Add features without modifying code | **Decorator** |
| Simplify a complex subsystem | **Facade** |
| Control or cache access to an object | **Proxy** |
| Work with tree/hierarchical structures | **Composite** |
| Avoid class explosion from combinations | **Bridge** |
| Swap algorithms at runtime | **Strategy** |
| Notify many objects of a change | **Observer** |
| Process requests through a pipeline | **Chain of Responsibility** |
| Support undo/redo or action queuing | **Command** |
| Object behavior changes with state | **State** |
| Same process structure, different details | **Template Method** |
| Navigate a collection sequentially | **Iterator** |
| Coordinate complex object interactions | **Mediator** |
| Separate data, UI, and control logic | **MVC** |
| Make code testable and flexible | **Dependency Injection** |
| Separate data access from business logic | **Repository** |

---

## 📄 License

This project is open source and available for learning purposes.
# design-patterns-python
