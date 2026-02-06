"""
Chain of Responsibility Pattern
=================================
Passes a request along a chain of handlers. Each handler decides either
to process the request or pass it to the next handler in the chain.

Real-World Example: Customer Support Escalation
Think of calling customer support. First you talk to the automated system (Level 1),
if it can't help, you get a human agent (Level 2), then a supervisor (Level 3),
then a manager (Level 4). The call moves UP the chain until someone can help.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


# ---------------------------------------------------------------------------
# Real-World Example 1: Expense Approval System
# ---------------------------------------------------------------------------


class ApprovalStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"


@dataclass
class ExpenseRequest:
    """An expense request that needs approval."""
    employee: str
    amount: float
    description: str
    status: ApprovalStatus = ApprovalStatus.PENDING
    approved_by: str = ""


class ExpenseApprover(ABC):
    """
    Handler in the chain of responsibility.

    Real-life analogy:
        Think of a permission slip at school. If you need $5 for a field trip,
        your teacher can approve it. If it's $500 for new equipment, it goes
        to the principal. If it's $50,000 for renovation, it goes to the
        school board. Each person has a LIMIT on what they can approve.
    """

    def __init__(self) -> None:
        self._next_approver: ExpenseApprover | None = None

    def set_next(self, approver: ExpenseApprover) -> ExpenseApprover:
        """Set the next approver in the chain."""
        self._next_approver = approver
        return approver

    def handle(self, request: ExpenseRequest) -> ExpenseRequest:
        """Try to handle the request, or pass to next approver."""
        if self.can_approve(request):
            return self.approve(request)
        elif self._next_approver:
            print(f"    ➡️  {self.get_title()} can't approve ${request.amount:,.2f} — passing up...")
            return self._next_approver.handle(request)
        else:
            request.status = ApprovalStatus.REJECTED
            return request

    @abstractmethod
    def can_approve(self, request: ExpenseRequest) -> bool:
        ...

    @abstractmethod
    def approve(self, request: ExpenseRequest) -> ExpenseRequest:
        ...

    @abstractmethod
    def get_title(self) -> str:
        ...


class TeamLead(ExpenseApprover):
    """Can approve expenses up to $1,000."""

    def can_approve(self, request: ExpenseRequest) -> bool:
        return request.amount <= 1_000

    def approve(self, request: ExpenseRequest) -> ExpenseRequest:
        request.status = ApprovalStatus.APPROVED
        request.approved_by = "Team Lead"
        print(f"    ✅ Team Lead approved ${request.amount:,.2f} for {request.employee}")
        return request

    def get_title(self) -> str:
        return "Team Lead"


class DepartmentManager(ExpenseApprover):
    """Can approve expenses up to $10,000."""

    def can_approve(self, request: ExpenseRequest) -> bool:
        return request.amount <= 10_000

    def approve(self, request: ExpenseRequest) -> ExpenseRequest:
        request.status = ApprovalStatus.APPROVED
        request.approved_by = "Department Manager"
        print(f"    ✅ Manager approved ${request.amount:,.2f} for {request.employee}")
        return request

    def get_title(self) -> str:
        return "Department Manager"


class Director(ExpenseApprover):
    """Can approve expenses up to $50,000."""

    def can_approve(self, request: ExpenseRequest) -> bool:
        return request.amount <= 50_000

    def approve(self, request: ExpenseRequest) -> ExpenseRequest:
        request.status = ApprovalStatus.APPROVED
        request.approved_by = "Director"
        print(f"    ✅ Director approved ${request.amount:,.2f} for {request.employee}")
        return request

    def get_title(self) -> str:
        return "Director"


class CEO(ExpenseApprover):
    """Can approve any expense."""

    def can_approve(self, request: ExpenseRequest) -> bool:
        return True  # CEO can approve anything!

    def approve(self, request: ExpenseRequest) -> ExpenseRequest:
        request.status = ApprovalStatus.APPROVED
        request.approved_by = "CEO"
        print(f"    ✅ CEO approved ${request.amount:,.2f} for {request.employee}")
        return request

    def get_title(self) -> str:
        return "CEO"


# ---------------------------------------------------------------------------
# Real-World Example 2: Authentication & Authorization Pipeline
# ---------------------------------------------------------------------------


@dataclass
class AuthRequest:
    """A request that needs to pass through security checks."""
    username: str
    password: str
    ip_address: str
    user_agent: str
    errors: list[str] = None  # type: ignore

    def __post_init__(self):
        if self.errors is None:
            self.errors = []


class SecurityHandler(ABC):
    """Handler in the security chain."""

    def __init__(self) -> None:
        self._next: SecurityHandler | None = None

    def set_next(self, handler: SecurityHandler) -> SecurityHandler:
        self._next = handler
        return handler

    def handle(self, request: AuthRequest) -> bool:
        if not self.check(request):
            return False
        if self._next:
            return self._next.handle(request)
        return True  # All checks passed!

    @abstractmethod
    def check(self, request: AuthRequest) -> bool:
        ...


class IPWhitelistCheck(SecurityHandler):
    """Check if the IP address is not blacklisted."""

    _blacklisted_ips = {"192.168.1.100", "10.0.0.1"}

    def check(self, request: AuthRequest) -> bool:
        if request.ip_address in self._blacklisted_ips:
            request.errors.append(f"🚫 IP {request.ip_address} is blacklisted")
            print(f"    🚫 IP Check: BLOCKED — {request.ip_address}")
            return False
        print(f"    ✅ IP Check: {request.ip_address} is allowed")
        return True


class RateLimitCheck(SecurityHandler):
    """Check if the user hasn't exceeded request limits."""

    _request_counts: dict[str, int] = {}

    def check(self, request: AuthRequest) -> bool:
        count = self._request_counts.get(request.username, 0) + 1
        self._request_counts[request.username] = count
        if count > 5:
            request.errors.append("⏱️ Rate limit exceeded")
            print(f"    ⏱️ Rate Limit: BLOCKED — attempt #{count}")
            return False
        print(f"    ✅ Rate Limit: attempt #{count}/5 — OK")
        return True


