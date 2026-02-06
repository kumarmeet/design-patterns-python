"""
State Pattern
==============
Allows an object to change its behavior when its internal state changes.
The object appears to change its class.

Real-World Example: Vending Machine
Think of a vending machine. Its behavior changes based on its state:
- No coin inserted → only accepts coins
- Coin inserted → can select a product
- Dispensing → gives you the product
- Out of stock → shows "sold out"
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Real-World Example 1: Order Processing System
# ---------------------------------------------------------------------------


class OrderState(ABC):
    """
    Base state class — each state defines what actions are possible.

    Real-life analogy:
        Think of a traffic light. When it's RED, cars must stop.
        When it's GREEN, cars can go. The same object (traffic light)
        behaves differently depending on its current state.
    """

    @abstractmethod
    def process(self, order: OnlineOrder) -> str:
        ...

    @abstractmethod
    def cancel(self, order: OnlineOrder) -> str:
        ...

    @abstractmethod
    def ship(self, order: OnlineOrder) -> str:
        ...

    @abstractmethod
    def deliver(self, order: OnlineOrder) -> str:
        ...

    @abstractmethod
    def get_status(self) -> str:
        ...


class PendingState(OrderState):
    """Order is created but not yet processed."""

    def process(self, order: OnlineOrder) -> str:
        order.set_state(ProcessingState())
        return "✅ Order is now being processed!"

    def cancel(self, order: OnlineOrder) -> str:
        order.set_state(CancelledState())
        return "❌ Order cancelled."

    def ship(self, order: OnlineOrder) -> str:
        return "⚠️ Can't ship — order hasn't been processed yet!"

    def deliver(self, order: OnlineOrder) -> str:
        return "⚠️ Can't deliver — order hasn't been shipped yet!"

    def get_status(self) -> str:
        return "📋 PENDING"


class ProcessingState(OrderState):
    """Order is being prepared."""

    def process(self, order: OnlineOrder) -> str:
        return "⚠️ Order is already being processed!"

    def cancel(self, order: OnlineOrder) -> str:
        order.set_state(CancelledState())
        return "❌ Order cancelled during processing."

    def ship(self, order: OnlineOrder) -> str:
        order.set_state(ShippedState())
        return "📦 Order shipped!"

    def deliver(self, order: OnlineOrder) -> str:
        return "⚠️ Can't deliver — order hasn't been shipped yet!"

    def get_status(self) -> str:
        return "⚙️ PROCESSING"


class ShippedState(OrderState):
    """Order has been shipped and is in transit."""

    def process(self, order: OnlineOrder) -> str:
        return "⚠️ Order is already shipped!"

    def cancel(self, order: OnlineOrder) -> str:
        return "⚠️ Can't cancel — order is already in transit!"

    def ship(self, order: OnlineOrder) -> str:
        return "⚠️ Order is already shipped!"

    def deliver(self, order: OnlineOrder) -> str:
        order.set_state(DeliveredState())
        return "🎉 Order delivered successfully!"

    def get_status(self) -> str:
        return "🚚 SHIPPED"


class DeliveredState(OrderState):
    """Order has been delivered."""

    def process(self, order: OnlineOrder) -> str:
        return "⚠️ Order already delivered — nothing to process!"

    def cancel(self, order: OnlineOrder) -> str:
        return "⚠️ Can't cancel — order already delivered. Please request a return."

    def ship(self, order: OnlineOrder) -> str:
        return "⚠️ Order already delivered!"

    def deliver(self, order: OnlineOrder) -> str:
        return "⚠️ Order was already delivered!"

    def get_status(self) -> str:
        return "✅ DELIVERED"


class CancelledState(OrderState):
    """Order has been cancelled."""

    def process(self, order: OnlineOrder) -> str:
        return "⚠️ Can't process — order was cancelled."

    def cancel(self, order: OnlineOrder) -> str:
        return "⚠️ Order is already cancelled."

    def ship(self, order: OnlineOrder) -> str:
        return "⚠️ Can't ship — order was cancelled."

    def deliver(self, order: OnlineOrder) -> str:
        return "⚠️ Can't deliver — order was cancelled."

    def get_status(self) -> str:
        return "❌ CANCELLED"


class OnlineOrder:
    """
    Context: The order whose behavior changes based on its state.
    """

    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        self._state: OrderState = PendingState()

    def set_state(self, state: OrderState) -> None:
        self._state = state

    def process(self) -> str:
        return self._state.process(self)

    def cancel(self) -> str:
        return self._state.cancel(self)

    def ship(self) -> str:
        return self._state.ship(self)

    def deliver(self) -> str:
        return self._state.deliver(self)

    def get_status(self) -> str:
        return f"Order {self.order_id}: {self._state.get_status()}"


# ---------------------------------------------------------------------------
# Real-World Example 2: Audio Player (Play/Pause/Stop)
# ---------------------------------------------------------------------------


class PlayerState(ABC):
    @abstractmethod
    def play(self, player: AudioPlayer) -> str:
        ...

    @abstractmethod
    def pause(self, player: AudioPlayer) -> str:
        ...

    @abstractmethod
    def stop(self, player: AudioPlayer) -> str:
        ...

    @abstractmethod
    def get_status(self) -> str:
        ...


class StoppedPlayerState(PlayerState):
    def play(self, player: AudioPlayer) -> str:
        player.set_state(PlayingState())
        return "▶️  Playing music!"

    def pause(self, player: AudioPlayer) -> str:
        return "⚠️ Can't pause — nothing is playing!"

    def stop(self, player: AudioPlayer) -> str:
        return "⚠️ Already stopped."

    def get_status(self) -> str:
        return "⏹️  Stopped"


class PlayingState(PlayerState):
    def play(self, player: AudioPlayer) -> str:
        return "⚠️ Already playing!"

    def pause(self, player: AudioPlayer) -> str:
        player.set_state(PausedState())
        return "⏸️  Paused."

    def stop(self, player: AudioPlayer) -> str:
        player.set_state(StoppedPlayerState())
        return "⏹️  Stopped."

    def get_status(self) -> str:
        return "▶️  Playing"


class PausedState(PlayerState):
    def play(self, player: AudioPlayer) -> str:
        player.set_state(PlayingState())
        return "▶️  Resumed playing!"

    def pause(self, player: AudioPlayer) -> str:
        return "⚠️ Already paused!"

    def stop(self, player: AudioPlayer) -> str:
        player.set_state(StoppedPlayerState())
        return "⏹️  Stopped."

    def get_status(self) -> str:
        return "⏸️  Paused"


class AudioPlayer:
    def __init__(self, song: str) -> None:
        self.song = song
        self._state: PlayerState = StoppedPlayerState()

    def set_state(self, state: PlayerState) -> None:
        self._state = state

    def play(self) -> str:
        return self._state.play(self)

    def pause(self) -> str:
        return self._state.pause(self)

    def stop(self) -> str:
        return self._state.stop(self)

    def get_status(self) -> str:
        return f"🎵 {self.song}: {self._state.get_status()}"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the State pattern demonstration."""
    print("=" * 60)
    print("  STATE PATTERN DEMO")
    print("=" * 60)

    # --- Order Processing Example ---
    print("\n📦 Example 1: Order Processing")
    print("-" * 50)

    order = OnlineOrder("ORD-001")
    print(f"  {order.get_status()}")

    actions = [
        ("Process", order.process),
        ("Ship", order.ship),
        ("Cancel (too late!)", order.cancel),
        ("Deliver", order.deliver),
        ("Deliver (again?)", order.deliver),
    ]

    for label, action in actions:
        result = action()
        print(f"  {label}: {result}")
        print(f"  {order.get_status()}")

    # Try a cancelled order
    print("\n  --- Order that gets cancelled early ---")
    order2 = OnlineOrder("ORD-002")
    print(f"  {order2.get_status()}")
    print(f"  Cancel: {order2.cancel()}")
    print(f"  {order2.get_status()}")
    print(f"  Process: {order2.process()}")

    # --- Audio Player Example ---
    print("\n\n🎵 Example 2: Audio Player")
    print("-" * 50)

    player = AudioPlayer("Bohemian Rhapsody")
    print(f"  {player.get_status()}")

    actions_player = [
        player.play,
        player.pause,
        player.play,
        player.stop,
        player.pause,  # Can't pause when stopped
    ]

    for action in actions_player:
        result = action()
        print(f"  {result}")
        print(f"  {player.get_status()}")


if __name__ == "__main__":
    demo()
