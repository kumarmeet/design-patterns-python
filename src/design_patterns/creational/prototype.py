"""
Prototype Pattern
==================
Creates new objects by copying (cloning) existing ones instead of creating from scratch.

Real-World Example: Document Templates
Think of it like photocopying — you have an original document,
and you make copies, then customize each copy slightly.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Real-World Example 1: Document Template System
# ---------------------------------------------------------------------------


@dataclass
class Document:
    """
    A document that can be cloned from a template.

    Real-life analogy:
        Think of a school test paper. The teacher creates ONE master copy,
        then photocopies it for every student. Each student writes different
        answers on their copy — but they all started from the same template.
    """
    title: str = ""
    content: str = ""
    author: str = ""
    formatting: dict[str, Any] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

    def clone(self) -> Document:
        """Create a deep copy of this document."""
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return (
            f"  📄 '{self.title}' by {self.author}\n"
            f"  Content: {self.content[:50]}{'...' if len(self.content) > 50 else ''}\n"
            f"  Tags: {', '.join(self.tags)}\n"
            f"  Format: {self.formatting}"
        )


class DocumentTemplateRegistry:
    """
    Stores reusable document templates.

    Real-life analogy:
        Think of a stationery shop that has ready-made templates
        for resumes, invoices, and letters. You pick one, copy it,
        and fill in your details.
    """

    def __init__(self) -> None:
        self._templates: dict[str, Document] = {}

    def register(self, name: str, template: Document) -> None:
        """Register a document template."""
        self._templates[name] = template

    def create_from_template(self, name: str) -> Document:
        """Create a new document by cloning a registered template."""
        template = self._templates.get(name)
        if template is None:
            raise ValueError(f"Template '{name}' not found")
        return template.clone()

    def list_templates(self) -> list[str]:
        """List all available template names."""
        return list(self._templates.keys())


# ---------------------------------------------------------------------------
# Real-World Example 2: Game Character Cloning
# ---------------------------------------------------------------------------


@dataclass
class GameCharacter:
    """
    A game character that can be cloned to create similar characters quickly.

    Real-life analogy:
        In a video game, you have an "enemy template." Instead of building
        each enemy from scratch, you clone the template and tweak small things
        like position, health, or color.
    """
    name: str = "Unknown"
    health: int = 100
    attack: int = 10
    defense: int = 5
    abilities: list[str] = field(default_factory=list)
    equipment: dict[str, str] = field(default_factory=dict)
    position: tuple[int, int] = (0, 0)

    def clone(self) -> GameCharacter:
        """Create a deep copy of this character."""
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return (
            f"  🎮 {self.name} | HP: {self.health} | ATK: {self.attack} | DEF: {self.defense}\n"
            f"  Abilities: {', '.join(self.abilities)}\n"
            f"  Equipment: {self.equipment}\n"
            f"  Position: {self.position}"
        )


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Prototype pattern demonstration."""
    print("=" * 60)
    print("  PROTOTYPE PATTERN DEMO")
    print("=" * 60)

    # --- Document Template Example ---
    print("\n📄 Example 1: Document Templates")
    print("-" * 40)

    registry = DocumentTemplateRegistry()

    # Create templates
    invoice_template = Document(
        title="Invoice",
        content="Invoice for services rendered...",
        author="Company XYZ",
        formatting={"font": "Arial", "size": 12, "margin": "1in"},
        tags=["finance", "invoice"],
        metadata={"version": "1.0"},
    )
    registry.register("invoice", invoice_template)

    report_template = Document(
        title="Monthly Report",
        content="Summary of activities for the month...",
        author="Company XYZ",
        formatting={"font": "Times New Roman", "size": 14, "margin": "1.5in"},
        tags=["report", "monthly"],
        metadata={"version": "2.0"},
    )
    registry.register("report", report_template)

    # Create documents from templates
    my_invoice = registry.create_from_template("invoice")
    my_invoice.title = "Invoice #1042 — Web Development"
    my_invoice.content = "Payment for building the company website..."
    my_invoice.metadata["invoice_number"] = "1042"

    print("Original Template:")
    print(invoice_template)
    print("\nCloned & Customized:")
    print(my_invoice)

    # Prove they're independent
    print(f"\n  Are they the same object? {my_invoice is invoice_template}")  # False

    # --- Game Character Example ---
    print("\n🎮 Example 2: Game Character Cloning")
    print("-" * 40)

    # Create a base enemy template
    goblin_template = GameCharacter(
        name="Goblin",
        health=50,
        attack=8,
        defense=3,
        abilities=["slash", "dodge"],
        equipment={"weapon": "rusty sword", "armor": "leather"},
    )

    # Clone and customize variants
    goblin_warrior = goblin_template.clone()
    goblin_warrior.name = "Goblin Warrior"
    goblin_warrior.health = 80
    goblin_warrior.attack = 15
    goblin_warrior.equipment["weapon"] = "iron sword"
    goblin_warrior.position = (10, 20)

    goblin_archer = goblin_template.clone()
    goblin_archer.name = "Goblin Archer"
    goblin_archer.attack = 12
    goblin_archer.abilities.append("arrow_shot")
    goblin_archer.equipment["weapon"] = "short bow"
    goblin_archer.position = (30, 15)

    print("Base Template:")
    print(goblin_template)
    print("\nWarrior (cloned + customized):")
    print(goblin_warrior)
    print("\nArcher (cloned + customized):")
    print(goblin_archer)


if __name__ == "__main__":
    demo()