class CredentialCheck(SecurityHandler):
    """Verify username and password."""

    _valid_credentials = {
        "alice": "password123",
        "bob": "secure456",
    }

    def check(self, request: AuthRequest) -> bool:
        valid_pass = self._valid_credentials.get(request.username)
        if valid_pass and valid_pass == request.password:
            print(f"    ✅ Credentials: Valid for {request.username}")
            return True
        request.errors.append("🔑 Invalid credentials")
        print(f"    ❌ Credentials: Invalid for {request.username}")
        return False


class BotDetectionCheck(SecurityHandler):
    """Check if the request looks like it's from a bot."""

    def check(self, request: AuthRequest) -> bool:
        if "bot" in request.user_agent.lower():
            request.errors.append("🤖 Bot detected")
            print(f"    🤖 Bot Detection: BLOCKED")
            return False
        print(f"    ✅ Bot Detection: Human detected")
        return True


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Chain of Responsibility pattern demonstration."""
    print("=" * 60)
    print("  CHAIN OF RESPONSIBILITY PATTERN DEMO")
    print("=" * 60)

    # --- Expense Approval Example ---
    print("\n💰 Example 1: Expense Approval Chain")
    print("-" * 50)

    # Build the chain: Team Lead → Manager → Director → CEO
    team_lead = TeamLead()
    manager = DepartmentManager()
    director = Director()
    ceo = CEO()

    team_lead.set_next(manager).set_next(director).set_next(ceo)

    expenses = [
        ExpenseRequest("Alice", 500, "Office supplies"),
        ExpenseRequest("Bob", 5_000, "New laptop"),
        ExpenseRequest("Charlie", 25_000, "Team offsite"),
        ExpenseRequest("Diana", 100_000, "New office furniture"),
    ]

    for expense in expenses:
        print(f"\n  📝 {expense.employee} requests ${expense.amount:,.2f} for: {expense.description}")
        result = team_lead.handle(expense)
        print(f"    Status: {result.status.value} (by {result.approved_by or 'N/A'})")

    # --- Authentication Pipeline Example ---
    print("\n\n🔐 Example 2: Authentication Security Chain")
    print("-" * 50)

    # Build security chain
    ip_check = IPWhitelistCheck()
    rate_limit = RateLimitCheck()
    creds_check = CredentialCheck()
    bot_check = BotDetectionCheck()

    ip_check.set_next(bot_check).set_next(rate_limit).set_next(creds_check)

    requests = [
        AuthRequest("alice", "password123", "203.0.113.1", "Mozilla/5.0"),
        AuthRequest("hacker", "wrong", "192.168.1.100", "Mozilla/5.0"),
        AuthRequest("bob", "secure456", "172.16.0.1", "GoogleBot/2.1"),
        AuthRequest("alice", "wrong_pass", "203.0.113.1", "Chrome/120"),
    ]

    for req in requests:
        print(f"\n  🔑 Login attempt: {req.username} from {req.ip_address}")
        result = ip_check.handle(req)
        print(f"    Result: {'✅ ACCESS GRANTED' if result else '❌ ACCESS DENIED'}")


if __name__ == "__main__":
    demo()
