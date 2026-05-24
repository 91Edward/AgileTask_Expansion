class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def display_task(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} - {status}"


task = Task("Complete AgileTask setup")
print(task.display_task())