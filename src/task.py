import sqlite3


class Task:
    def __init__(self, tid, title, description, priority, deadline, tag, completed=False):
        self.id = tid
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.tag = tag
        self.completed = completed

    def __str__(self):
        return f'{self.id}: {self.title}: {self.description}: {self.priority}: {self.deadline}: {self.tag} : {self.completed}'

    @classmethod
    def init_by_list(cls, args):
        tid, title, description, priority, deadline, tag, completed = args
        completed = True if completed == 1 else False
        return cls(tid, title, description, priority, deadline, tag, completed)

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.id};{self.title};{self.description};{self.priority};{self.deadline};{self.tag}"

    def __repr__(self):
        return f"Task({self.id}, {self.title}, {self.description}, {self.priority}, {self.deadline}, {self.tag})"

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.id == other.id

    def finish(self):
        self.deadline = None


def adapt_task(task):
    return f"{task.id};{task.title};{task.description};{task.priority};{task.tag}"


def convert_task(s):
    tid, title, description, priority, deadline, tag = list(s.split(b";"))
    return Task(tid, title, description, priority, deadline, tag)
