"""
Composite Pattern
==================
Composes objects into tree structures to represent part-whole hierarchies.
Lets clients treat individual objects and groups of objects the same way.

Real-World Example: File System (Files and Folders)
Think of it like a folder on your computer. A folder can contain files
AND other folders. You can ask for the "size" of a file or a folder
(which adds up all its contents) using the SAME method.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Real-World Example 1: File System
# ---------------------------------------------------------------------------


class FileSystemItem(ABC):
    """
    Component: something in a file system (file OR folder).

    Real-life analogy:
        Both a file and a folder can tell you their name and size.
        A folder just adds up the sizes of everything inside it.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def get_size(self) -> int:
        """Get size in KB."""
        ...

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display the item with indentation."""
        ...


class File(FileSystemItem):
    """A leaf node — a simple file with a fixed size."""

    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self._size = size

    def get_size(self) -> int:
        return self._size

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix}📄 {self.name} ({self._size} KB)"


class Folder(FileSystemItem):
    """A composite node — a folder that can contain files and other folders."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem) -> None:
        """Add a file or folder to this folder."""
        self._children.append(item)

    def remove(self, item: FileSystemItem) -> None:
        """Remove an item from this folder."""
        self._children.remove(item)

    def get_size(self) -> int:
        """Total size = sum of all children's sizes."""
        return sum(child.get_size() for child in self._children)

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        result = f"{prefix}📁 {self.name}/ ({self.get_size()} KB)"
        for child in self._children:
            result += "\n" + child.display(indent + 1)
        return result


# ---------------------------------------------------------------------------
# Real-World Example 2: Organization Hierarchy (Company Structure)
# ---------------------------------------------------------------------------


class Employee(ABC):
    """Component: any member of the organization."""

    def __init__(self, name: str, title: str, salary: float) -> None:
        self.name = name
        self.title = title
        self.salary = salary

    @abstractmethod
    def get_total_salary(self) -> float:
        ...

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        ...


class IndividualContributor(Employee):
    """Leaf: an employee with no direct reports."""

    def get_total_salary(self) -> float:
        return self.salary

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix}👤 {self.name} ({self.title}) — ${self.salary:,.0f}"


class Manager(Employee):
    """Composite: a manager who has team members under them."""

    def __init__(self, name: str, title: str, salary: float) -> None:
        super().__init__(name, title, salary)
        self._reports: list[Employee] = []

    def add_report(self, employee: Employee) -> None:
        self._reports.append(employee)

    def get_total_salary(self) -> float:
        """Total salary includes this manager + all reports."""
        return self.salary + sum(r.get_total_salary() for r in self._reports)

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        result = f"{prefix}👔 {self.name} ({self.title}) — ${self.salary:,.0f}"
        for report in self._reports:
            result += "\n" + report.display(indent + 1)
        return result

    def get_team_size(self) -> int:
        """Count total people in this subtree."""
        count = 1  # self
        for report in self._reports:
            if isinstance(report, Manager):
                count += report.get_team_size()
            else:
                count += 1
        return count


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the Composite pattern demonstration."""
    print("=" * 60)
    print("  COMPOSITE PATTERN DEMO")
    print("=" * 60)

    # --- File System Example ---
    print("\n📁 Example 1: File System")
    print("-" * 40)

    root = Folder("project")

    src = Folder("src")
    src.add(File("main.py", 15))
    src.add(File("utils.py", 8))
    src.add(File("config.py", 3))

    tests = Folder("tests")
    tests.add(File("test_main.py", 12))
    tests.add(File("test_utils.py", 6))

    docs = Folder("docs")
    docs.add(File("README.md", 5))
    docs.add(File("CONTRIBUTING.md", 3))

    root.add(src)
    root.add(tests)
    root.add(docs)
    root.add(File("pyproject.toml", 2))
    root.add(File(".gitignore", 1))

    print(root.display())
    print(f"\n  Total project size: {root.get_size()} KB")

    # --- Company Hierarchy Example ---
    print("\n\n🏢 Example 2: Company Organization")
    print("-" * 40)

    ceo = Manager("Alice", "CEO", 250_000)

    cto = Manager("Bob", "CTO", 200_000)
    dev_lead = Manager("Charlie", "Dev Lead", 150_000)
    dev_lead.add_report(IndividualContributor("Dave", "Senior Dev", 120_000))
    dev_lead.add_report(IndividualContributor("Eve", "Junior Dev", 80_000))
    dev_lead.add_report(IndividualContributor("Frank", "Junior Dev", 75_000))
    cto.add_report(dev_lead)
    cto.add_report(IndividualContributor("Grace", "DevOps Engineer", 130_000))

    cfo = Manager("Heidi", "CFO", 200_000)
    cfo.add_report(IndividualContributor("Ivan", "Accountant", 90_000))
    cfo.add_report(IndividualContributor("Judy", "Financial Analyst", 95_000))

    ceo.add_report(cto)
    ceo.add_report(cfo)

    print(ceo.display())
    print(f"\n  Total salary budget: ${ceo.get_total_salary():,.0f}")
    print(f"  Total team size: {ceo.get_team_size()} people")


if __name__ == "__main__":
    demo()
