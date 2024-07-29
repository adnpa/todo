import datetime
from typing import List

from src import db
from src.task import Task
from src.constant import LOW


class Todo:
    dbservice = db.DBService()

    def __init__(self):
        pass

    def get_tasks(self) -> List[Task]:
        return self.dbservice.list_todos()

    def get_task(self, tid):
        return self.dbservice.get_task(tid)

    def create_task(self, task) -> None:
        """
        创建一个任务
        """
        self.dbservice.add_todo(task)

    def delete_task(self, tid) -> None:
        """

        """
        self.dbservice.delete_todo(tid)

    def update_task(self, tid, **kwargs) -> None:
        self.dbservice.update_task(tid, **kwargs)

    def negate_task(self, tid):
        self.dbservice.negate_task(tid)
