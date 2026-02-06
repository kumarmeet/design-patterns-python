# 🌉 Bridge Pattern

## What Is It? (Explain Like I'm 10)

Imagine you have **different types of messages** (alert, reminder, promo) and **different ways to send them** (email, SMS, push notification).

WITHOUT Bridge: You'd need AlertEmail, AlertSMS, AlertPush, ReminderEmail, ReminderSMS, ReminderPush... that's 9 classes for just 3×3!

WITH Bridge: You have 3 message types + 3 channels = 6 classes. **Mix and match** any message with any channel!

---

## 📖 Simple Definition

> The Bridge pattern separates an **abstraction** (what something IS) from its **implementation** (how it's DONE), so both can vary independently.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📺 Remote + TV | Any remote can work with any TV brand |
| 🎨 Shape + Color | Any shape (circle, square) can be any color (red, blue) |
| 🚗 Car + Engine | Any car body can have any engine type |
| 📨 Message + Delivery Method | Any message type can use any delivery channel |

---

## ✅ When to Use

- **Multiple dimensions of variation** — Message type × Channel, Shape × Renderer
- **Platform independence** — Same app logic, different OS-specific implementations
- **Driver systems** — Same interface, different hardware drivers
- **When inheritance leads to class explosion** — Too many combinations

---

## ❌ When NOT to Use

- **Single dimension of variation** — If only one thing varies, use simple inheritance
- **Tight coupling is acceptable** — When abstraction and implementation always go together
- **Simple scenarios** — Over-engineering for small applications

---

## 💻 Code Example

```python
from design_patterns.structural.bridge import (
    EmailChannel, SMSChannel, SlackChannel,
    AlertNotification, ReminderNotification, PromotionalNotification
)

# Mix ANY notification type with ANY channel!
alert_email = AlertNotification(EmailChannel(), "Server down!")
alert_sms = AlertNotification(SMSChannel(), "Server down!")
promo_slack = PromotionalNotification(SlackChannel(), "Summer sale!", 30)

print(alert_email.notify("ops-team"))
print(alert_sms.notify("on-call"))
print(promo_slack.notify("general"))
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Structural |
| **Intent** | Separate abstraction from implementation |
| **Key Benefit** | Avoids class explosion, mix-and-match |
| **Key Risk** | Added complexity for simple cases |
| **Use When** | Multiple independent dimensions of variation |
| **Avoid When** | Only one dimension varies |
