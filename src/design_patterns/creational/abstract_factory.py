"""
Abstract Factory Pattern
=========================
Creates families of related objects without specifying their concrete classes.

Real-World Example: Cross-Platform UI Components
Think of it like IKEA furniture sets — you pick a "style" (Modern, Classic),
and the factory gives you a matching chair, table, and sofa in that style.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Abstract Products: UI Components
# ---------------------------------------------------------------------------


class Button(ABC):
    """Abstract button that all platforms must implement."""

    @abstractmethod
    def render(self) -> str:
        ...

    @abstractmethod
    def on_click(self, action: str) -> str:
        ...


class TextInput(ABC):
    """Abstract text input that all platforms must implement."""

    @abstractmethod
    def render(self) -> str:
        ...

    @abstractmethod
    def set_placeholder(self, text: str) -> str:
        ...


class Checkbox(ABC):
    """Abstract checkbox that all platforms must implement."""

    @abstractmethod
    def render(self) -> str:
        ...

    @abstractmethod
    def toggle(self) -> str:
        ...


# ---------------------------------------------------------------------------
# Concrete Products: Web Platform
# ---------------------------------------------------------------------------


class WebButton(Button):
    def render(self) -> str:
        return "🌐 <button class='btn btn-primary'>Click Me</button>"

    def on_click(self, action: str) -> str:
        return f"🌐 Web button triggered: {action}"


class WebTextInput(TextInput):
    def render(self) -> str:
        return "🌐 <input type='text' class='form-control' />"

    def set_placeholder(self, text: str) -> str:
        return f"🌐 <input placeholder='{text}' />"


class WebCheckbox(Checkbox):
    def render(self) -> str:
        return "🌐 <input type='checkbox' class='form-check' />"

    def toggle(self) -> str:
        return "🌐 Web checkbox toggled"


# ---------------------------------------------------------------------------
# Concrete Products: Mobile Platform
# ---------------------------------------------------------------------------


class MobileButton(Button):
    def render(self) -> str:
        return "📱 UIButton(title: 'Click Me', style: .filled)"

    def on_click(self, action: str) -> str:
        return f"📱 Mobile button triggered: {action}"


class MobileTextInput(TextInput):
    def render(self) -> str:
        return "📱 UITextField(borderStyle: .roundedRect)"

    def set_placeholder(self, text: str) -> str:
        return f"📱 UITextField(placeholder: '{text}')"


class MobileCheckbox(Checkbox):
    def render(self) -> str:
        return "📱 UISwitch(isOn: false)"

    def toggle(self) -> str:
        return "📱 Mobile switch toggled"


# ---------------------------------------------------------------------------
# Concrete Products: Desktop Platform
# ---------------------------------------------------------------------------


class DesktopButton(Button):
    def render(self) -> str:
        return "🖥️  QPushButton('Click Me')"

    def on_click(self, action: str) -> str:
        return f"🖥️  Desktop button triggered: {action}"


class DesktopTextInput(TextInput):
    def render(self) -> str:
        return "🖥️  QLineEdit()"

    def set_placeholder(self, text: str) -> str:
        return f"🖥️  QLineEdit(placeholderText='{text}')"


class DesktopCheckbox(Checkbox):
    def render(self) -> str:
        return "🖥️  QCheckBox('Option')"

    def toggle(self) -> str:
        return "🖥️  Desktop checkbox toggled"


# ---------------------------------------------------------------------------
# Abstract Factory
# ---------------------------------------------------------------------------


class UIFactory(ABC):
    """
    Abstract factory that creates a family of UI components.

    Real-life analogy:
        Think of a furniture store with different style sections.
        If you go to the "Modern" section, EVERYTHING is modern —
        modern chair, modern table, modern lamp. They all match!
        That's what an Abstract Factory does for your code.
    """

    @abstractmethod
    def create_button(self) -> Button:
        ...

    @abstractmethod
    def create_text_input(self) -> TextInput:
        ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        ...


# ---------------------------------------------------------------------------
# Concrete Factories
# ---------------------------------------------------------------------------


class WebUIFactory(UIFactory):
    """Factory for web UI components."""

    def create_button(self) -> Button:
        return WebButton()

    def create_text_input(self) -> TextInput:
        return WebTextInput()

    def create_checkbox(self) -> Checkbox:
        return WebCheckbox()


class MobileUIFactory(UIFactory):
    """Factory for mobile UI components."""

    def create_button(self) -> Button:
        return MobileButton()

    def create_text_input(self) -> TextInput:
        return MobileTextInput()

    def create_checkbox(self) -> Checkbox:
        return MobileCheckbox()


class DesktopUIFactory(UIFactory):
    """Factory for desktop UI components."""

    def create_button(self) -> Button:
        return DesktopButton()

    def create_text_input(self) -> TextInput:
        return DesktopTextInput()

    def create_checkbox(self) -> Checkbox:
        return DesktopCheckbox()


# ---------------------------------------------------------------------------
# Client code that works with ANY factory
# ---------------------------------------------------------------------------


def build_login_form(factory: UIFactory) -> list[str]:
    """Build a login form using whatever platform factory is provided."""
    components = []
    components.append(factory.create_text_input().set_placeholder("Enter username"))
    components.append(factory.create_text_input().set_placeholder("Enter password"))
    components.append(factory.create_checkbox().render() + " — Remember me")
    components.append(factory.create_button().on_click("submit_login"))
    return components


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Abstract Factory pattern demonstration."""
    print("=" * 60)
    print("  ABSTRACT FACTORY PATTERN DEMO")
    print("=" * 60)

    factories: dict[str, UIFactory] = {
        "Web": WebUIFactory(),
        "Mobile": MobileUIFactory(),
        "Desktop": DesktopUIFactory(),
    }

    for platform, factory in factories.items():
        print(f"\n🏗️  Building Login Form for {platform}")
        print("-" * 40)
        form = build_login_form(factory)
        for component in form:
            print(f"  {component}")


if __name__ == "__main__":
    demo()
