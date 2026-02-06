"""
Architectural Design Patterns
===============================
Patterns that deal with system-level organization.

Included:
    - MVC: Model-View-Controller separation
    - Dependency Injection: Loose coupling via injected dependencies
    - Repository: Abstract data access layer
"""

from .mvc import TaskModel, TaskView, TaskController
from .dependency_injection import NotificationService, EmailSender, ServiceContainer
from .repository import InMemoryUserRepository, InMemoryProductRepository, UserService

__all__ = [
    "TaskModel", "TaskView", "TaskController",
    "NotificationService", "EmailSender", "ServiceContainer",
    "InMemoryUserRepository", "InMemoryProductRepository", "UserService",
]
