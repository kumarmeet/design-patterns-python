"""
Decorator Pattern
==================
Adds new behavior to objects dynamically without altering their structure.
Wraps objects like layers of an onion — each layer adds something new.

Real-World Example: Coffee Shop Order System
Think of ordering coffee — you start with a basic coffee,
then ADD milk, ADD sugar, ADD whipped cream. Each addition
wraps around the original without changing it.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Real-World Example 1: Coffee Shop Order System
# ---------------------------------------------------------------------------


class Coffee(ABC):
    """Base coffee interface."""

    @abstractmethod
    def get_description(self) -> str:
        ...

    @abstractmethod
    def get_cost(self) -> float:
        ...


class BasicCoffee(Coffee):
    """A plain black coffee — the starting point."""

    def get_description(self) -> str:
        return "Basic Coffee"

    def get_cost(self) -> float:
        return 2.00


class CoffeeDecorator(Coffee, ABC):
    """Base decorator that wraps a Coffee."""

    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee


class MilkDecorator(CoffeeDecorator):
    """Adds milk to the coffee."""

    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + Milk"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50


class SugarDecorator(CoffeeDecorator):
    """Adds sugar to the coffee."""

    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + Sugar"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.25


class WhippedCreamDecorator(CoffeeDecorator):
    """Adds whipped cream to the coffee."""

    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + Whipped Cream"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.75


class CaramelDecorator(CoffeeDecorator):
    """Adds caramel drizzle to the coffee."""

    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + Caramel"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.60


# ---------------------------------------------------------------------------
# Real-World Example 2: Web Request Middleware Pipeline
# ---------------------------------------------------------------------------


class WebRequest:
    """A simple web request object."""

    def __init__(self, path: str, body: str = "", headers: dict | None = None) -> None:
        self.path = path
        self.body = body
        self.headers = headers or {}


class WebResponse:
    """A simple web response object."""

    def __init__(self, status: int = 200, body: str = "") -> None:
        self.status = status
        self.body = body
        self.headers: dict[str, str] = {}


class RequestHandler(ABC):
    """Base request handler."""

    @abstractmethod
    def handle(self, request: WebRequest) -> WebResponse:
        ...


class BasicHandler(RequestHandler):
    """Simply returns a success response."""

    def handle(self, request: WebRequest) -> WebResponse:
        return WebResponse(200, f"OK: Handled {request.path}")


class HandlerDecorator(RequestHandler, ABC):
    """Base decorator for request handlers (middleware)."""

    def __init__(self, handler: RequestHandler) -> None:
        self._handler = handler


class LoggingMiddleware(HandlerDecorator):
    """
    Logs every request before passing it to the next handler.

    Real-life analogy:
        Like a security camera at a store entrance —
        it records everyone who enters, but doesn't stop them.
    """

    def __init__(self, handler: RequestHandler) -> None:
        super().__init__(handler)
        self.logged_requests: list[str] = []

    def handle(self, request: WebRequest) -> WebResponse:
        log_entry = f"📝 LOG: {request.path}"
        self.logged_requests.append(log_entry)
        print(f"    {log_entry}")
        return self._handler.handle(request)


class AuthMiddleware(HandlerDecorator):
    """
    Checks if the request has a valid auth token.

    Real-life analogy:
        Like a bouncer at a club — checks your ID before letting you in.
    """

    def handle(self, request: WebRequest) -> WebResponse:
        token = request.headers.get("Authorization")
        if not token:
            print("    🔒 AUTH: No token — Access Denied!")
            return WebResponse(401, "Unauthorized: No auth token provided")
        print(f"    ✅ AUTH: Token found — Access Granted")
        return self._handler.handle(request)


class RateLimitMiddleware(HandlerDecorator):
    """
    Limits the number of requests per client.

    Real-life analogy:
        Like a theme park ride — only 10 people can ride at a time.
        Others have to wait in line.
    """

    def __init__(self, handler: RequestHandler, max_requests: int = 5) -> None:
        super().__init__(handler)
        self._max_requests = max_requests
        self._request_count = 0

    def handle(self, request: WebRequest) -> WebResponse:
        self._request_count += 1
        if self._request_count > self._max_requests:
            print(f"    ⛔ RATE LIMIT: Request #{self._request_count} blocked!")
            return WebResponse(429, "Too Many Requests")
        print(f"    🚦 RATE LIMIT: Request #{self._request_count}/{self._max_requests} — OK")
        return self._handler.handle(request)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Decorator pattern demonstration."""
    print("=" * 60)
    print("  DECORATOR PATTERN DEMO")
    print("=" * 60)

    # --- Coffee Shop Example ---
    print("\n☕ Example 1: Coffee Shop Orders")
    print("-" * 40)

    # Order 1: Simple coffee with milk
    coffee1: Coffee = BasicCoffee()
    coffee1 = MilkDecorator(coffee1)
    print(f"  Order 1: {coffee1.get_description()}")
    print(f"  Price: ${coffee1.get_cost():.2f}")

    # Order 2: Fancy coffee with everything!
    coffee2: Coffee = BasicCoffee()
    coffee2 = MilkDecorator(coffee2)
    coffee2 = SugarDecorator(coffee2)
    coffee2 = WhippedCreamDecorator(coffee2)
    coffee2 = CaramelDecorator(coffee2)
    print(f"\n  Order 2: {coffee2.get_description()}")
    print(f"  Price: ${coffee2.get_cost():.2f}")

    # Order 3: Double milk!
    coffee3: Coffee = BasicCoffee()
    coffee3 = MilkDecorator(coffee3)
    coffee3 = MilkDecorator(coffee3)  # Extra milk!
    print(f"\n  Order 3: {coffee3.get_description()}")
    print(f"  Price: ${coffee3.get_cost():.2f}")

    # --- Middleware Pipeline Example ---
    print("\n🌐 Example 2: Web Middleware Pipeline")
    print("-" * 40)

    # Build a handler with middleware layers (decorators)
    handler: RequestHandler = BasicHandler()
    handler = LoggingMiddleware(handler)
    handler = AuthMiddleware(handler)
    handler = RateLimitMiddleware(handler, max_requests=3)

    # Request WITH auth token
    print("\n  Request 1: With auth token")
    req1 = WebRequest("/api/users", headers={"Authorization": "Bearer abc123"})
    resp1 = handler.handle(req1)
    print(f"    Response: {resp1.status} — {resp1.body}")

    # Request WITHOUT auth token
    print("\n  Request 2: Without auth token")
    req2 = WebRequest("/api/secret")
    resp2 = handler.handle(req2)
    print(f"    Response: {resp2.status} — {resp2.body}")


if __name__ == "__main__":
    demo()
