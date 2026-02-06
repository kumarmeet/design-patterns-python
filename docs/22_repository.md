# 🗄️ Repository Pattern

## What Is It? (Explain Like I'm 10)

Imagine a **library**. When you want a book:
- You DON'T go into the warehouse and search through shelves yourself
- You ask the **librarian** (repository): "I want the Harry Potter book"
- The librarian finds it and gives it to you

You don't know WHERE the book was (shelf A? shelf B? digital?). You just asked, and got it.

That's the Repository pattern — a **librarian for your data**.

---

## 📖 Simple Definition

> The Repository pattern **abstracts data access logic** from business logic. It provides a collection-like interface for querying and persisting domain objects.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📚 Librarian | You ask for a book; they find it (you don't search the shelves) |
| 🏪 Store Clerk | You ask for an item; they get it from the stockroom |
| 📞 Phone Contact Book | You search by name; it finds the number (no matter how it's stored) |
| 🗂️ Filing Cabinet | You ask for a file by label; the system finds it |

---

## ✅ When to Use

- **Database-driven applications** — Separate SQL from business logic
- **Microservices** — Each service has its own data access layer
- **Domain-Driven Design** — Clean separation between domain and infrastructure
- **When data source might change** — Switch from PostgreSQL to MongoDB without touching business code
- **Unit testing** — Use in-memory repository in tests, real database in production

---

## ❌ When NOT to Use

- **Simple CRUD apps** — If your app just reads/writes to one table, a repository adds unnecessary abstraction
- **When using an ORM directly is fine** — ORMs like SQLAlchemy already provide repository-like features
- **Very small projects** — Added layers don't justify the simplicity needed

---

## 🔧 How It Works

```
Business Logic Layer        Repository Layer         Data Storage
       │                         │                       │
  UserService              UserRepository           Database
       │                         │                       │
  register_user()  ──►     repo.add(user)    ──►   INSERT INTO users
  find_user(id)    ──►     repo.find_by_id() ──►   SELECT * FROM users
  deactivate()     ──►     repo.update()     ──►   UPDATE users SET...
       │                         │                       │
  Business logic           Data access logic        Storage details
  (NO SQL here!)           (SQL/ORM here)           (PostgreSQL/MongoDB)
```

---

## 💻 Code Example

```python
from design_patterns.architectural.repository import (
    InMemoryUserRepository, User, UserService
)

# Create repository and service
repo = InMemoryUserRepository()
service = UserService(repo)

# Business logic doesn't know about storage!
alice = service.register_user("alice", "alice@example.com", "Alice Johnson")
bob = service.register_user("bob", "bob@example.com", "Bob Smith")

# Query through the repository
user = service.find_user(1)
all_users = service.get_all_users()

# Swap to a different database? Just change the repository!
# service = UserService(PostgresUserRepository())  # Same business logic!
```

---

## 🆚 With vs Without Repository

```python
# ❌ WITHOUT Repository (SQL mixed with business logic)
class UserService:
    def register_user(self, name, email):
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        # Business logic mixed with SQL!

# ✅ WITH Repository (clean separation)
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register_user(self, name, email):
        user = User(name=name, email=email)
        return self.repo.add(user)
        # No SQL here! The repo handles storage details.
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Architectural |
| **Intent** | Abstract data access from business logic |
| **Key Benefit** | Clean separation, easy database switching, testability |
| **Key Risk** | Over-abstraction for simple CRUD apps |
| **Use When** | Complex business logic, multiple data sources, testing needed |
| **Avoid When** | Simple CRUD, small projects, ORM is sufficient |
