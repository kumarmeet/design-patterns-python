"""
Design Patterns & OOP Concepts Demo Runner
============================================
Run any or all design pattern / OOP concept demos from the command line.

Usage:
    python -m examples.runner                    # List all topics
    python -m examples.runner singleton          # Run one pattern
    python -m examples.runner all                # Run all patterns
    python -m examples.runner creational         # Run all creational patterns
    python -m examples.runner oops               # Run all OOP concepts
    python -m examples.runner classes_and_objects # Run one OOP concept
"""

from __future__ import annotations

import sys

# --- OOP Concept Imports ---
from src.oops_concepts.classes_and_objects import demo as classes_demo
from src.oops_concepts.encapsulation import demo as encapsulation_demo
from src.oops_concepts.inheritance import demo as inheritance_demo
from src.oops_concepts.polymorphism import demo as polymorphism_demo
from src.oops_concepts.abstraction import demo as abstraction_demo
from src.oops_concepts.composition import demo as composition_demo
from src.oops_concepts.solid_principles import demo as solid_demo

# --- Design Pattern Imports ---
from src.design_patterns.creational.singleton import demo as singleton_demo
from src.design_patterns.creational.factory import demo as factory_demo
from src.design_patterns.creational.builder import demo as builder_demo
from src.design_patterns.creational.prototype import demo as prototype_demo
from src.design_patterns.creational.abstract_factory import demo as abstract_factory_demo

from src.design_patterns.structural.adapter import demo as adapter_demo
from src.design_patterns.structural.decorator import demo as decorator_demo
from src.design_patterns.structural.facade import demo as facade_demo
from src.design_patterns.structural.proxy import demo as proxy_demo
from src.design_patterns.structural.composite import demo as composite_demo
from src.design_patterns.structural.bridge import demo as bridge_demo

from src.design_patterns.behavioral.strategy import demo as strategy_demo
from src.design_patterns.behavioral.observer import demo as observer_demo
from src.design_patterns.behavioral.chain_of_responsibility import demo as chain_demo
from src.design_patterns.behavioral.command import demo as command_demo
from src.design_patterns.behavioral.state import demo as state_demo
from src.design_patterns.behavioral.template_method import demo as template_method_demo
from src.design_patterns.behavioral.iterator import demo as iterator_demo
from src.design_patterns.behavioral.mediator import demo as mediator_demo

from src.design_patterns.architectural.mvc import demo as mvc_demo
from src.design_patterns.architectural.dependency_injection import demo as di_demo
from src.design_patterns.architectural.repository import demo as repository_demo

# ---------------------------------------------------------------------------
# OOP Concepts (learn these BEFORE design patterns!)
# ---------------------------------------------------------------------------
OOP_CONCEPTS: dict[str, dict] = {
    "classes_and_objects": {"demo": classes_demo, "category": "oops", "name": "Classes & Objects"},
    "encapsulation": {"demo": encapsulation_demo, "category": "oops", "name": "Encapsulation"},
    "inheritance": {"demo": inheritance_demo, "category": "oops", "name": "Inheritance"},
    "polymorphism": {"demo": polymorphism_demo, "category": "oops", "name": "Polymorphism"},
    "abstraction": {"demo": abstraction_demo, "category": "oops", "name": "Abstraction"},
    "composition": {"demo": composition_demo, "category": "oops", "name": "Composition vs Inheritance"},
    "solid_principles": {"demo": solid_demo, "category": "oops", "name": "SOLID Principles"},
}

