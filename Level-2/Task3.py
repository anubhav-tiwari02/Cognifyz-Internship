class Task:
    """Represents an individual task."""

    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = "Pending"


class TaskManager:
    """Manages tasks and provides CRUD operations."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self):
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            return

        description = input("Enter task description: ").strip()
        task = Task(self.next_id, title, description)
        self.tasks.append(task)

        print(f"Task added successfully! ID: {self.next_id}")
        self.next_id += 1

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n========== TASK LIST ==========")
        for task in self.tasks:
            print(f"\nTask ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status}")

    def update_task(self):
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Please enter a valid numeric task ID.")
            return

        task = next(
            (item for item in self.tasks if item.task_id == task_id),
            None
        )

        if task is None:
            print("Task ID not found.")
            return

        print("\n1. Update title")
        print("2. Update description")
        print("3. Mark as completed")
        print("4. Mark as pending")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter new title: ").strip()
            if title:
                task.title = title
                print("Title updated successfully.")
            else:
                print("Title cannot be empty.")
        elif choice == "2":
            task.description = input("Enter new description: ").strip()
            print("Description updated successfully.")
        elif choice == "3":
            task.status = "Completed"
            print("Task marked as completed.")
        elif choice == "4":
            task.status = "Pending"
            print("Task marked as pending.")
        else:
            print("Invalid update option.")

    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Please enter a valid numeric task ID.")
            return

        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return

        print("Task ID not found.")


def main():
    manager = TaskManager()

    while True:
        print("\n================================")
        print("       TASK MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task()
        elif choice == "4":
            manager.delete_task()
        elif choice == "5":
            print("Thank you for using Task Manager!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
