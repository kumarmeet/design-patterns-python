"""
Encapsulation — Protecting Your Data
======================================
Encapsulation means bundling data and the methods that operate on it
inside a class, and CONTROLLING who can access or change the data.

Real-World Analogy:
    Think of a vending machine 🥤
    You can press buttons (public methods) to get a drink,
    but you CAN'T open the machine and grab the money inside (private data).
    The machine PROTECTS its internal state.
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# 1. Public, Protected, and Private Access
# ---------------------------------------------------------------------------


class SmartPhone:
    """
    Demonstrates Python's access levels:
        public:    self.brand        → Anyone can access
        protected: self._battery     → Convention: "don't touch from outside" (single _)
        private:   self.__pin_code   → Name mangling: hard to access from outside (double __)

    Real-life analogy:
        Your phone's HOME SCREEN is public — anyone can see it.
        Your SETTINGS are protected — you probably shouldn't mess with them.
        Your PASSWORDS are private — nobody else should access them.
    """

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand              # Public — anyone can read/write
        self.model = model              # Public
        self._battery_level = 100       # Protected — "please don't touch"
        self.__pin_code = "1234"        # Private — hidden from outside
        self._apps: list[str] = []

    # --- Public methods (the buttons on the vending machine) ---

    def install_app(self, app_name: str) -> str:
        """Public: Install an app."""
        if self._battery_level < 5:
            return "❌ Battery too low to install apps"
        self._apps.append(app_name)
        self._drain_battery(2)  # Uses a protected method internally
        return f"✅ Installed {app_name}"

    def use_app(self, app_name: str) -> str:
        """Public: Use an app."""
        if app_name not in self._apps:
            return f"❌ {app_name} not installed"
        self._drain_battery(5)
        return f"📱 Using {app_name} (Battery: {self._battery_level}%)"

    def charge(self, amount: int = 100) -> str:
        """Public: Charge the phone."""
        self._battery_level = min(100, self._battery_level + amount)
        return f"🔋 Charged to {self._battery_level}%"

    def unlock(self, pin: str) -> str:
        """Public: Unlock with PIN."""
        if self.__verify_pin(pin):
            return "🔓 Phone unlocked!"
        return "🔒 Wrong PIN!"

    def get_battery_level(self) -> int:
        """Public: Read-only access to battery level."""
        return self._battery_level

    # --- Protected methods (internal helpers) ---

    def _drain_battery(self, amount: int) -> None:
        """Protected: Reduces battery. Should not be called directly from outside."""
        self._battery_level = max(0, self._battery_level - amount)

    # --- Private methods (deeply hidden) ---

    def __verify_pin(self, pin: str) -> bool:
        """Private: Verifies the PIN code. Cannot be called from outside."""
        return pin == self.__pin_code


# ---------------------------------------------------------------------------
# 2. Properties — Controlled Getters and Setters
# ---------------------------------------------------------------------------


class Temperature:
    """
    Uses @property to control how data is read and written.

    Real-life analogy:
        A thermostat has a display (getter) and a dial (setter).
        But the dial won't let you set the temperature above 35°C
        or below 5°C — it VALIDATES your input!

    In Python, @property lets you:
        - Read a value like an attribute (temp.celsius)
        - But run validation code when setting it
    """

    def __init__(self, celsius: float = 0.0) -> None:
        self._celsius = celsius  # Protected — access through property

    @property
    def celsius(self) -> float:
        """Getter: Read the temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Setter: Set temperature with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Computed property: Auto-converts to Fahrenheit."""
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Set temperature in Fahrenheit (auto-converts to Celsius)."""
        self.celsius = (value - 32) * 5 / 9

    def __str__(self) -> str:
        return f"🌡️  {self.celsius:.1f}°C / {self.fahrenheit:.1f}°F"


# ---------------------------------------------------------------------------
# 3. Real-World Example: User Account System
# ---------------------------------------------------------------------------


