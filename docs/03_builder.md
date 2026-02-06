# 🧩 Builder Pattern

## What Is It? (Explain Like I'm 10)

Imagine you're at **Subway** making a sandwich. You don't get a pre-made sandwich. Instead, you build it step by step:
1. Pick your bread 🍞
2. Pick your meat 🥩
3. Pick your veggies 🥬
4. Pick your sauce 🧴

Some steps are required, some are optional. You build EXACTLY what you want!

That's the Builder pattern — constructing something complex **one step at a time**.

---

## 📖 Simple Definition

> The Builder pattern constructs complex objects step by step. It separates the construction of an object from its representation, allowing the same construction process to create different representations.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🥪 Subway Sandwich | Choose bread → meat → veggies → sauce, step by step |
| 🏠 Building a House | Foundation → walls → roof → paint → furniture |
| 🍕 Custom Pizza | Size → crust → sauce → toppings → extras |
| 📝 Fill Out a Form | Name → email → phone (optional) → address (optional) |

---

## ✅ When to Use

- **Complex API request objects** — Many headers, params, body, auth tokens
- **Configuration objects** — Database config with host, port, user, password, pool size
- **UI components** — Dialogs with title, message, buttons, icon, theme
- **Query builders** — SQL queries with SELECT, WHERE, JOIN, ORDER BY
- **Email builders** — To, CC, BCC, subject, body, attachments

---

## ❌ When NOT to Use

- **Simple objects** — If your object only has 1-2 fields, a constructor is fine
- **Immutable data** — If the object never changes after creation, `dataclass` or `namedtuple` might be enough
- **When parameters are always required** — If ALL fields are mandatory, a regular constructor works better

---

## 🔧 How It Works

```
Builder                          Product
  │                                │
  ├─ set_method("POST")           │
  ├─ set_url("https://...")       │
  ├─ add_header("Auth", "...")    │
  ├─ set_body({...})              │
  ├─ set_timeout(10)              │
  │                                │
  ├─ build() ─────────────────────► HttpRequest
  │                                │  method: POST
                                   │  url: https://...
                                   │  headers: {Auth: ...}
                                   │  body: {...}
                                   │  timeout: 10
```

---

## 💻 Code Example

```python
from design_patterns.creational.builder import HttpRequestBuilder

# Build a complex request step by step
request = (
    HttpRequestBuilder()
    .set_method("POST")
    .set_url("https://api.example.com/users")
    .add_header("Content-Type", "application/json")
    .set_body({"name": "Alice"})
    .set_auth_token("secret-token")
    .set_timeout(10)
    .set_retries(3)
    .build()
)

print(request)
```

---

## 🆚 Builder vs Constructor

```python
# ❌ Telescoping Constructor (hard to read!)
request = HttpRequest("POST", "https://api.com", {"Auth": "..."}, 
                      {"page": "1"}, '{"name": "Alice"}', 10, 3, "token")

# ✅ Builder (clear and readable!)
request = (
    HttpRequestBuilder()
    .set_method("POST")
    .set_url("https://api.com")
    .set_body({"name": "Alice"})
    .set_timeout(10)
    .build()
)
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Creational |
| **Intent** | Construct complex objects step by step |
| **Key Benefit** | Readable, flexible object construction |
| **Key Risk** | Over-engineering for simple objects |
| **Use When** | Many optional parameters, complex construction |
| **Avoid When** | Object is simple with few required fields |