# ---------------------------------------------------------------------------
# Design Patterns
# ---------------------------------------------------------------------------
PATTERNS: dict[str, dict] = {
    # Creational
    "singleton": {"demo": singleton_demo, "category": "creational", "name": "Singleton"},
    "factory": {"demo": factory_demo, "category": "creational", "name": "Factory Method"},
    "abstract_factory": {"demo": abstract_factory_demo, "category": "creational", "name": "Abstract Factory"},
    "builder": {"demo": builder_demo, "category": "creational", "name": "Builder"},
    "prototype": {"demo": prototype_demo, "category": "creational", "name": "Prototype"},
    # Structural
    "adapter": {"demo": adapter_demo, "category": "structural", "name": "Adapter"},
    "decorator": {"demo": decorator_demo, "category": "structural", "name": "Decorator"},
    "facade": {"demo": facade_demo, "category": "structural", "name": "Facade"},
    "proxy": {"demo": proxy_demo, "category": "structural", "name": "Proxy"},
    "composite": {"demo": composite_demo, "category": "structural", "name": "Composite"},
    "bridge": {"demo": bridge_demo, "category": "structural", "name": "Bridge"},
    # Behavioral
    "strategy": {"demo": strategy_demo, "category": "behavioral", "name": "Strategy"},
    "observer": {"demo": observer_demo, "category": "behavioral", "name": "Observer"},
    "chain_of_responsibility": {"demo": chain_demo, "category": "behavioral", "name": "Chain of Responsibility"},
    "command": {"demo": command_demo, "category": "behavioral", "name": "Command"},
    "state": {"demo": state_demo, "category": "behavioral", "name": "State"},
    "template_method": {"demo": template_method_demo, "category": "behavioral", "name": "Template Method"},
    "iterator": {"demo": iterator_demo, "category": "behavioral", "name": "Iterator"},
    "mediator": {"demo": mediator_demo, "category": "behavioral", "name": "Mediator"},
    # Architectural
    "mvc": {"demo": mvc_demo, "category": "architectural", "name": "MVC"},
    "dependency_injection": {"demo": di_demo, "category": "architectural", "name": "Dependency Injection"},
    "repository": {"demo": repository_demo, "category": "architectural", "name": "Repository"},
}

# Merged lookup for running individual demos by name
ALL_DEMOS: dict[str, dict] = {**OOP_CONCEPTS, **PATTERNS}

PATTERN_CATEGORIES = ["creational", "structural", "behavioral", "architectural"]
ALL_CATEGORIES = ["oops"] + PATTERN_CATEGORIES


def list_patterns() -> None:
    """Print all available OOP concepts and patterns grouped by category."""
    print("\n" + "=" * 60)
    print("  🎨 DESIGN PATTERNS & OOP CONCEPTS IN PYTHON")
    print("  A Comprehensive Learning Collection")
    print("=" * 60)

    # OOP Concepts first
    print(f"\n  📚 OOP CONCEPTS (Start Here!)")
    print(f"  {'─' * 50}")
    for key, info in OOP_CONCEPTS.items():
        print(f"    • {info['name']:<35} → python -m examples.runner {key}")

    # Design Patterns by category
    for category in PATTERN_CATEGORIES:
        patterns = {k: v for k, v in PATTERNS.items() if v["category"] == category}
        print(f"\n  📂 {category.upper()} PATTERNS")
        print(f"  {'─' * 50}")
        for key, info in patterns.items():
            print(f"    • {info['name']:<35} → python -m examples.runner {key}")

    print(f"\n  💡 Run all OOP concepts:  python -m examples.runner oops")
    print(f"  💡 Run by category:      python -m examples.runner creational")
    print(f"  💡 Run ALL demos:        python -m examples.runner all")
    print()


def run_demo(name: str) -> None:
    """Run a specific OOP concept or pattern demo."""
    demo_info = ALL_DEMOS.get(name.lower())
    if demo_info:
        demo_info["demo"]()
        print()
    else:
        print(f"  ❌ Unknown topic: '{name}'")
        print(f"  Available: {', '.join(ALL_DEMOS.keys())}")


def run_category(category: str) -> None:
    """Run all demos in a category."""
    if category == "oops":
        for key in OOP_CONCEPTS:
            run_demo(key)
    else:
        patterns = {k: v for k, v in PATTERNS.items() if v["category"] == category}
        if not patterns:
            print(f"  ❌ Unknown category: '{category}'")
            return
        for key in patterns:
            run_demo(key)


def run_all() -> None:
    """Run all demos (OOP concepts first, then patterns)."""
    for key in OOP_CONCEPTS:
        run_demo(key)
    for key in PATTERNS:
        run_demo(key)


def main() -> None:
    """Main entry point."""
    args = sys.argv[1:]

    if not args:
        list_patterns()
    elif args[0].lower() == "all":
        run_all()
    elif args[0].lower() in ALL_CATEGORIES:
        run_category(args[0].lower())
    else:
        for arg in args:
            run_demo(arg)


if __name__ == "__main__":
    main()
