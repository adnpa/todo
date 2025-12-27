from task_list import TaskList

class TaskManager:
    # ll = {}
    # {list_id, list}
    # {task_id, task_list}

    # def __init__(self):
    # self.tasks = TaskList()
    tl_l = []

    def create_task_list(self, name):
        """Initialize an empty task list."""
        self.tl_l.append(TaskList(name))

    def delete_task_list(self, position):
        """Delete a task list by position."""
        if 0 <= position < len(self.tl_l):
            self.tl_l.pop(position)

    def add_task(self, position, task):
        """Add a new task to the task list."""
        self.tl_l[position].append(task)

    def remove_task(self, position, task):
        """Remove a task from the task list."""
        if task in self.tl_l[position]:
            self.tl_l[position].remove(task)

    def get_tasks(self):
        """Return the list of tasks."""
        return self.tasks
