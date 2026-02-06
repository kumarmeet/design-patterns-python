"""
Structural Design Patterns
============================
Patterns that deal with object composition and relationships.

Included:
    - Adapter: Make incompatible interfaces work together
    - Decorator: Add behavior dynamically
    - Facade: Simplify complex subsystems
    - Proxy: Control access to objects
    - Composite: Tree structures with uniform interface
    - Bridge: Separate abstraction from implementation
"""

from .adapter import StripeAdapter, PayPalAdapter, RazorpayAdapter
from .decorator import BasicCoffee, MilkDecorator, SugarDecorator
from .facade import OnlineStoreFacade
from .proxy import InternetProxy, CachingWeatherProxy, LazyImageProxy
from .composite import File, Folder, Manager, IndividualContributor
from .bridge import EmailChannel, SMSChannel, AlertNotification

__all__ = [
    "StripeAdapter", "PayPalAdapter", "RazorpayAdapter",
    "BasicCoffee", "MilkDecorator", "SugarDecorator",
    "OnlineStoreFacade",
    "InternetProxy", "CachingWeatherProxy", "LazyImageProxy",
    "File", "Folder", "Manager", "IndividualContributor",
    "EmailChannel", "SMSChannel", "AlertNotification",
]
