"""
Iterator Pattern
=================
Provides a way to access elements of a collection sequentially
without exposing its underlying representation.

Real-World Example: Playlist Navigation
Think of scrolling through a playlist on Spotify. You press "Next" and "Previous"
without knowing how the songs are stored internally (array? linked list? database?).
The iterator gives you a simple way to navigate.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterator


# ---------------------------------------------------------------------------
# Real-World Example 1: Playlist Iterator
# ---------------------------------------------------------------------------


class Song:
    """Represents a song in a playlist."""

    def __init__(self, title: str, artist: str, duration_seconds: int) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration_seconds

    def __str__(self) -> str:
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"🎵 {self.title} — {self.artist} ({minutes}:{seconds:02d})"


class Playlist:
    """
    A playlist that supports iteration over songs.

    Real-life analogy:
        Think of a book. You don't need to know how the pages are bound
        together — you just flip to the next page. That's what an iterator does!
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._songs: list[Song] = []

    def add_song(self, song: Song) -> None:
        self._songs.append(song)

    def __len__(self) -> int:
        return len(self._songs)

    def __iter__(self) -> PlaylistIterator:
        """Return a forward iterator."""
        return PlaylistIterator(self._songs)

    def reverse_iterator(self) -> ReversePlaylistIterator:
        """Return a reverse iterator."""
        return ReversePlaylistIterator(self._songs)

    def shuffle_iterator(self) -> ShufflePlaylistIterator:
        """Return a shuffle iterator."""
        return ShufflePlaylistIterator(self._songs)


class PlaylistIterator:
    """Iterates through songs in order."""

    def __init__(self, songs: list[Song]) -> None:
        self._songs = songs
        self._index = 0

    def __iter__(self) -> PlaylistIterator:
        return self

    def __next__(self) -> Song:
        if self._index >= len(self._songs):
            raise StopIteration
        song = self._songs[self._index]
        self._index += 1
        return song

    def has_next(self) -> bool:
        return self._index < len(self._songs)


class ReversePlaylistIterator:
    """Iterates through songs in reverse order."""

    def __init__(self, songs: list[Song]) -> None:
        self._songs = songs
        self._index = len(songs) - 1

    def __iter__(self) -> ReversePlaylistIterator:
        return self

    def __next__(self) -> Song:
        if self._index < 0:
            raise StopIteration
        song = self._songs[self._index]
        self._index -= 1
        return song


class ShufflePlaylistIterator:
    """Iterates through songs in random order."""

    def __init__(self, songs: list[Song]) -> None:
        import random
        self._songs = songs.copy()
        random.shuffle(self._songs)
        self._index = 0

    def __iter__(self) -> ShufflePlaylistIterator:
        return self

    def __next__(self) -> Song:
        if self._index >= len(self._songs):
            raise StopIteration
        song = self._songs[self._index]
        self._index += 1
        return song


# ---------------------------------------------------------------------------
# Real-World Example 2: Paginated API Results
# ---------------------------------------------------------------------------


class PaginatedIterator:
    """
    Iterates over paginated results (like an API that returns 10 items per page).

    Real-life analogy:
        Think of Google search results. You see 10 results per page,
        and you click "Next" to see more. This iterator does that automatically!
    """

    def __init__(self, all_items: list[Any], page_size: int = 3) -> None:
        self._items = all_items
        self._page_size = page_size
        self._current_page = 0

    def __iter__(self) -> PaginatedIterator:
        return self

    def __next__(self) -> list[Any]:
        start = self._current_page * self._page_size
        if start >= len(self._items):
            raise StopIteration
        end = min(start + self._page_size, len(self._items))
        page = self._items[start:end]
        self._current_page += 1
        return page

    @property
    def total_pages(self) -> int:
        return -(-len(self._items) // self._page_size)  # Ceiling division


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Iterator pattern demonstration."""
    print("=" * 60)
    print("  ITERATOR PATTERN DEMO")
    print("=" * 60)

    # --- Playlist Example ---
    print("\n🎧 Example 1: Music Playlist")
    print("-" * 50)

    playlist = Playlist("My Favorites")
    playlist.add_song(Song("Bohemian Rhapsody", "Queen", 355))
    playlist.add_song(Song("Imagine", "John Lennon", 187))
    playlist.add_song(Song("Hotel California", "Eagles", 391))
    playlist.add_song(Song("Stairway to Heaven", "Led Zeppelin", 482))
    playlist.add_song(Song("Hey Jude", "The Beatles", 431))

    # Normal iteration (using Python's for loop!)
    print(f"\n  ▶️  Playing '{playlist.name}' (forward):")
    for song in playlist:
        print(f"    {song}")

    # Reverse iteration
    print(f"\n  ◀️  Playing '{playlist.name}' (reverse):")
    for song in playlist.reverse_iterator():
        print(f"    {song}")

    # Shuffle iteration
    print(f"\n  🔀 Playing '{playlist.name}' (shuffled):")
    for song in playlist.shuffle_iterator():
        print(f"    {song}")

    # --- Paginated Results Example ---
    print("\n\n📄 Example 2: Paginated Search Results")
    print("-" * 50)

    results = [f"Result #{i+1}" for i in range(10)]
    paginator = PaginatedIterator(results, page_size=3)
    print(f"  Total results: {len(results)}, Pages: {paginator.total_pages}")

    for page_num, page in enumerate(paginator, start=1):
        print(f"\n  📄 Page {page_num}:")
        for item in page:
            print(f"    • {item}")


if __name__ == "__main__":
    demo()
