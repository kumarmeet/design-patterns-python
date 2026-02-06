# 🧱 Singleton Pattern

## What Is It? (Explain Like I'm 10)

Imagine there's only **ONE principal's office** in your school. No matter which teacher or student goes to ask a question, they all go to the **same office**. You can't build a second principal's office — there's always just one.

That's the Singleton pattern! It makes sure a class has **only ONE instance** (one copy), and everyone in the program uses that same one.

---

## 📖 Simple Definition

> The Singleton pattern ensures that a class has **only one instance** and provides a **global point of access** to that instance.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🏫 Principal's Office | Only ONE in the whole school — everyone visits the same one |
| 📱 Settings App | Your phone has ONE settings app, no matter how many times you open it |
| 🌍 Earth | There's only ONE Earth — you can't create another one |
| 📋 School Diary | ONE diary for the whole school where all announcements go |

---

## ✅ When to Use

- **Configuration Manager** — Your app needs ONE place to store all settings (database URL, API keys, etc.)
- **Logger Service** — All logs should go to ONE place, not scattered across multiple loggers
- **Database Connection Pool** — You want ONE pool of connections shared by everyone
- **Cache Manager** — ONE cache store that everyone reads from and writes to
- **Print Spooler** — ONE queue that manages all print jobs

---

## ❌ When NOT to Use

- **When you need multiple instances** — If different parts of your app need separate configurations, Singleton will cause problems
- **In unit tests** — Singletons carry state between tests, making them unpredictable
- **When it hides dependencies** — If everything depends on a Singleton, it becomes a hidden global variable
- **In multi-threaded apps without proper locking** — Without thread safety, two threads might create two instances

---

## ⚠️ Common Pitfalls

1. **Testing Nightmare** — Singletons keep state between tests. You can't easily reset them.
2. **Hidden Dependencies** — Code that uses a Singleton doesn't clearly show its dependencies.
3. **Tight Coupling** — Everything depends on the Singleton, making changes risky.
4. **Concurrency Issues** — Without proper locking, two threads can create two instances.

---

## 🔧 How It Works

```
┌──────────────────────────────┐
│        SingletonMeta         │
│  (Controls instance creation)│
├──────────────────────────────┤
│  _instances: dict            │
│  _lock: Lock                 │
├──────────────────────────────┤
│  __call__() → instance       │
│    ├─ Check if exists        │
│    ├─ Lock (thread-safe)     │
│    ├─ Create if first time   │
│    └─ Return same instance   │
└──────────────────────────────┘
```

---

## 💻 Code Example

```python
from design_patterns.creational.singleton import AppConfig, Logger

# Both variables point to the SAME instance
config1 = AppConfig()
config2 = AppConfig()

config1.set("database", "postgresql://localhost/mydb")
print(config2.get("database"))  # Same value! They're the same object.
print(config1 is config2)       # True

# Logger — same idea
logger1 = Logger()
logger2 = Logger()
logger1.info("Server started")
print(logger2.get_logs())  # Shows the log from logger1!
```

---

## 🆚 Singleton vs Global Variable

| Feature | Singleton | Global Variable |
|---------|-----------|-----------------|
| Lazy initialization | ✅ Created when first needed | ❌ Created at startup |
| Controlled access | ✅ Through methods | ❌ Anyone can modify directly |
| Thread safety | ✅ Can be made thread-safe | ❌ Not inherently safe |
| Inheritance | ✅ Can be subclassed | ❌ Just a variable |

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Creational |
| **Intent** | Ensure one instance, global access |
| **Key Benefit** | Controlled shared resource |
| **Key Risk** | Testing difficulty, hidden dependencies |
| **Use When** | You need exactly ONE shared instance |
| **Avoid When** | Multiple instances are needed, or in heavy unit testing |
