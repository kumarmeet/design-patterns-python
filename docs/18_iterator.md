# 🔄 Iterator Pattern

## What Is It? (Explain Like I'm 10)

Imagine you're reading a **book**. You don't need to know how the pages are glued together or how the printer made it. You just **flip to the next page**.

That's the Iterator pattern — it gives you a simple way to go through items **one by one**, without knowing how they're stored inside.

---

## 📖 Simple Definition

> The Iterator pattern provides a way to **access elements** of a collection **sequentially** without exposing its underlying representation.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📖 Reading a Book | Flip pages one by one — don't care how they're bound |
| 🎵 Music Playlist | Press Next/Previous — don't care if songs are in an array or database |
| 📺 TV Channel Surfing | Channel up/down — don't care how channels are stored |
| 📜 Scrolling Social Media | Swipe for next post — don't care about the backend |

---

## ✅ When to Use

- **Custom collections** — Provide a standard way to iterate over your data structure
- **Multiple traversal methods** — Forward, reverse, shuffle, filtered
- **Paginated results** — Iterate through pages of API results
- **Lazy loading** — Load items one at a time instead of all at once
- **Tree/graph traversal** — Depth-first, breadth-first iterations

---

## ❌ When NOT to Use

- **Simple lists/arrays** — Python's built-in iteration is already great
- **When you need random access** — Iterators go one direction; use indexing instead
- **When the collection is small** — Overhead isn't worth it for tiny collections

---

## 💻 Code Example

```python
from design_patterns.behavioral.iterator import Playlist, Song

playlist = Playlist("My Favorites")
playlist.add_song(Song("Bohemian Rhapsody", "Queen", 355))
playlist.add_song(Song("Imagine", "John Lennon", 187))

# Normal iteration
for song in playlist:
    print(song)

# Reverse iteration
for song in playlist.reverse_iterator():
    print(song)

# Shuffle iteration
for song in playlist.shuffle_iterator():
    print(song)
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Sequential access without exposing internals |
| **Key Benefit** | Uniform traversal, multiple traversal methods |
| **Key Risk** | Overhead for simple collections |
| **Use When** | Custom collections, multiple traversal modes |
| **Avoid When** | Standard Python iteration is sufficient |
