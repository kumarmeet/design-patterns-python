# 🔗 Chain of Responsibility Pattern

## What Is It? (Explain Like I'm 10)

Imagine you have a **question at school**:
1. First, you ask your **classmate** — if they know, great!
2. If not, you ask your **teacher**
3. If the teacher doesn't know, you ask the **principal**
4. If the principal doesn't know, you ask the **school board**

The question moves **up the chain** until someone can answer it. That's Chain of Responsibility!

---

## 📖 Simple Definition

> The Chain of Responsibility pattern passes a request along a **chain of handlers**. Each handler decides either to **process** the request or **pass it** to the next handler in the chain.

---

## 🏠 Real-Life Analogies

| Analogy | Explanation |
|---------|-------------|
| 📞 Customer Support | Automated system → Agent → Supervisor → Manager |
| 💰 Expense Approval | Team Lead ($1K) → Manager ($10K) → Director ($50K) → CEO (unlimited) |
| 🔐 Security Checks | IP check → Rate limit → Password check → 2FA |
| 📋 Bug Report | Junior dev → Senior dev → Tech lead → Architect |

---

## ✅ When to Use

- **Expense/approval workflows** — Different approval levels based on amount
- **Authentication pipelines** — Multiple security checks in sequence
- **Middleware chains** — Web request processing (logging → auth → rate limit → handler)
- **Event handling** — Try one handler, if it can't handle it, try the next
- **Help desk escalation** — Escalate issues through support tiers

---

## ❌ When NOT to Use

- **When every request needs all handlers** — If ALL handlers must process every request, use Decorator instead
- **Simple direct routing** — If you always know which handler to use, call it directly
- **Performance-critical paths** — Walking through a chain adds latency
- **When the chain might have no handler** — Request could fall through with no response

---

## 💻 Code Example

```python
from design_patterns.behavioral.chain_of_responsibility import (
    TeamLead, DepartmentManager, Director, CEO, ExpenseRequest
)

# Build the chain
team_lead = TeamLead()
manager = DepartmentManager()
director = Director()
ceo = CEO()

team_lead.set_next(manager).set_next(director).set_next(ceo)

# Requests flow through the chain
expense = ExpenseRequest("Alice", 500, "Office supplies")
team_lead.handle(expense)   # Team Lead approves (under $1,000)

expense2 = ExpenseRequest("Bob", 25000, "Team retreat")
team_lead.handle(expense2)  # Passes to Manager → Director approves
```

---

## 📚 Summary

| Aspect | Details |
|--------|---------|
| **Category** | Behavioral |
| **Intent** | Pass requests along a chain of handlers |
| **Key Benefit** | Flexible, decoupled request handling |
| **Key Risk** | Request might not be handled at all |
| **Use When** | Multiple handlers, dynamic processing |
| **Avoid When** | You always know which handler to use |
