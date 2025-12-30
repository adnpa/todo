from fastapi import FastAPI
from task_manager import TaskManager
from db import DBService
from req import *

app = FastAPI()
conn = DBService()

# ================================
# List
# ================================


@app.get("/task-lists")
async def get_task_lists():
    """获取任务列表基础信息"""
    res = []
    lists = conn.get_lists()
    for list in lists:
        res.append({"id": list[0], "name": list[1]})
    return res


@app.post("/add-list")
async def add_list(req: AddListReq):
    conn.add_list(req.name)
    return {"msg": "ok"}


@app.post("/delete-list")
async def delete_list(req: DeleteListReq):
    conn.delete_list(req.id)
    return {"msg": "ok"}


@app.post("/list/update-name")
async def update_list_name(req: UpdateListNameReq):
    conn.update_list_name(req.id, req.name)
    return {"msg": "ok"}


# ================================
# Task
# ================================


@app.get("/lists/{id}/tasks")
async def tasks(id: int):
    tasks = conn.get_list_tasks(id)
    result = []
    for task in tasks:
        result.append(
            {"id": task[0], "name": task[1], "completed": task[2]})
    return result


@app.get("/task/{id}")
async def task_detail(id: int):
    task = conn.get_task(id)
    # return task
    if task:
        return {
            "id": task[0],
            "name": task[1],
            "completed": task[2],
            "list_id": task[3],
            # "description": task[2],
            # "priority": task[3],
            # "start_date": task[4],
            # "end_date": task[5],
            # "tags": task[6],
        }
    else:
        return None


@app.post("/add-task")
async def add_task(req: AddTaskReq):
    conn.add_task(req.id, req.name)
    return {"msg": "ok"}


@app.post("/delete_task")
async def delete_task(req: DeleteTaskReq):
    conn.delete_task(req.id)
    return {"msg": "ok"}


@app.post("/reverse-completed")
async def reverse_completed(req: ReverseCompleteReq):
    conn.reverse_completed(req.id)
    return {"msg": "ok"}


@app.post("/task/update-name")
async def update_task_name(req: UpdateTaskNameReq):
    conn.update_task_name(req.id, req.name)
    return {"msg": "ok"}


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# fastapi dev main.py
