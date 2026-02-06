"""
Proxy Pattern
==============
Provides a substitute or placeholder for another object.
Controls access to the original object, adding extra behavior.

Real-World Example: Internet Access Control at an Office
Think of it like a security guard at a building entrance.
The guard (proxy) checks your badge before letting you through
to the actual office (real object).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime


# ---------------------------------------------------------------------------
# Real-World Example 1: Internet Access Control (Protection Proxy)
# ---------------------------------------------------------------------------


class Internet(ABC):
    """Interface for internet access."""

    @abstractmethod
    def connect_to(self, url: str) -> str:
        ...


class RealInternet(Internet):
    """Actual internet connection — no restrictions."""

    def connect_to(self, url: str) -> str:
        return f"🌐 Connected to {url}"


class InternetProxy(Internet):
    """
    Controls internet access — blocks certain websites.

    Real-life analogy:
        Think of your school's Wi-Fi. You can visit educational sites,
        but social media might be blocked. The school's firewall
        is acting as a PROXY — it decides what you can access.
    """

    _blocked_sites: list[str] = [
        "facebook.com",
        "twitter.com",
        "instagram.com",
        "tiktok.com",
        "reddit.com",
    ]

    def __init__(self) -> None:
        self._real_internet = RealInternet()
        self._access_log: list[dict[str, str]] = []

    def connect_to(self, url: str) -> str:
        # Check if the site is blocked
        for blocked in self._blocked_sites:
            if blocked in url.lower():
                entry = {"url": url, "status": "BLOCKED", "time": str(datetime.now())}
                self._access_log.append(entry)
                return f"🚫 Access BLOCKED: {url} is not allowed!"

        # Allow access and log it
        entry = {"url": url, "status": "ALLOWED", "time": str(datetime.now())}
        self._access_log.append(entry)
        return self._real_internet.connect_to(url)

    def get_access_log(self) -> list[dict[str, str]]:
        """Get the access log (extra functionality the proxy provides)."""
        return self._access_log.copy()


# ---------------------------------------------------------------------------
# Real-World Example 2: Caching Proxy for API Calls
# ---------------------------------------------------------------------------


class WeatherAPI(ABC):
    """Interface for weather data retrieval."""

    @abstractmethod
    def get_weather(self, city: str) -> dict:
        ...


class RealWeatherAPI(WeatherAPI):
    """Actual weather API — slow and expensive to call."""

    def __init__(self) -> None:
        self.call_count = 0

    def get_weather(self, city: str) -> dict:
        self.call_count += 1
        # Simulate an expensive API call
        return {
            "city": city,
            "temperature": 22,
            "condition": "Sunny",
            "humidity": 45,
            "source": "Live API (expensive call!)",
        }


class CachingWeatherProxy(WeatherAPI):
    """
    Caches weather data to avoid calling the real API repeatedly.

    Real-life analogy:
        Think of checking the weather app. The first time, it fetches
        live data from the internet. But if you check again 2 minutes later,
        it shows you the CACHED data instead of fetching again.
        This saves battery and data!
    """

    def __init__(self, cache_ttl_seconds: int = 300) -> None:
        self._real_api = RealWeatherAPI()
        self._cache: dict[str, dict] = {}
        self._cache_timestamps: dict[str, datetime] = {}
        self._cache_ttl = cache_ttl_seconds
        self.cache_hits = 0
        self.cache_misses = 0

    def get_weather(self, city: str) -> dict:
        city_key = city.lower()

        # Check if we have a fresh cached result
        if city_key in self._cache:
            cached_time = self._cache_timestamps[city_key]
            age = (datetime.now() - cached_time).total_seconds()
            if age < self._cache_ttl:
                self.cache_hits += 1
                result = self._cache[city_key].copy()
                result["source"] = f"Cache (age: {age:.0f}s)"
                return result

        # Cache miss — call the real API
        self.cache_misses += 1
        result = self._real_api.get_weather(city)
        self._cache[city_key] = result
        self._cache_timestamps[city_key] = datetime.now()
        return result

    def get_stats(self) -> dict:
        return {
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "real_api_calls": self._real_api.call_count,
        }


# ---------------------------------------------------------------------------
# Real-World Example 3: Lazy Loading Proxy
# ---------------------------------------------------------------------------


class HeavyImage(ABC):
    """Interface for an image."""

    @abstractmethod
    def display(self) -> str:
        ...


class RealImage(HeavyImage):
    """
    A heavy image that takes time to load.
    Loading happens in __init__ (when created).
    """

    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        self._loaded = True
        self._data = f"[Image data for {self._filename}]"

    def display(self) -> str:
        return f"🖼️  Displaying {self._filename}"


class LazyImageProxy(HeavyImage):
    """
    Only loads the image when it's actually needed (displayed).

    Real-life analogy:
        Think of scrolling Instagram. The photos at the bottom
        don't load until you scroll down to them. That saves memory
        and makes the app load faster!
    """

    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._real_image: RealImage | None = None

    def display(self) -> str:
        if self._real_image is None:
            print(f"    ⏳ Lazy loading {self._filename}...")
            self._real_image = RealImage(self._filename)
        return self._real_image.display()


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Proxy pattern demonstration."""
    print("=" * 60)
    print("  PROXY PATTERN DEMO")
    print("=" * 60)

    # --- Internet Access Control ---
    print("\n🔒 Example 1: Internet Access Control Proxy")
    print("-" * 40)

    internet = InternetProxy()
    urls = [
        "https://stackoverflow.com",
        "https://facebook.com",
        "https://github.com",
        "https://instagram.com/reels",
        "https://docs.python.org",
    ]
    for url in urls:
        result = internet.connect_to(url)
        print(f"  {result}")

    # --- Caching Proxy ---
    print("\n⚡ Example 2: Caching Weather API Proxy")
    print("-" * 40)

    weather = CachingWeatherProxy(cache_ttl_seconds=300)

    cities = ["New York", "London", "New York", "Tokyo", "London", "New York"]
    for city in cities:
        data = weather.get_weather(city)
        print(f"  {city}: {data['temperature']}°C, {data['condition']} — {data['source']}")

    stats = weather.get_stats()
    print(f"\n  📊 Stats: {stats}")

    # --- Lazy Loading Proxy ---
    print("\n🖼️  Example 3: Lazy Loading Image Proxy")
    print("-" * 40)

    # Create proxy objects — images are NOT loaded yet!
    images = [
        LazyImageProxy("photo1.jpg"),
        LazyImageProxy("photo2.jpg"),
        LazyImageProxy("photo3.jpg"),
    ]

    print("  Images created (not loaded yet!)")

    # Only load when displayed
    print(f"\n  {images[0].display()}")  # Loads now!
    print(f"  {images[0].display()}")    # Already loaded — no delay!
    print(f"  {images[2].display()}")    # Loads now!


if __name__ == "__main__":
    demo()
