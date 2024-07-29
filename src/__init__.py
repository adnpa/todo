import sqlite3
import src.task

sqlite3.register_adapter(task.Task, task.adapt_task)
sqlite3.register_converter("task", task.convert_task)
