# 🔌 Adapter Pattern

## What Is It? (Explain Like I'm 10)

Imagine you're traveling from India to the USA. Your phone charger has an Indian plug, but US sockets are different! You use a **travel adapter** — it doesn't change your charger or the socket, it just makes them work together.

That's the Adapter pattern! It's a **translator** between two things that don't normally fit together.

---

## 📖 Simple Definition

> The Adapter pattern allows **incompatible interfaces** to work together. It wraps an existing class with a new interface that the client expects.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 🔌 Travel Power Adapter | Indian plug + US socket = adapter makes them fit |
| 🌐 Language Translator | Person speaks French, you speak English — translator in between |
| 📱 USB-C to Headphone Jack | New phone, old headphones — adapter dongle connects them |
| 📋 Resume Format Converter | Your resume is in Word, but the job requires PDF — converter adapts it |

---

## ✅ When to Use

- **Third-party library integration** — Library has a different interface than your code expects
- **Payment gateway integration** — Stripe, PayPal, Razorpay all have different APIs, but your app needs ONE interface
- **Legacy system integration** — Old system returns CSV, new system needs JSON
- **API version migration** — Old API v1 and new API v2 have different response formats
- **Multiple vendor SDKs** — Same functionality, different method names

---

## ❌ When NOT to Use

- **When you can modify the source** — If you control both interfaces, just make them compatible directly
- **When interfaces are already compatible** — Don't add unnecessary layers
- **Too many adapters** — If you have adapters for adapters, redesign your system

---

## 🔧 How It Works

```
Your App ──► PaymentGateway (your interface)
                    │
            ┌───────┼────────┐
            │       │        │
     StripeAdapter  │   RazorpayAdapter
            │       │        │
       StripeAPI  PayPal   RazorpayClient
     (different   SDK     (different
      interface)  (different  interface)
                  interface)
```

---

## 💻 Code Example

```python
from design_patterns.structural.adapter import (
    StripeAdapter, PayPalAdapter, RazorpayAdapter, PaymentGateway
)

# All adapters share the SAME interface!
gateways: list[PaymentGateway] = [
    StripeAdapter(),
    PayPalAdapter(),
    RazorpayAdapter(),
]

# SAME code works with ALL payment providers
for gateway in gateways:
    result = gateway.charge(49.99)
    print(f"{result.provider}: {result.message}")
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Structural |
| **Intent** | Make incompatible interfaces work together |
| **Key Benefit** | Reuse existing code without modification |
| **Key Risk** | Too many adapters = complexity |
| **Use When** | Integrating with external/legacy systems |
| **Avoid When** | You can modify the source directly |
