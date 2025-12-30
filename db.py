import os
import sqlite3
from typing import List
# from main import tasks
# from task import Task

db_file = 'data/todo.db'


class DBService:

    def __init__(self):
        if not os.path.isdir("data"):
            os.makedirs("data")
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
#         self.c.execute('''

# CREATE TABLE task_list (
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
# 	name TEXT
# );

# CREATE TABLE tasks (
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
# 	name TEXT,
# 	description TEXT,
# 	priority INTEGER,
# 	start_date TEXT,
# 	end_date TEXT,
# 	tags TEXT,
# 	list_id INTEGER,
# 	CONSTRAINT tasks_FK FOREIGN KEY (list_id) REFERENCES task_list(id)
# );
#                      ''')

    def get_conn(self):
        return self.conn

    # def get_all(self):
    #     res = []
    #     self.c.execute("SELECT id, name FROM task_list;")
    #     lists = self.c.fetchall()
    #     for list in lists:
    #         id, name = list
    #         tks = self.get_list_tasks(id)
    #         res.append({"id": id, "name": name, "tasks": tks})
    #     return res

    def get_lists(self):
        self.c.execute("SELECT id, name FROM task_list;")
        lists = self.c.fetchall()
        return lists

    def get_list_tasks(self, lid):
        self.c.execute(
            "SELECT id, name, completed FROM tasks WHERE list_id = ?;", (lid,))
        tasks = self.c.fetchall()
        return tasks

    def add_list(self, name):
        self.c.execute(
            "INSERT INTO task_list (name) VALUES(?)", (name,))
        self.conn.commit()

    def delete_list(self, lid):
        self.c.execute("DELETE FROM task_list WHERE id = ?", (lid,))
        self.conn.commit()

    def update_list_name(self, lid, name):
        self.c.execute(
            "UPDATE task_list SET name = ? WHERE id = ?;", (name, lid))
        self.conn.commit()

    def get_task(self, tid):
        self.c.execute(
            "SELECT * FROM tasks WHERE id = ?;", (tid,))
        task = self.c.fetchone()
        return task

    def add_task(self, list_id, name):
        self.c.execute(
            "INSERT INTO tasks (name, list_id) VALUES(?, ?);", (name, list_id))
        self.conn.commit()

    def delete_task(self, tid):
        self.c.execute("DELETE FROM tasks WHERE id = ?", (tid,))
        self.conn.commit()

    def reverse_completed(self, tid):
        self.c.execute(
            "UPDATE tasks SET completed = completed * -1 WHERE id = ?;", (tid,))
        self.conn.commit()

    def update_task_name(self, tid, name):
        self.c.execute(
            "UPDATE tasks SET name = ? WHERE id = ?;", (name, tid))
        self.conn.commit()

    # def negate_task(self, tid):
    #     task = self.get_task(tid)
    #     boo = 0 if task.completed else 1
    #     self.c.execute("UPDATE todo SET completed = " +
    #                    str(boo) + " WHERE id = ?", (tid,))
    #     self.conn.commit()

    # def update_task(self, tid, **kwargs):
    #     set_clause = ', '.join([f"{field} = ?" for field in kwargs])
    #     sql = f"UPDATE todo SET {set_clause} WHERE id = ?"
    #     values = list(kwargs.values()) + [tid]
    #     self.c.execute(sql, values)
    #     self.conn.commit()

    # def delete_todo(self, tid):
    #     self.c.execute("DELETE FROM todo WHERE id = ?", (tid,))
    #     self.conn.commit()

    # def get_task(self, tid):
    #     self.c.execute("SELECT id, title, description, priority, deadline, tag, completed FROM todo WHERE id = ?",
    #                    (tid,))
    #     task = self.c.fetchone()
    #     return Task.init_by_list(task)

    # def list_todos(self) -> List[Task]:
    #     self.c.execute(
    #         "SELECT id, title, description, priority, deadline, tag, completed FROM todo")
    #     todos = self.c.fetchall()
    #     if not todos:
    #         return []
    #     else:
    #         return list(map(Task.init_by_list, todos))

    # def close(self):
    #     # 关闭数据库连接
    #     self.conn.close()

    # def get_info(self):
    #     # 执行一个查询语句
    #     self.c.execute("SELECT * FROM todo LIMIT 1")

    #     # 获取列信息
    #     columns = [column[0] for column in self.c.description]

    #     # 打印列名
    #     print(columns)

    # def test_insert(self):
    #     self.c.execute(
    #         "INSERT INTO todo (title, description, priority, deadline, tag, completed) VALUES('abc', '', 4, '2024-4-4', 'a', False);")
    #     self.conn.commit()


conn = DBService()
