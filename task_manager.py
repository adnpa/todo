from task_list import TaskList
from task import Task

class TaskManager:
    # ll = {}
    # {list_id, list}
    # {task_id, task_list}

    # def __init__(self):
    # self.tasks = TaskList()
    def __init__(self):
        self.tl_l = []

    def get_tasklist_info(self):
        return self.tl_l

    def create_task_list(self, name):
        """Initialize an empty task list."""
        self.tl_l.append(TaskList(name))

    def delete_task_list(self, position):
        """Delete a task list by position."""
        if 0 <= position < len(self.tl_l):
            self.tl_l.pop(position)

    def add_task(self, position, name):
        """Add a new task to the task list."""
        self.tl_l[position].append(Task(name=name))

    def remove_task(self, position, task):
        """Remove a task from the task list."""
        if task in self.tl_l[position]:
            self.tl_l[position].remove(task)

    def get_tasks(self, position):
        """Return the list of tasks."""
        return self.tl_l[position].data
    
    
tm = TaskManager()
tm.create_task_list("默认任务列表")
tm.add_task(0, "学习Python")
print(tm.get_tasks(0))
print(tm.get_tasklist_info())

