"""
Bridge Pattern
===============
Separates an abstraction from its implementation so the two can vary independently.

Real-World Example: Remote Control + Device
Think of it like a TV remote. The remote is the "abstraction" and the TV is
the "implementation." You can use the SAME remote concept with different TVs,
and you can have different remotes for the SAME TV.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Real-World Example 1: Notification System (Message + Channel)
# ---------------------------------------------------------------------------


class NotificationChannel(ABC):
    """
    Implementation: HOW the message is delivered.

    Real-life analogy:
        This is the delivery truck. It knows HOW to deliver (by road, by air, etc.)
        but doesn't care WHAT'S in the package.
    """

    @abstractmethod
    def send(self, title: str, body: str, recipient: str) -> str:
        ...


class EmailChannel(NotificationChannel):
    def send(self, title: str, body: str, recipient: str) -> str:
        return f"📧 Email to {recipient}: [{title}] {body}"


class SMSChannel(NotificationChannel):
    def send(self, title: str, body: str, recipient: str) -> str:
        return f"📱 SMS to {recipient}: {title} — {body}"


class SlackChannel(NotificationChannel):
    def send(self, title: str, body: str, recipient: str) -> str:
        return f"💬 Slack to #{recipient}: *{title}* — {body}"


class PushChannel(NotificationChannel):
    def send(self, title: str, body: str, recipient: str) -> str:
        return f"🔔 Push to {recipient}: {title}"


class Notification(ABC):
    """
    Abstraction: WHAT kind of notification it is.

    Real-life analogy:
        This is the package. It knows WHAT it contains (urgent letter, birthday card)
        but doesn't care HOW it's delivered.
    """

    def __init__(self, channel: NotificationChannel) -> None:
        self._channel = channel

    @abstractmethod
    def notify(self, recipient: str) -> str:
        ...


class AlertNotification(Notification):
    """Urgent alert — something went wrong!"""

    def __init__(self, channel: NotificationChannel, alert_message: str) -> None:
        super().__init__(channel)
        self._message = alert_message

    def notify(self, recipient: str) -> str:
        return self._channel.send("🚨 ALERT", self._message, recipient)


class ReminderNotification(Notification):
    """Gentle reminder."""

    def __init__(self, channel: NotificationChannel, reminder: str) -> None:
        super().__init__(channel)
        self._reminder = reminder

    def notify(self, recipient: str) -> str:
        return self._channel.send("⏰ Reminder", self._reminder, recipient)


class PromotionalNotification(Notification):
    """Marketing / promotional message."""

    def __init__(self, channel: NotificationChannel, promo: str, discount: int) -> None:
        super().__init__(channel)
        self._promo = promo
        self._discount = discount

    def notify(self, recipient: str) -> str:
        return self._channel.send(
            f"🎉 {self._discount}% OFF!",
            self._promo,
            recipient,
        )


# ---------------------------------------------------------------------------
# Real-World Example 2: Shape + Renderer (Drawing System)
# ---------------------------------------------------------------------------


class Renderer(ABC):
    """Implementation: HOW to draw."""

    @abstractmethod
    def render_circle(self, radius: float) -> str:
        ...

    @abstractmethod
    def render_rectangle(self, width: float, height: float) -> str:
        ...


class SVGRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"<svg><circle r='{radius}'/></svg>"

    def render_rectangle(self, width: float, height: float) -> str:
        return f"<svg><rect width='{width}' height='{height}'/></svg>"


class CanvasRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"ctx.arc(0, 0, {radius}, 0, 2*PI); ctx.fill();"

    def render_rectangle(self, width: float, height: float) -> str:
        return f"ctx.fillRect(0, 0, {width}, {height});"


class Shape(ABC):
    """Abstraction: WHAT shape to draw."""

    def __init__(self, renderer: Renderer) -> None:
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> str:
        ...


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float) -> None:
        super().__init__(renderer)
        self._radius = radius

    def draw(self) -> str:
        return self._renderer.render_circle(self._radius)


class Rectangle(Shape):
    def __init__(self, renderer: Renderer, width: float, height: float) -> None:
        super().__init__(renderer)
        self._width = width
        self._height = height

    def draw(self) -> str:
        return self._renderer.render_rectangle(self._width, self._height)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Bridge pattern demonstration."""
    print("=" * 60)
    print("  BRIDGE PATTERN DEMO")
    print("=" * 60)

    # --- Notification Example ---
    print("\n🔔 Example 1: Notification System")
    print("-" * 40)
    print("  Same notification type, different channels:\n")

    channels: list[NotificationChannel] = [
        EmailChannel(),
        SMSChannel(),
        SlackChannel(),
        PushChannel(),
    ]

    # Send alert via ALL channels
    for channel in channels:
        alert = AlertNotification(channel, "Server CPU at 95%!")
        print(f"  {alert.notify('ops-team')}")

    print()

    # Send promo via email and SMS only
    for channel in [EmailChannel(), SMSChannel()]:
        promo = PromotionalNotification(channel, "Summer sale on all items!", 30)
        print(f"  {promo.notify('customers')}")

    # --- Shape + Renderer Example ---
    print("\n\n🎨 Example 2: Shape Drawing System")
    print("-" * 40)

    svg = SVGRenderer()
    canvas = CanvasRenderer()

    shapes = [
        ("SVG Circle", Circle(svg, 50)),
        ("Canvas Circle", Circle(canvas, 50)),
        ("SVG Rectangle", Rectangle(svg, 100, 60)),
        ("Canvas Rectangle", Rectangle(canvas, 100, 60)),
    ]

    for label, shape in shapes:
        print(f"  {label}: {shape.draw()}")


if __name__ == "__main__":
    demo()
