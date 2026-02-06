"""
Creational Design Patterns
===========================
Patterns that deal with object creation mechanisms.

Included:
    - Singleton: One instance only
    - Factory Method: Create objects without specifying exact class
    - Abstract Factory: Create families of related objects
    - Builder: Construct complex objects step by step
    - Prototype: Clone existing objects
"""

from .singleton import AppConfig, Logger, SingletonMeta
from .factory import PaymentFactory, NotificationFactory
from .abstract_factory import WebUIFactory, MobileUIFactory, DesktopUIFactory
from .builder import HttpRequestBuilder, UserProfileBuilder, PizzaBuilder
from .prototype import Document, DocumentTemplateRegistry, GameCharacter

__all__ = [
    "AppConfig", "Logger", "SingletonMeta",
    "PaymentFactory", "NotificationFactory",
    "WebUIFactory", "MobileUIFactory", "DesktopUIFactory",
    "HttpRequestBuilder", "UserProfileBuilder", "PizzaBuilder",
    "Document", "DocumentTemplateRegistry", "GameCharacter",
]
