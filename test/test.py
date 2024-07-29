import datetime
import logging
import os

from src.todo import Todo
from src.task import Task


# os.remove("../data/todo.db")


class TestTodo:
    todoSrv = Todo()

    def test_add_todo(self):
        self.todoSrv.create_task('test')
        assert self.todoSrv.get_tasks() == [Task(1, "test", "", 4, "2024-07-25", "", True)]

    def test_complete_todo(self):
        self.todoSrv.negate_task(1)

        assert self.todoSrv.get_task(1) == Task(1, "test", "test", 4, "2024-07-25", "", "abc")

    def test_update_task(self):
        self.todoSrv.update_task(1, description="test")
        assert self.todoSrv.get_tasks() == [Task(1, "test", "test", 4, "2024-07-25", "", 0)]

    def test_delete_todo(self):
        self.todoSrv.delete_task(1)
        assert self.todoSrv.get_tasks() == []

    def test_get_task(self):
        task = self.todoSrv.get_task(1)
        print(task)
        assert task == Task(2, "test", "test", 4, "2024-07-25", "", True)

    def test_get_tasks(self):
        tasks = self.todoSrv.get_tasks()
        assert tasks == [Task(2, "test", "test", 4, "2024-07-25", "", True)]
