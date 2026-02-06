"""
Template Method Pattern
========================
Defines the skeleton of an algorithm in a base class, letting subclasses
override specific steps without changing the overall structure.

Real-World Example: Making Different Beverages
Think of it like a recipe template. Making tea and coffee follow the SAME steps:
1. Boil water → 2. Brew → 3. Pour → 4. Add condiments
The TEMPLATE is the same, but the details (brew tea vs. brew coffee) differ.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Real-World Example 1: Data Processing Pipeline
# ---------------------------------------------------------------------------


class DataProcessor(ABC):
    """
    Template for processing data — the steps are fixed, but details vary.

    Real-life analogy:
        Think of cooking. Every recipe follows the same template:
        1. Gather ingredients
        2. Prepare ingredients
        3. Cook
        4. Serve
        The TEMPLATE is the same, but HOW you do each step depends
        on whether you're making pasta or a salad.
    """

    def process(self, source: str) -> dict:
        """
        Template method — defines the algorithm skeleton.
        Subclasses override individual steps, NOT this method.
        """
        print(f"    📁 Step 1: Reading data from {source}")
        raw_data = self.read_data(source)

        print(f"    🔍 Step 2: Validating data ({len(raw_data)} records)")
        valid_data = self.validate_data(raw_data)

        print(f"    🔄 Step 3: Transforming data ({len(valid_data)} valid records)")
        transformed = self.transform_data(valid_data)

        print(f"    💾 Step 4: Saving results")
        result = self.save_data(transformed)

        # Hook: optional step that subclasses CAN override
        self.on_complete(result)

        return result

    @abstractmethod
    def read_data(self, source: str) -> list[dict]:
        """Read raw data from the source."""
        ...

    @abstractmethod
    def validate_data(self, data: list[dict]) -> list[dict]:
        """Validate and filter the data."""
        ...

    @abstractmethod
    def transform_data(self, data: list[dict]) -> list[dict]:
        """Transform the data into the desired format."""
        ...

    @abstractmethod
    def save_data(self, data: list[dict]) -> dict:
        """Save the processed data."""
        ...

    def on_complete(self, result: dict) -> None:
        """Hook: called after processing completes. Override if needed."""
        pass


class CSVDataProcessor(DataProcessor):
    """Processes CSV data."""

    def read_data(self, source: str) -> list[dict]:
        # Simulate reading CSV
        return [
            {"name": "Alice", "age": "30", "city": "New York"},
            {"name": "", "age": "25", "city": "LA"},  # Invalid: empty name
            {"name": "Charlie", "age": "abc", "city": "Chicago"},  # Invalid: bad age
            {"name": "Diana", "age": "28", "city": "Houston"},
        ]

    def validate_data(self, data: list[dict]) -> list[dict]:
        valid = []
        for record in data:
            if record.get("name") and record.get("age", "").isdigit():
                valid.append(record)
        return valid

    def transform_data(self, data: list[dict]) -> list[dict]:
        return [
            {
                "full_name": record["name"].upper(),
                "age": int(record["age"]),
                "location": record["city"],
            }
            for record in data
        ]

    def save_data(self, data: list[dict]) -> dict:
        return {"format": "CSV", "records_saved": len(data), "data": data}


class JSONDataProcessor(DataProcessor):
    """Processes JSON data."""

    def read_data(self, source: str) -> list[dict]:
        return [
            {"product": "Laptop", "price": 999.99, "stock": 10},
            {"product": "", "price": -5, "stock": 0},  # Invalid
            {"product": "Phone", "price": 599.99, "stock": 25},
            {"product": "Tablet", "price": 399.99, "stock": 0},
        ]

    def validate_data(self, data: list[dict]) -> list[dict]:
        return [
            record for record in data
            if record.get("product") and record.get("price", 0) > 0
        ]

    def transform_data(self, data: list[dict]) -> list[dict]:
        return [
            {
                "item": record["product"],
                "price_usd": f"${record['price']:.2f}",
                "available": record["stock"] > 0,
            }
            for record in data
        ]

    def save_data(self, data: list[dict]) -> dict:
        return {"format": "JSON", "records_saved": len(data), "data": data}

    def on_complete(self, result: dict) -> None:
        print(f"    📊 JSON processing complete: {result['records_saved']} records saved")


# ---------------------------------------------------------------------------
# Real-World Example 2: Beverage Maker (Classic Example)
# ---------------------------------------------------------------------------


class BeverageMaker(ABC):
    """
    Template for making beverages.
    The steps are the same, but the details differ for each drink.
    """

    def make(self) -> str:
        """Template method — the recipe steps."""
        steps = []
        steps.append(self.boil_water())
        steps.append(self.brew())
        steps.append(self.pour_in_cup())
        if self.wants_condiments():  # Hook!
            steps.append(self.add_condiments())
        return " → ".join(steps)

    def boil_water(self) -> str:
        return "Boil water"

    @abstractmethod
    def brew(self) -> str:
        ...

    def pour_in_cup(self) -> str:
        return "Pour in cup"

    @abstractmethod
    def add_condiments(self) -> str:
        ...

    def wants_condiments(self) -> bool:
        """Hook: override to skip condiments."""
        return True


class TeaMaker(BeverageMaker):
    def brew(self) -> str:
        return "Steep tea bag"

    def add_condiments(self) -> str:
        return "Add lemon"


class CoffeeMaker(BeverageMaker):
    def brew(self) -> str:
        return "Drip brew coffee"

    def add_condiments(self) -> str:
        return "Add sugar and cream"


class HotChocolateMaker(BeverageMaker):
    def brew(self) -> str:
        return "Mix cocoa powder"

    def add_condiments(self) -> str:
        return "Add marshmallows"


class BlackCoffeeMaker(BeverageMaker):
    """Black coffee — no condiments!"""

    def brew(self) -> str:
        return "Brew strong espresso"

    def add_condiments(self) -> str:
        return ""

    def wants_condiments(self) -> bool:
        return False  # No condiments for black coffee!


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Template Method pattern demonstration."""
    print("=" * 60)
    print("  TEMPLATE METHOD PATTERN DEMO")
    print("=" * 60)

    # --- Data Processing Example ---
    print("\n📊 Example 1: Data Processing Pipeline")
    print("-" * 50)

    print("\n  Processing CSV data:")
    csv_processor = CSVDataProcessor()
    csv_result = csv_processor.process("users.csv")
    print(f"    Result: {csv_result['records_saved']} records in {csv_result['format']} format")

    print("\n  Processing JSON data:")
    json_processor = JSONDataProcessor()
    json_result = json_processor.process("products.json")
    print(f"    Result: {json_result['records_saved']} records in {json_result['format']} format")

    # --- Beverage Example ---
    print("\n\n☕ Example 2: Making Beverages")
    print("-" * 50)

    beverages = [
        ("Tea", TeaMaker()),
        ("Coffee", CoffeeMaker()),
        ("Hot Chocolate", HotChocolateMaker()),
        ("Black Coffee", BlackCoffeeMaker()),
    ]

    for name, maker in beverages:
        print(f"\n  {name}: {maker.make()}")


if __name__ == "__main__":
    demo()
