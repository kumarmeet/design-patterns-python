"""
Behavioral Design Patterns
============================
Patterns that deal with object communication and responsibility.

Included:
    - Strategy: Interchangeable algorithms
    - Observer: Event-driven notifications
    - Chain of Responsibility: Request processing pipeline
    - Command: Encapsulate actions as objects
    - State: Object behavior based on state
    - Template Method: Algorithm skeleton with customizable steps
    - Iterator: Sequential access to collections
    - Mediator: Centralized communication
"""

from .strategy import ShoppingCart, PercentageDiscount, FlatDiscount
from .observer import Order, CustomerNotifier, DashboardUpdater
from .chain_of_responsibility import TeamLead, DepartmentManager, Director, CEO
from .command import TextEditor, InsertTextCommand, DeleteTextCommand
from .state import OnlineOrder, AudioPlayer
from .template_method import CSVDataProcessor, JSONDataProcessor
from .iterator import Playlist, Song
from .mediator import ChatRoom, ChatUser, SmartHomeController

__all__ = [
    "ShoppingCart", "PercentageDiscount", "FlatDiscount",
    "Order", "CustomerNotifier", "DashboardUpdater",
    "TeamLead", "DepartmentManager", "Director", "CEO",
    "TextEditor", "InsertTextCommand", "DeleteTextCommand",
    "OnlineOrder", "AudioPlayer",
    "CSVDataProcessor", "JSONDataProcessor",
    "Playlist", "Song",
    "ChatRoom", "ChatUser", "SmartHomeController",
]
