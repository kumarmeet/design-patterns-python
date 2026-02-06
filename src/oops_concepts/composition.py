"""
Composition vs Inheritance — "Has-A" vs "Is-A"
=================================================
Composition means building complex objects by combining simpler ones.
Instead of saying "A is a B" (inheritance), you say "A has a B" (composition).

Real-World Analogy:
    Inheritance: "A Tesla IS A Car" (Tesla inherits from Car)
    Composition: "A Car HAS AN Engine, HAS Wheels, HAS a GPS"

    Composition is often BETTER because you can swap parts easily.
    You can't swap your parents, but you can swap your car's tires! 🛞
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# The Problem with Inheritance (Why Composition is Often Better)
# ---------------------------------------------------------------------------


# ❌ INHERITANCE APPROACH (gets messy fast!)
# Imagine: Robot that can walk, swim, and fly.
#
# class Walker: ...
# class Swimmer: ...
# class Flyer: ...
#
# class WalkingSwimmingRobot(Walker, Swimmer): ...
# class WalkingFlyingRobot(Walker, Flyer): ...
# class SwimmingFlyingRobot(Swimmer, Flyer): ...
# class WalkingSwimmingFlyingRobot(Walker, Swimmer, Flyer): ...
#
# 😱 Class explosion! And adding a new ability means EVEN MORE classes!


# ✅ COMPOSITION APPROACH (clean and flexible!)


class MovementAbility(ABC):
    """Interface for a movement ability."""

    @abstractmethod
    def move(self) -> str:
        ...

    @abstractmethod
    def get_name(self) -> str:
        ...


class WalkAbility(MovementAbility):
    def move(self) -> str:
        return "🚶 Walking on the ground"

    def get_name(self) -> str:
        return "Walk"


class SwimAbility(MovementAbility):
    def move(self) -> str:
        return "🏊 Swimming through water"

    def get_name(self) -> str:
        return "Swim"


class FlyAbility(MovementAbility):
    def move(self) -> str:
        return "✈️  Flying through the air"

    def get_name(self) -> str:
        return "Fly"


class ClimbAbility(MovementAbility):
    def move(self) -> str:
        return "🧗 Climbing the wall"

    def get_name(self) -> str:
        return "Climb"


class Robot:
    """
    A robot COMPOSED of different abilities.
    Add or remove abilities without creating new classes!

    Real-life analogy:
        Think of a LEGO robot. You can snap on different parts:
        legs for walking, propellers for flying, fins for swimming.
        You don't need a new robot for each combination — just swap parts!
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._abilities: list[MovementAbility] = []

    def add_ability(self, ability: MovementAbility) -> None:
        self._abilities.append(ability)

    def remove_ability(self, ability_name: str) -> None:
        self._abilities = [a for a in self._abilities if a.get_name() != ability_name]

    def show_abilities(self) -> str:
        if not self._abilities:
            return f"🤖 {self.name} has no abilities"
        names = [a.get_name() for a in self._abilities]
        return f"🤖 {self.name} can: {', '.join(names)}"

    def perform_all(self) -> list[str]:
        return [f"  {a.move()}" for a in self._abilities]


# ---------------------------------------------------------------------------
# Real-World Example: Computer System (Composition)
# ---------------------------------------------------------------------------


class CPU:
    """A processor component."""

    def __init__(self, model: str, cores: int, speed_ghz: float) -> None:
        self.model = model
        self.cores = cores
        self.speed_ghz = speed_ghz

    def process(self) -> str:
        return f"⚡ {self.model} ({self.cores} cores @ {self.speed_ghz}GHz) processing..."

    def __str__(self) -> str:
        return f"CPU: {self.model}"


class RAM:
    """A memory component."""

    def __init__(self, size_gb: int, type: str = "DDR5") -> None:
        self.size_gb = size_gb
        self.type = type

    def __str__(self) -> str:
        return f"RAM: {self.size_gb}GB {self.type}"


class Storage:
    """A storage component."""

    def __init__(self, size_gb: int, type: str = "SSD") -> None:
        self.size_gb = size_gb
        self.type = type

    def __str__(self) -> str:
        return f"Storage: {self.size_gb}GB {self.type}"


class GPU:
    """A graphics card component."""

    def __init__(self, model: str, vram_gb: int) -> None:
        self.model = model
        self.vram_gb = vram_gb

    def render(self) -> str:
        return f"🎮 {self.model} ({self.vram_gb}GB VRAM) rendering..."

    def __str__(self) -> str:
        return f"GPU: {self.model}"


class Computer:
    """
    A computer COMPOSED of parts.

    Real-life analogy:
        A computer "HAS A" CPU, "HAS" RAM, "HAS" storage.
        You can upgrade the RAM without replacing the whole computer.
        That's the beauty of composition!
    """

    def __init__(self, name: str, cpu: CPU, ram: RAM, storage: Storage,
                 gpu: GPU | None = None) -> None:
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def specs(self) -> str:
        parts = [
            f"  💻 {self.name}",
            f"     {self.cpu}",
            f"     {self.ram}",
            f"     {self.storage}",
        ]
        if self.gpu:
            parts.append(f"     {self.gpu}")
        return "\n".join(parts)

    def run_task(self, task: str) -> list[str]:
        results = [
            f"  Running '{task}' on {self.name}:",
            f"    {self.cpu.process()}",
        ]
        if self.gpu and "render" in task.lower():
            results.append(f"    {self.gpu.render()}")
        return results

    def upgrade_ram(self, new_ram: RAM) -> str:
        old = self.ram
        self.ram = new_ram
        return f"  🔧 Upgraded RAM: {old} → {new_ram}"

    def upgrade_storage(self, new_storage: Storage) -> str:
        old = self.storage
        self.storage = new_storage
        return f"  🔧 Upgraded Storage: {old} → {new_storage}"


