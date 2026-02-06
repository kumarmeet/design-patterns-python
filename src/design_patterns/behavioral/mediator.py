"""
Mediator Pattern
=================
Defines an object that encapsulates how a set of objects interact.
Promotes loose coupling by keeping objects from referring to each other directly.

Real-World Example: Air Traffic Control Tower
Think of an airport control tower. Airplanes don't talk to each other directly.
Instead, they all communicate through the control tower (mediator),
which coordinates takeoffs, landings, and movements safely.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


# ---------------------------------------------------------------------------
# Real-World Example 1: Chat Room
# ---------------------------------------------------------------------------


class ChatMediator(ABC):
    """
    Mediator interface for a chat system.

    Real-life analogy:
        Think of a WhatsApp group. You don't send messages directly
        to each person — you send it to the GROUP, and the group
        delivers it to everyone. The group chat is the mediator!
    """

    @abstractmethod
    def send_message(self, message: str, sender: ChatUser) -> None:
        ...

    @abstractmethod
    def add_user(self, user: ChatUser) -> None:
        ...


class ChatUser:
    """A user in the chat room."""

    def __init__(self, name: str, mediator: ChatMediator | None = None) -> None:
        self.name = name
        self._mediator = mediator
        self.received_messages: list[str] = []

    def set_mediator(self, mediator: ChatMediator) -> None:
        self._mediator = mediator

    def send(self, message: str) -> None:
        """Send a message through the mediator (chat room)."""
        if self._mediator:
            print(f"    📤 {self.name} sends: \"{message}\"")
            self._mediator.send_message(message, self)

    def receive(self, message: str, sender_name: str) -> None:
        """Receive a message from the chat room."""
        formatted = f"[{sender_name}]: {message}"
        self.received_messages.append(formatted)
        print(f"    📥 {self.name} received: {formatted}")


class ChatRoom(ChatMediator):
    """
    Concrete mediator — a chat room that routes messages.
    Users don't know about each other — only the chat room does!
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._users: list[ChatUser] = []

    def add_user(self, user: ChatUser) -> None:
        user.set_mediator(self)
        self._users.append(user)
        print(f"  👋 {user.name} joined '{self.name}'")

    def send_message(self, message: str, sender: ChatUser) -> None:
        """Broadcast message to all users EXCEPT the sender."""
        for user in self._users:
            if user != sender:
                user.receive(message, sender.name)


# ---------------------------------------------------------------------------
# Real-World Example 2: Smart Home Controller
# ---------------------------------------------------------------------------


class SmartHomeMediator(ABC):
    """Mediator for smart home devices."""

    @abstractmethod
    def notify(self, sender: SmartHomeDevice, event: str) -> None:
        ...


