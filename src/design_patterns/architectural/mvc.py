"""
MVC (Model-View-Controller) Pattern
=====================================
Separates an application into three interconnected components:
- Model: The data and business logic
- View: The presentation layer (what the user sees)
- Controller: Handles user input and updates Model and View

Real-World Example: Task Management App
Think of a restaurant:
- Model = The kitchen (prepares the food / data)
- View = The menu and plates (presents the food / data to the customer)
- Controller = The waiter (takes orders from customer, tells kitchen what to cook)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


# ---------------------------------------------------------------------------
# MODEL: Data and Business Logic
# ---------------------------------------------------------------------------


class TaskPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


@dataclass
class Task:
    """A single task."""
    id: int
    title: str
    description: str = ""
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.TODO
    created_at: str = ""
    completed_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")


class TaskModel:
    """
    Model: Manages the task data and business rules.

    Real-life analogy:
        The kitchen in a restaurant. It holds all the ingredients (data),
        knows the recipes (business rules), and prepares the food.
        The kitchen doesn't care how the food is presented — that's the view's job.
    """

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1
        self._observers: list = []  # For notifying views of changes

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def _notify_observers(self) -> None:
        for observer in self._observers:
            observer.on_model_changed()

    def add_task(self, title: str, description: str = "",
                 priority: TaskPriority = TaskPriority.MEDIUM) -> Task:
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            priority=priority,
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        self._notify_observers()
        return task

    def get_task(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def update_status(self, task_id: int, status: TaskStatus) -> Task | None:
        task = self._tasks.get(task_id)
        if task:
            task.status = status
            if status == TaskStatus.DONE:
                task.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M")
            self._notify_observers()
        return task

    def delete_task(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            self._notify_observers()
            return True
        return False

    def get_tasks_by_status(self, status: TaskStatus) -> list[Task]:
        return [t for t in self._tasks.values() if t.status == status]

    def get_tasks_by_priority(self, priority: TaskPriority) -> list[Task]:
        return [t for t in self._tasks.values() if t.priority == priority]

    @property
    def stats(self) -> dict:
        total = len(self._tasks)
        done = len(self.get_tasks_by_status(TaskStatus.DONE))
        in_progress = len(self.get_tasks_by_status(TaskStatus.IN_PROGRESS))
        todo = len(self.get_tasks_by_status(TaskStatus.TODO))
        return {
            "total": total,
            "done": done,
            "in_progress": in_progress,
            "todo": todo,
            "completion_rate": f"{(done / total * 100):.0f}%" if total > 0 else "0%",
        }


# ---------------------------------------------------------------------------
# VIEW: Presentation Layer
# ---------------------------------------------------------------------------


class TaskView:
    """
    View: Displays task data to the user.

    Real-life analogy:
        The menu and the plate presentation in a restaurant.
        The view knows HOW to display things beautifully,
        but it doesn't know how to cook (that's the model's job).
    """

    def display_tasks(self, tasks: list[Task]) -> None:
        """Display a list of tasks."""
        if not tasks:
            print("    📭 No tasks found.")
            return

        print(f"    {'ID':<5} {'Title':<25} {'Priority':<10} {'Status':<15}")
        print(f"    {'-'*5} {'-'*25} {'-'*10} {'-'*15}")
        for task in tasks:
            priority_icon = {"Low": "🟢", "Medium": "🟡", "High": "🟠", "Critical": "🔴"}
            icon = priority_icon.get(task.priority.value, "⚪")
            print(f"    {task.id:<5} {task.title:<25} {icon} {task.priority.value:<8} {task.status.value:<15}")

    def display_task_detail(self, task: Task) -> None:
        """Display detailed view of a single task."""
        print(f"    📋 Task #{task.id}")
        print(f"       Title: {task.title}")
        print(f"       Description: {task.description or 'N/A'}")
        print(f"       Priority: {task.priority.value}")
        print(f"       Status: {task.status.value}")
        print(f"       Created: {task.created_at}")
        if task.completed_at:
            print(f"       Completed: {task.completed_at}")

    def display_stats(self, stats: dict) -> None:
        """Display task statistics."""
        print(f"    📊 Task Statistics:")
        print(f"       Total: {stats['total']}")
        print(f"       To Do: {stats['todo']} | In Progress: {stats['in_progress']} | Done: {stats['done']}")
        print(f"       Completion Rate: {stats['completion_rate']}")

    def display_message(self, message: str) -> None:
        """Display a message to the user."""
        print(f"    💬 {message}")

    def on_model_changed(self) -> None:
        """Called when the model changes (observer)."""
        pass  # In a real app, this would trigger a re-render


# ---------------------------------------------------------------------------
# CONTROLLER: Handles User Actions
# ---------------------------------------------------------------------------


class TaskController:
    """
    Controller: Handles user input and coordinates Model and View.

    Real-life analogy:
        The waiter in a restaurant. They take orders from the customer (user input),
        tell the kitchen what to cook (update model), and bring the food
        to the table (update view).
    """

    def __init__(self, model: TaskModel, view: TaskView) -> None:
        self._model = model
        self._view = view
        self._model.add_observer(view)

    def create_task(self, title: str, description: str = "",
                    priority: str = "medium") -> None:
        """Handle creating a new task."""
        priority_map = {
            "low": TaskPriority.LOW,
            "medium": TaskPriority.MEDIUM,
            "high": TaskPriority.HIGH,
            "critical": TaskPriority.CRITICAL,
        }
        task_priority = priority_map.get(priority.lower(), TaskPriority.MEDIUM)
        task = self._model.add_task(title, description, task_priority)
        self._view.display_message(f"Task '{task.title}' created (ID: {task.id})")

    def complete_task(self, task_id: int) -> None:
        """Mark a task as done."""
        task = self._model.update_status(task_id, TaskStatus.DONE)
        if task:
            self._view.display_message(f"Task '{task.title}' marked as done! ✅")
        else:
            self._view.display_message(f"Task #{task_id} not found.")

    def start_task(self, task_id: int) -> None:
        """Start working on a task."""
        task = self._model.update_status(task_id, TaskStatus.IN_PROGRESS)
        if task:
            self._view.display_message(f"Started working on '{task.title}' 🚀")
        else:
            self._view.display_message(f"Task #{task_id} not found.")

    def delete_task(self, task_id: int) -> None:
        """Delete a task."""
        if self._model.delete_task(task_id):
            self._view.display_message(f"Task #{task_id} deleted. 🗑️")
        else:
            self._view.display_message(f"Task #{task_id} not found.")

    def show_all_tasks(self) -> None:
        """Display all tasks."""
        tasks = self._model.get_all_tasks()
        self._view.display_tasks(tasks)

    def show_task(self, task_id: int) -> None:
        """Display a single task."""
        task = self._model.get_task(task_id)
        if task:
            self._view.display_task_detail(task)
        else:
            self._view.display_message(f"Task #{task_id} not found.")

    def show_stats(self) -> None:
        """Display task statistics."""
        self._view.display_stats(self._model.stats)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Run the MVC pattern demonstration."""
    print("=" * 60)
    print("  MVC (Model-View-Controller) PATTERN DEMO")
    print("=" * 60)

    print("\n📋 Task Management Application")
    print("-" * 50)

    # Create MVC components
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    # User actions (handled by Controller)
    print("\n  Creating tasks...")
    controller.create_task("Design database schema", "Create ERD for user module", "high")
    controller.create_task("Write API endpoints", "REST API for user CRUD", "critical")
    controller.create_task("Setup CI/CD pipeline", "GitHub Actions config", "medium")
    controller.create_task("Write unit tests", "Pytest for all services", "high")
    controller.create_task("Update README", "Add setup instructions", "low")

    # Show all tasks
    print("\n  All Tasks:")
    controller.show_all_tasks()

    # Start and complete some tasks
    print("\n  Working on tasks...")
    controller.start_task(1)
    controller.start_task(2)
    controller.complete_task(1)

    # Show updated view
    print("\n  Updated Task List:")
    controller.show_all_tasks()

    # Show stats
    print()
    controller.show_stats()

    # Show task detail
    print()
    controller.show_task(2)


if __name__ == "__main__":
    demo()
