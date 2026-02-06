# 🌳 Composite Pattern

## What Is It? (Explain Like I'm 10)

Think of a **folder on your computer**. A folder can contain:
- **Files** (individual items)
- **Other folders** (which can contain more files and folders!)

You can ask "what's the size?" of a single file OR an entire folder. The folder automatically adds up all the sizes of everything inside it.

That's the Composite pattern — treating **individual items** and **groups of items** the **same way**.

---

## 📖 Simple Definition

> The Composite pattern composes objects into **tree structures** to represent part-whole hierarchies. It lets clients treat individual objects and collections of objects **uniformly**.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📁 File System | Files and folders — folders contain files AND other folders |
| 🏢 Company Org Chart | CEO → VPs → Managers → Employees (tree structure) |
| 📦 Boxes in Boxes | A box can contain items or smaller boxes |
| 🍽️ Menu | Categories contain items or sub-categories |

---

## ✅ When to Use

- **File system representation** — Files and folders
- **Organization hierarchies** — Companies, school districts, military ranks
- **UI component trees** — Panels contain buttons, which contain text
- **Menu systems** — Categories with items and sub-categories
- **Mathematical expressions** — `(3 + 5) * 2` → tree of operations

---

## ❌ When NOT to Use

- **Flat data** — If there's no hierarchy, Composite is overkill
- **When leaf and composite behave very differently** — If the operations don't make sense for both, don't force it
- **Simple lists** — A regular list is enough if items don't contain other items

---

## 💻 Code Example

```python
from design_patterns.structural.composite import File, Folder

root = Folder("project")

src = Folder("src")
src.add(File("main.py", 15))
src.add(File("utils.py", 8))

root.add(src)
root.add(File("README.md", 5))

print(root.display())     # Shows tree structure
print(root.get_size())    # 28 KB (adds up all files!)
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Structural |
| **Intent** | Treat individual objects and groups uniformly |
| **Key Benefit** | Simplifies tree structure operations |
| **Key Risk** | Hard to restrict what can contain what |
| **Use When** | Data naturally forms a tree/hierarchy |
| **Avoid When** | Data is flat with no nesting |