class UserAccount:
    """
    A realistic user account with proper encapsulation.

    - Password is PRIVATE — never exposed directly
    - Email has VALIDATION in its setter
    - Login attempts are TRACKED internally
    """

    MAX_LOGIN_ATTEMPTS = 5

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self._email = ""
        self.email = email  # Uses the property setter (with validation!)
        self.__password_hash = self.__hash_password(password)
        self.__login_attempts = 0
        self.__is_locked = False

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if "@" not in value or "." not in value:
            raise ValueError(f"Invalid email: {value}")
        self._email = value

    def login(self, password: str) -> str:
        """Attempt to log in."""
        if self.__is_locked:
            return "🔒 Account is locked due to too many failed attempts"

        if self.__hash_password(password) == self.__password_hash:
            self.__login_attempts = 0
            return f"✅ Welcome back, {self.username}!"
        else:
            self.__login_attempts += 1
            remaining = self.MAX_LOGIN_ATTEMPTS - self.__login_attempts
            if self.__login_attempts >= self.MAX_LOGIN_ATTEMPTS:
                self.__is_locked = True
                return "🔒 Account LOCKED — too many failed attempts"
            return f"❌ Wrong password. {remaining} attempts remaining"

    def change_password(self, old_password: str, new_password: str) -> str:
        """Change password (must verify old password first)."""
        if self.__hash_password(old_password) != self.__password_hash:
            return "❌ Old password is incorrect"
        if len(new_password) < 8:
            return "❌ New password must be at least 8 characters"
        self.__password_hash = self.__hash_password(new_password)
        return "✅ Password changed successfully"

    @staticmethod
    def __hash_password(password: str) -> int:
        """Private: Simple hash (real apps use bcrypt!)."""
        return hash(password + "salt_secret")

    def __str__(self) -> str:
        return f"👤 {self.username} ({self._email})"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Encapsulation demonstration."""
    print("=" * 60)
    print("  ENCAPSULATION — Protecting Your Data")
    print("=" * 60)

    # --- Access Levels ---
    print("\n📱 1. Public, Protected, and Private Access")
    print("-" * 40)
    phone = SmartPhone("Apple", "iPhone 15")

    print(f"  Brand (public): {phone.brand}")
    print(f"  Battery (protected): {phone._battery_level}%")

    # Private attributes are name-mangled:
    # phone.__pin_code → AttributeError!
    # But phone._SmartPhone__pin_code works (not recommended!)

    print(f"  {phone.install_app('Instagram')}")
    print(f"  {phone.install_app('YouTube')}")
    print(f"  {phone.use_app('Instagram')}")
    print(f"  {phone.unlock('1234')}")
    print(f"  {phone.unlock('0000')}")
    print(f"  Battery level: {phone.get_battery_level()}%")

    # --- Properties ---
    print("\n\n🌡️  2. Properties (Controlled Getters/Setters)")
    print("-" * 40)
    temp = Temperature(25)
    print(f"  {temp}")

    temp.celsius = 100  # Uses setter
    print(f"  Set to 100°C: {temp}")

    temp.fahrenheit = 72  # Converts automatically!
    print(f"  Set to 72°F: {temp}")

    try:
        temp.celsius = -300  # Below absolute zero!
    except ValueError as e:
        print(f"  ❌ Validation: {e}")

    # --- User Account ---
    print("\n\n👤 3. User Account (Real-World Encapsulation)")
    print("-" * 40)
    user = UserAccount("alice_dev", "alice@example.com", "secretpass123")
    print(f"  {user}")

    print(f"  {user.login('wrong_password')}")
    print(f"  {user.login('wrong_password')}")
    print(f"  {user.login('secretpass123')}")

    print(f"  {user.change_password('secretpass123', 'newpass456789')}")
    print(f"  {user.login('newpass456789')}")

    # Email validation
    try:
        user.email = "invalid-email"
    except ValueError as e:
        print(f"  ❌ Email validation: {e}")


if __name__ == "__main__":
    demo()