# ---------------------------------------------------------------------------
# Real-World Example: Notification System (Composition)
# ---------------------------------------------------------------------------


class MessageFormatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        ...


class PlainTextFormatter(MessageFormatter):
    def format(self, message: str) -> str:
        return message


class HTMLFormatter(MessageFormatter):
    def format(self, message: str) -> str:
        return f"<html><body><p>{message}</p></body></html>"


class MarkdownFormatter(MessageFormatter):
    def format(self, message: str) -> str:
        return f"**Notification:** {message}"


class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient: str, content: str) -> str:
        ...


class EmailSender(MessageSender):
    def send(self, recipient: str, content: str) -> str:
        return f"📧 Email to {recipient}: {content[:50]}..."


class SMSSender(MessageSender):
    def send(self, recipient: str, content: str) -> str:
        return f"📱 SMS to {recipient}: {content[:50]}..."


class NotificationService:
    """
    Composed of a formatter AND a sender.
    Mix and match ANY formatter with ANY sender!

    Without composition: EmailHTMLNotification, EmailPlainNotification,
                         SMSHTMLNotification, SMSPlainNotification... 😱

    With composition: NotificationService(any_formatter, any_sender) ✅
    """

    def __init__(self, formatter: MessageFormatter, sender: MessageSender) -> None:
        self._formatter = formatter
        self._sender = sender

    def notify(self, recipient: str, message: str) -> str:
        formatted = self._formatter.format(message)
        return self._sender.send(recipient, formatted)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Composition vs Inheritance demonstration."""
    print("=" * 60)
    print("  COMPOSITION — Building with Parts")
    print("=" * 60)

    # --- Robot with Abilities ---
    print("\n🤖 1. Robot with Composable Abilities")
    print("-" * 40)

    robot1 = Robot("Explorer Bot")
    robot1.add_ability(WalkAbility())
    robot1.add_ability(SwimAbility())
    robot1.add_ability(ClimbAbility())

    print(f"  {robot1.show_abilities()}")
    for action in robot1.perform_all():
        print(f"  {action}")

    # Swap abilities at runtime!
    print("\n  Upgrading: Remove Swim, Add Fly!")
    robot1.remove_ability("Swim")
    robot1.add_ability(FlyAbility())
    print(f"  {robot1.show_abilities()}")

    robot2 = Robot("Aqua Bot")
    robot2.add_ability(SwimAbility())
    print(f"\n  {robot2.show_abilities()}")

    # --- Computer System ---
    print("\n\n💻 2. Computer System (Composed of Parts)")
    print("-" * 40)

    gaming_pc = Computer(
        "Gaming PC",
        cpu=CPU("Intel i9-14900K", 24, 6.0),
        ram=RAM(32, "DDR5"),
        storage=Storage(2000, "NVMe SSD"),
        gpu=GPU("NVIDIA RTX 4090", 24),
    )

    office_pc = Computer(
        "Office PC",
        cpu=CPU("Intel i5-14400", 10, 4.7),
        ram=RAM(16, "DDR5"),
        storage=Storage(512, "SSD"),
    )

    print(gaming_pc.specs())
    print()
    print(office_pc.specs())

    # Upgrade parts without replacing the whole computer!
    print(f"\n{office_pc.upgrade_ram(RAM(32, 'DDR5'))}")
    print(f"{office_pc.upgrade_storage(Storage(1000, 'NVMe SSD'))}")
    print(f"\n  Updated specs:")
    print(office_pc.specs())

    # --- Notification System ---
    print("\n\n🔔 3. Notification System (Formatter × Sender)")
    print("-" * 40)

    combos = [
        ("Email + HTML", NotificationService(HTMLFormatter(), EmailSender())),
        ("Email + Plain", NotificationService(PlainTextFormatter(), EmailSender())),
        ("SMS + Plain", NotificationService(PlainTextFormatter(), SMSSender())),
        ("SMS + Markdown", NotificationService(MarkdownFormatter(), SMSSender())),
    ]

    for label, service in combos:
        result = service.notify("alice@example.com", "Your order has shipped!")
        print(f"  {label}: {result}")

    # --- Key Takeaway ---
    print("\n\n💡 KEY TAKEAWAY")
    print("-" * 40)
    print("  Inheritance: 'IS A' relationship")
    print("    → Dog IS AN Animal")
    print("    → Tesla IS A Car")
    print()
    print("  Composition: 'HAS A' relationship")
    print("    → Car HAS AN Engine")
    print("    → Computer HAS A CPU")
    print("    → Robot HAS Abilities")
    print()
    print("  👉 RULE OF THUMB: Favor composition over inheritance!")
    print("     Use inheritance for true 'is-a' relationships.")
    print("     Use composition for 'has-a' or 'can-do' relationships.")


if __name__ == "__main__":
    demo()