class SmartHomeDevice(ABC):
    """Base class for smart home devices."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._mediator: SmartHomeMediator | None = None

    def set_mediator(self, mediator: SmartHomeMediator) -> None:
        self._mediator = mediator

    def notify_mediator(self, event: str) -> None:
        if self._mediator:
            self._mediator.notify(self, event)


class SmartLight(SmartHomeDevice):
    def __init__(self, name: str = "Smart Light") -> None:
        super().__init__(name)
        self.is_on = False
        self.brightness = 100

    def turn_on(self, brightness: int = 100) -> None:
        self.is_on = True
        self.brightness = brightness
        print(f"    💡 {self.name}: ON (brightness: {brightness}%)")

    def turn_off(self) -> None:
        self.is_on = False
        print(f"    💡 {self.name}: OFF")


class SmartThermostat(SmartHomeDevice):
    def __init__(self, name: str = "Thermostat") -> None:
        super().__init__(name)
        self.temperature = 22.0
        self.mode = "auto"

    def set_temperature(self, temp: float) -> None:
        self.temperature = temp
        print(f"    🌡️  {self.name}: Set to {temp}°C")

    def set_mode(self, mode: str) -> None:
        self.mode = mode
        print(f"    🌡️  {self.name}: Mode = {mode}")


class SmartDoorLock(SmartHomeDevice):
    def __init__(self, name: str = "Door Lock") -> None:
        super().__init__(name)
        self.is_locked = True

    def lock(self) -> None:
        self.is_locked = True
        print(f"    🔒 {self.name}: LOCKED")
        self.notify_mediator("door_locked")

    def unlock(self) -> None:
        self.is_locked = False
        print(f"    🔓 {self.name}: UNLOCKED")
        self.notify_mediator("door_unlocked")


class SecurityCamera(SmartHomeDevice):
    def __init__(self, name: str = "Security Camera") -> None:
        super().__init__(name)
        self.is_recording = False

    def start_recording(self) -> None:
        self.is_recording = True
        print(f"    📹 {self.name}: Recording STARTED")

    def stop_recording(self) -> None:
        self.is_recording = False
        print(f"    📹 {self.name}: Recording STOPPED")


class MotionSensor(SmartHomeDevice):
    def __init__(self, name: str = "Motion Sensor") -> None:
        super().__init__(name)

    def detect_motion(self) -> None:
        print(f"    🏃 {self.name}: Motion detected!")
        self.notify_mediator("motion_detected")

    def detect_no_motion(self) -> None:
        print(f"    😴 {self.name}: No motion for 30 minutes")
        self.notify_mediator("no_motion")


class SmartHomeController(SmartHomeMediator):
    """
    The brain of the smart home — coordinates all devices.

    When one device triggers an event, the controller decides
    what OTHER devices should do in response.
    Devices DON'T communicate directly with each other!
    """

    def __init__(self) -> None:
        self.light = SmartLight("Living Room Light")
        self.thermostat = SmartThermostat("Main Thermostat")
        self.door_lock = SmartDoorLock("Front Door")
        self.camera = SecurityCamera("Front Camera")
        self.motion_sensor = MotionSensor("Hallway Sensor")

        # Set mediator for all devices
        for device in [self.light, self.thermostat, self.door_lock,
                       self.camera, self.motion_sensor]:
            device.set_mediator(self)

    def notify(self, sender: SmartHomeDevice, event: str) -> None:
        """React to events from devices."""
        if event == "motion_detected":
            print("    🏠 Controller: Motion detected! Activating home...")
            self.light.turn_on(brightness=80)
            self.camera.start_recording()

        elif event == "no_motion":
            print("    🏠 Controller: No activity. Entering sleep mode...")
            self.light.turn_off()
            self.thermostat.set_temperature(18.0)
            self.camera.stop_recording()

        elif event == "door_unlocked":
            print("    🏠 Controller: Welcome home!")
            self.light.turn_on()
            self.thermostat.set_temperature(22.0)
            self.camera.start_recording()

        elif event == "door_locked":
            print("    🏠 Controller: Goodbye! Securing home...")
            self.light.turn_off()
            self.thermostat.set_mode("eco")
            self.camera.start_recording()


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Mediator pattern demonstration."""
    print("=" * 60)
    print("  MEDIATOR PATTERN DEMO")
    print("=" * 60)

    # --- Chat Room Example ---
    print("\n💬 Example 1: Chat Room")
    print("-" * 50)

    room = ChatRoom("Python Developers")

    alice = ChatUser("Alice")
    bob = ChatUser("Bob")
    charlie = ChatUser("Charlie")

    room.add_user(alice)
    room.add_user(bob)
    room.add_user(charlie)

    print()
    alice.send("Hey everyone! Anyone up for code review?")
    print()
    bob.send("Sure! Send me the PR link.")
    print()
    charlie.send("I'll join too!")

    # --- Smart Home Example ---
    print("\n\n🏠 Example 2: Smart Home Controller")
    print("-" * 50)

    home = SmartHomeController()

    print("\n  Scenario 1: Someone comes home")
    home.door_lock.unlock()

    print("\n  Scenario 2: Motion detected in hallway")
    home.motion_sensor.detect_motion()

    print("\n  Scenario 3: No motion for a while")
    home.motion_sensor.detect_no_motion()

    print("\n  Scenario 4: Leaving home")
    home.door_lock.lock()


if __name__ == "__main__":
    demo()
