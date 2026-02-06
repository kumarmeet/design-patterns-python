"""
Builder Pattern
================
Constructs complex objects step by step.
Separates construction from representation.

Real-World Example: Building a meal order at a restaurant.
You pick your main dish, then your drink, then your dessert — step by step.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Self


# ---------------------------------------------------------------------------
# Real-World Example 1: HTTP Request Builder
# ---------------------------------------------------------------------------


@dataclass
class HttpRequest:
    """Represents an HTTP request with all its parts."""
    method: str = "GET"
    url: str = ""
    headers: dict[str, str] = field(default_factory=dict)
    query_params: dict[str, str] = field(default_factory=dict)
    body: str | dict | None = None
    timeout: int = 30
    retries: int = 0
    auth_token: str | None = None

    def __str__(self) -> str:
        parts = [
            f"  Method: {self.method}",
            f"  URL: {self.url}",
            f"  Headers: {self.headers}",
            f"  Query Params: {self.query_params}",
            f"  Body: {self.body}",
            f"  Timeout: {self.timeout}s",
            f"  Retries: {self.retries}",
            f"  Auth: {'✅ Set' if self.auth_token else '❌ None'}",
        ]
        return "\n".join(parts)


class HttpRequestBuilder:
    """
    Builds HTTP requests step by step.

    Real-life analogy:
        Think of ordering a custom sandwich at Subway.
        You start with bread, then pick meat, veggies, sauce —
        each step is optional, and you build exactly what you want.

    Usage:
        request = (
            HttpRequestBuilder()
            .set_method("POST")
            .set_url("https://api.example.com/users")
            .add_header("Content-Type", "application/json")
            .set_body({"name": "Alice"})
            .set_timeout(10)
            .build()
        )
    """

    def __init__(self) -> None:
        self._request = HttpRequest()

    def set_method(self, method: str) -> Self:
        """Set HTTP method (GET, POST, PUT, DELETE, etc.)."""
        self._request.method = method.upper()
        return self

    def set_url(self, url: str) -> Self:
        """Set the request URL."""
        self._request.url = url
        return self

    def add_header(self, key: str, value: str) -> Self:
        """Add a header to the request."""
        self._request.headers[key] = value
        return self

    def add_query_param(self, key: str, value: str) -> Self:
        """Add a query parameter."""
        self._request.query_params[key] = value
        return self

    def set_body(self, body: str | dict) -> Self:
        """Set the request body."""
        self._request.body = body
        return self

    def set_timeout(self, seconds: int) -> Self:
        """Set the timeout in seconds."""
        self._request.timeout = seconds
        return self

    def set_retries(self, count: int) -> Self:
        """Set number of retry attempts."""
        self._request.retries = count
        return self

    def set_auth_token(self, token: str) -> Self:
        """Set the authentication token."""
        self._request.auth_token = token
        self._request.headers["Authorization"] = f"Bearer {token}"
        return self

    def build(self) -> HttpRequest:
        """Build and return the final HttpRequest object."""
        if not self._request.url:
            raise ValueError("URL is required to build an HTTP request")
        return self._request


# ---------------------------------------------------------------------------
# Real-World Example 2: User Profile Builder
# ---------------------------------------------------------------------------


@dataclass
class UserProfile:
    """A user profile with many optional fields."""
    username: str = ""
    email: str = ""
    first_name: str = ""
    last_name: str = ""
    age: int | None = None
    phone: str = ""
    address: str = ""
    bio: str = ""
    is_premium: bool = False
    preferences: dict[str, str] = field(default_factory=dict)

    def __str__(self) -> str:
        parts = [f"  {k}: {v}" for k, v in self.__dict__.items() if v]
        return "\n".join(parts)


class UserProfileBuilder:
    """
    Builds a user profile step by step.

    Real-life analogy:
        Think of filling out a form to sign up for a website.
        Some fields are required (username, email),
        and some are optional (bio, phone). You fill them one by one.
    """

    def __init__(self, username: str, email: str) -> None:
        """Username and email are required — the rest is optional."""
        self._profile = UserProfile(username=username, email=email)

    def set_name(self, first: str, last: str) -> Self:
        self._profile.first_name = first
        self._profile.last_name = last
        return self

    def set_age(self, age: int) -> Self:
        self._profile.age = age
        return self

    def set_phone(self, phone: str) -> Self:
        self._profile.phone = phone
        return self

    def set_address(self, address: str) -> Self:
        self._profile.address = address
        return self

    def set_bio(self, bio: str) -> Self:
        self._profile.bio = bio
        return self

    def set_premium(self, is_premium: bool = True) -> Self:
        self._profile.is_premium = is_premium
        return self

    def add_preference(self, key: str, value: str) -> Self:
        self._profile.preferences[key] = value
        return self

    def build(self) -> UserProfile:
        """Build and return the UserProfile."""
        return self._profile


# ---------------------------------------------------------------------------
# Real-World Example 3: Pizza Order Builder (Fun Example!)
# ---------------------------------------------------------------------------


@dataclass
class Pizza:
    """A pizza with customizable options."""
    size: str = "medium"
    crust: str = "regular"
    sauce: str = "tomato"
    cheese: str = "mozzarella"
    toppings: list[str] = field(default_factory=list)
    is_extra_cheese: bool = False
    special_instructions: str = ""

    def __str__(self) -> str:
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return (
            f"  🍕 {self.size.title()} pizza on {self.crust} crust\n"
            f"  Sauce: {self.sauce} | Cheese: {self.cheese}"
            f"{' + EXTRA!' if self.is_extra_cheese else ''}\n"
            f"  Toppings: {toppings_str}\n"
            f"  Notes: {self.special_instructions or 'None'}"
        )


class PizzaBuilder:
    """
    Build your perfect pizza, one choice at a time!

    Real-life analogy:
        Ordering a custom pizza at Domino's — you pick size,
        crust, sauce, cheese, and toppings step by step.
    """

    def __init__(self) -> None:
        self._pizza = Pizza()

    def set_size(self, size: str) -> Self:
        self._pizza.size = size
        return self

    def set_crust(self, crust: str) -> Self:
        self._pizza.crust = crust
        return self

    def set_sauce(self, sauce: str) -> Self:
        self._pizza.sauce = sauce
        return self

    def set_cheese(self, cheese: str) -> Self:
        self._pizza.cheese = cheese
        return self

    def add_topping(self, topping: str) -> Self:
        self._pizza.toppings.append(topping)
        return self

    def extra_cheese(self) -> Self:
        self._pizza.is_extra_cheese = True
        return self

    def add_instructions(self, notes: str) -> Self:
        self._pizza.special_instructions = notes
        return self

    def build(self) -> Pizza:
        return self._pizza


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Builder pattern demonstration."""
    print("=" * 60)
    print("  BUILDER PATTERN DEMO")
    print("=" * 60)

    # --- HTTP Request Builder ---
    print("\n🌐 Example 1: HTTP Request Builder")
    print("-" * 40)

    request = (
        HttpRequestBuilder()
        .set_method("POST")
        .set_url("https://api.example.com/users")
        .add_header("Content-Type", "application/json")
        .add_header("Accept", "application/json")
        .set_body({"name": "Alice", "email": "alice@example.com"})
        .set_auth_token("my-secret-token-123")
        .set_timeout(10)
        .set_retries(3)
        .build()
    )
    print(request)

    # --- User Profile Builder ---
    print("\n👤 Example 2: User Profile Builder")
    print("-" * 40)

    profile = (
        UserProfileBuilder("alice_dev", "alice@example.com")
        .set_name("Alice", "Johnson")
        .set_age(28)
        .set_bio("Full-stack developer who loves Python 🐍")
        .set_premium()
        .add_preference("theme", "dark")
        .add_preference("language", "en")
        .build()
    )
    print(profile)

    # --- Pizza Builder ---
    print("\n🍕 Example 3: Pizza Order Builder")
    print("-" * 40)

    pizza = (
        PizzaBuilder()
        .set_size("large")
        .set_crust("thin")
        .set_sauce("bbq")
        .add_topping("chicken")
        .add_topping("onions")
        .add_topping("peppers")
        .extra_cheese()
        .add_instructions("Cut into 8 slices please")
        .build()
    )
    print(pizza)


if __name__ == "__main__":
    demo()
