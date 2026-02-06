# 🔐 Proxy Pattern

## What Is It? (Explain Like I'm 10)

Imagine you want to enter a **building**. There's a **security guard** at the door. The guard:
- Checks your ID before letting you in (**Protection Proxy**)
- Writes down when you entered in a logbook (**Logging Proxy**)
- Sometimes says "the boss isn't in yet, come back later" (**Virtual/Lazy Proxy**)

The guard doesn't DO the work — the people inside the building do. But the guard **controls access** to them.

---

## 📖 Simple Definition

> The Proxy pattern provides a **substitute or placeholder** for another object. It controls access to the original object, adding behavior like security checks, caching, or lazy loading.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🔒 Security Guard | Checks your access before letting you in |
| 💳 Credit Card | A proxy for your bank account — you don't carry cash |
| 📋 Secretary | Filters who can meet the CEO |
| 🗂️ Bookmark | A proxy for a web page — quick access without loading the full page |

---

## Types of Proxies

| Type | What It Does | Example |
|------|-------------|---------|
| **Protection Proxy** | Controls access based on permissions | Website firewall blocking dangerous sites |
| **Caching Proxy** | Stores results to avoid repeated expensive operations | Weather API cache |
| **Virtual/Lazy Proxy** | Delays creation until actually needed | Loading images only when scrolled to |
| **Logging Proxy** | Records all access for monitoring | API request logger |

---

## ✅ When to Use

- **Access control** — Block certain users/IPs from accessing resources
- **Caching** — Cache expensive API calls or database queries
- **Lazy loading** — Don't load heavy resources until needed (images, files)
- **Logging/Monitoring** — Track all access to a resource
- **Rate limiting** — Control how often a resource is accessed

---

## ❌ When NOT to Use

- **Simple direct access** — If there's no need for control, a proxy adds overhead
- **Performance-critical paths** — The extra layer adds latency
- **When it overcomplicates things** — Don't add proxies "just in case"

---

## 💻 Code Example

```python
from design_patterns.structural.proxy import CachingWeatherProxy

# Caching proxy — first call hits the API, repeat calls use cache
weather = CachingWeatherProxy(cache_ttl_seconds=300)

data1 = weather.get_weather("New York")   # Cache MISS → calls real API
data2 = weather.get_weather("New York")   # Cache HIT → returns cached data!
data3 = weather.get_weather("London")     # Cache MISS → calls real API

stats = weather.get_stats()
print(stats)  # {"cache_hits": 1, "cache_misses": 2, "real_api_calls": 2}
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Structural |
| **Intent** | Control access to another object |
| **Key Benefit** | Security, caching, lazy loading, logging |
| **Key Risk** | Added complexity and latency |
| **Use When** | You need to control or enhance access to an object |
| **Avoid When** | Direct access is sufficient |
