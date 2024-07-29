import os
import sqlite3
from typing import List

from src.task import Task

db_file = 'data/todo.db'


class DBService:

    def __init__(self):
        if not os.path.isdir("data"):
            os.makedirs("data")
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS todo
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, priority INTEGER, deadline DATE, tag TEXT, completed BOOLEAN)''')

    def get_conn(self):
        return self.conn

    def add_todo(self, task):
        self.c.execute(
            "INSERT INTO todo (title, description, priority, deadline, tag, completed) VALUES(:title, :description, :priority, :deadline, :tag, :completed);",
            vars(task))
        self.conn.commit()

    def negate_task(self, tid):
        task = self.get_task(tid)
        boo = 0 if task.completed else 1
        self.c.execute("UPDATE todo SET completed = " + str(boo) + " WHERE id = ?", (tid,))
        self.conn.commit()

    def update_task(self, tid, **kwargs):
        set_clause = ', '.join([f"{field} = ?" for field in kwargs])
        sql = f"UPDATE todo SET {set_clause} WHERE id = ?"
        values = list(kwargs.values()) + [tid]
        self.c.execute(sql, values)
        self.conn.commit()

    def delete_todo(self, tid):
        self.c.execute("DELETE FROM todo WHERE id = ?", (tid,))
        self.conn.commit()

    def get_task(self, tid):
        self.c.execute("SELECT id, title, description, priority, deadline, tag, completed FROM todo WHERE id = ?",
                       (tid,))
        task = self.c.fetchone()
        return Task.init_by_list(task)

    def list_todos(self) -> List[Task]:
        self.c.execute("SELECT id, title, description, priority, deadline, tag, completed FROM todo")
        todos = self.c.fetchall()
        if not todos:
            return []
        else:
            return list(map(Task.init_by_list, todos))

    def close(self):
        # 关闭数据库连接
        self.conn.close()

    def get_info(self):
        # 执行一个查询语句
        self.c.execute("SELECT * FROM todo LIMIT 1")

        # 获取列信息
        columns = [column[0] for column in self.c.description]

        # 打印列名
        print(columns)

    def test_insert(self):
        self.c.execute(
            "INSERT INTO todo (title, description, priority, deadline, tag, completed) VALUES('abc', '', 4, '2024-4-4', 'a', False);")
        self.conn.commit()
