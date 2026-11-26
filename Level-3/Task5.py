import os


class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def to_file_format(self):
        """Convert task data into a pipe-separated string."""
        return (
            f"{self.task_id}|{self.title}|"
            f"{self.description}|{self.status}\n"
        )


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load existing tasks from the text file."""
        self.tasks = []

        if not os.path.exists(self.filename):
            print("No existing task file found. Starting fresh.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.rstrip("\n").split("|")

                    if len(parts) != 4:
                        print("Skipping invalid task record.")
                        continue

                    task_id, title, description, status = parts

                    try:
                        task_id = int(task_id)
                    except ValueError:
                        print("Skipping task with invalid ID.")
                        continue

                    self.tasks.append(
                        Task(task_id, title, description, status)
                    )

            print(f"Loaded {len(self.tasks)} task(s) successfully.")

        except OSError as error:
            print(f"Error loading tasks: {error}")

    def save_tasks(self):
        """Save all tasks to the text file."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                for task in self.tasks:
                    file.write(task.to_file_format())

            print("Tasks saved successfully.")

        except OSError as error:
            print(f"Error saving tasks: {error}")

    def add_task(self):
        title = input("Enter task title: ").strip()

        if not title:
            print("Task title cannot be empty.")
            return

        description = input("Enter task description: ").strip()

        new_id = max(
            (task.task_id for task in self.tasks),
            default=0
        ) + 1

        task = Task(new_id, title, description)
        self.tasks.append(task)

        self.save_tasks()
        print(f"Task added successfully! ID: {new_id}")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n========== YOUR TASKS ==========")

        for task in self.tasks:
            print(f"\nID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status}")

        print("\n================================")

    def update_task(self):
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        task = next(
            (task for task in self.tasks if task.task_id == task_id),
            None
        )

        if task is None:
            print("Task not found.")
            return

        print("1. Update title")
        print("2. Update description")
        print("3. Mark as completed")
        print("4. Mark as pending")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter new title: ").strip()
            if title:
                task.title = title
            else:
                print("Title cannot be empty.")
                return

        elif choice == "2":
            task.description = input("Enter new description: ").strip()

        elif choice == "3":
            task.status = "Completed"

        elif choice == "4":
            task.status = "Pending"

        else:
            print("Invalid choice.")
            return

        self.save_tasks()
        print("Task updated successfully.")

    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        task = next(
            (task for task in self.tasks if task.task_id == task_id),
            None
        )

        if task is None:
            print("Task not found.")
            return

        self.tasks.remove(task)
        self.save_tasks()
        print("Task deleted successfully.")

    def run(self):
        while True:
            print("\n========== TASK MANAGER ==========")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.update_task()

            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                self.save_tasks()
                print("Exiting Task Manager. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()
