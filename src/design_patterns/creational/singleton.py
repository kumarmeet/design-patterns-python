"""
Singleton Pattern
=================
Ensures a class has only one instance and provides a global access point to it.

Real-World Example: Application Configuration Manager
Think of it like the settings app on your phone — there's only ONE settings,
no matter how many times you open it.
"""

from __future__ import annotations

import threading
from typing import Any


class SingletonMeta(type):
    """
    Thread-safe Singleton metaclass.

    This metaclass ensures that only one instance of any class using it
    can ever exist — even when multiple threads try to create it at the same time.
    """

    _instances: dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        # Double-checked locking for thread safety
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


# ---------------------------------------------------------------------------
# Real-World Example: Application Configuration Manager
# ---------------------------------------------------------------------------


class AppConfig(metaclass=SingletonMeta):
    """
    Application Configuration Manager.

    Imagine your app has settings like database URL, API keys, and feature flags.
    You want ONE place to manage all of them — not multiple copies floating around.

    Real-life analogy:
        Think of it like the principal's office in a school.
        There's only ONE principal's office. Every teacher who needs
        to check a school rule goes to the SAME office.
    """

    def __init__(self) -> None:
        self._settings: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """Store a configuration value."""
        self._settings[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value."""
        return self._settings.get(key, default)

    def get_all(self) -> dict[str, Any]:
        """Get all configuration settings."""
        return self._settings.copy()

    def __repr__(self) -> str:
        return f"AppConfig(settings={self._settings})"


# ---------------------------------------------------------------------------
# Real-World Example: Logger Service
# ---------------------------------------------------------------------------


class Logger(metaclass=SingletonMeta):
    """
    Logger Service — only one logger should exist so all logs go to the same place.

    Real-life analogy:
        Think of a school diary. The entire school writes announcements
        in ONE diary — not separate diaries for each class.
    """

    def __init__(self) -> None:
        self._logs: list[str] = []

    def log(self, level: str, message: str) -> str:
        """Log a message with a level (INFO, WARNING, ERROR)."""
        entry = f"[{level.upper()}] {message}"
        self._logs.append(entry)
        return entry

    def info(self, message: str) -> str:
        return self.log("INFO", message)

    def warning(self, message: str) -> str:
        return self.log("WARNING", message)

    def error(self, message: str) -> str:
        return self.log("ERROR", message)

    def get_logs(self) -> list[str]:
        """Get all recorded logs."""
        return self._logs.copy()

    def __repr__(self) -> str:
        return f"Logger(entries={len(self._logs)})"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Singleton pattern demonstration."""
    print("=" * 60)
    print("  SINGLETON PATTERN DEMO")
    print("=" * 60)

    # --- Config Manager Example ---
    print("\n📋 Example 1: Application Config Manager")
    print("-" * 40)

    config1 = AppConfig()
    config1.set("database_url", "postgresql://localhost:5432/mydb")
    config1.set("debug_mode", True)

    # Creating another "instance" — it's actually the same one!
    config2 = AppConfig()

    print(f"config1 is config2? {config1 is config2}")  # True!
    print(f"Database URL from config2: {config2.get('database_url')}")
    print(f"All settings: {config2.get_all()}")

    # --- Logger Example ---
    print("\n📝 Example 2: Logger Service")
    print("-" * 40)

    logger1 = Logger()
    logger1.info("Application started")
    logger1.warning("Disk space running low")

    # Another reference — same logger!
    logger2 = Logger()
    logger2.error("Failed to connect to database")

    print(f"logger1 is logger2? {logger1 is logger2}")  # True!
    print("All logs from logger2:")
    for log_entry in logger2.get_logs():
        print(f"  {log_entry}")


if __name__ == "__main__":
    demo()
