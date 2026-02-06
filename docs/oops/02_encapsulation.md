# 🔒 Encapsulation — Protecting Your Data

## What Is It?

Encapsulation means **bundling data and methods together** inside a class, and **controlling who can access or change** that data.

### 🥤 Think of It Like This (For a 10-Year-Old)

Imagine a **vending machine**:
- You can **press buttons** (public methods) to get a drink.
- You **CAN'T open** the machine and grab the money inside (private data).
- The machine **protects** its cash and drinks behind a locked panel.

Your class is the vending machine. The buttons are public methods. The money inside is private data.

---

## Python's Access Levels

| Prefix | Level | Who Can Access? | Example |
|--------|-------|----------------|---------|
| `none` | **Public** | Anyone, anywhere | `self.name` |
| `_` | **Protected** | Class & subclasses (convention) | `self._battery` |
| `__` | **Private** | Only the class itself (name mangling) | `self.__password` |

> ⚠️ Python doesn't have TRUE private like Java/C++. The `__` prefix uses "name mangling" to make it harder to access, but it's still possible with `obj._ClassName__attribute`.

---

## Key Concepts

### 1. **Properties** (`@property`)
The best way to control access in Python!

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter — read the value."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter — validate before setting."""
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
```

Now you can use it like a regular attribute, but with validation:
```python
temp = Temperature(25)
temp.celsius = 100    # ✅ Uses the setter (validated!)
temp.celsius = -300   # ❌ Raises ValueError!
```

### 2. **Read-Only Properties**
Just define a getter without a setter:
```python
@property
def account_balance(self):
    return self._balance  # Can read, but can't set from outside!
```

### 3. **Data Validation**
Encapsulation lets you ensure data is always valid:
```python
@email.setter
def email(self, value):
    if "@" not in value:
        raise ValueError("Invalid email!")
    self._email = value
```

---

## Why Learn This?

Encapsulation prevents **accidental data corruption**. Without it, anyone could set a bank balance to -$999,999 or change a password without verification. Design patterns like **Singleton**, **Proxy**, and **Facade** heavily rely on encapsulation.

---

## When to Use

✅ When you have data that should be **validated** before changing (email, password, age)
✅ When you want to **hide complex internal state** from users of your class
✅ When you need **read-only** attributes
✅ When internal changes shouldn't affect external code

## When NOT to Use

❌ Don't make EVERYTHING private — if data is simple and doesn't need protection, keep it public.
❌ Don't overuse getters/setters for simple attributes — that's Java-style, not Pythonic.

---

## Run the Example

```bash
uv run python -m src.oops_concepts.encapsulation
```
