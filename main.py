from fastapi import FastAPI
from task_manager import TaskManager
from pydantic import BaseModel


app = FastAPI()

tm = TaskManager()
tm.create_task_list("默认任务列表")
tm.add_task(0, "学习Python")

# ================================
# List
# ================================


@app.get("/task-lists")
async def get_task_lists():
    """获取任务列表基础信息"""
    # [{"pos":1, "name":"task1"}]
    result = []
    taskls = tm.get_tasklist_info()
    for i, tl in enumerate(taskls):
        result.append({"pos": i, "name": tl.name})
    return result


class CreateListReq(BaseModel):
    name: str


@app.post("/create-task-list")
async def create_task_list(req: CreateListReq):
    """创建新任务列表"""
    print(f"创建任务列表: {req.name}")
    tm.create_task_list(req.name)
    print(tm.get_tasklist_info())
    return {"message": "ok"}

class DeleteListReq(BaseModel):
    pos: int

@app.post("/delete-task-list")
async def delete_task_list(req: DeleteListReq):
    """删除任务列表"""
    tm.delete_task_list(req.pos)
    return {"message": "Hello World"}

# ================================
# Task
# ================================


@app.get("/tasks/{pos}")
async def tasks(pos: int):
    """获取任务列表"""
    result = []
    tasks = tm.get_tasks(pos)
    print(tasks)
    # for i, task in enumerate(tasks):
    #     print(task)
    # result.append({"pos": i, "name": task.name})
    return tasks


@app.get("/task_detail/")
async def task_detail(list_id: int, task_id: int):
    """获取任务详细信息"""
    return {"message": "Hello World"}


class CreateTaskReq(BaseModel):
    pos: int
    name: str


@app.post("/add-task")
async def add_task(req: CreateTaskReq):
    """添加新任务"""
    print(f"添加任务: {req.name} 到列表 {req.pos}")
    tm.add_task(req.pos, req.name)
    return {"message": "Hello World"}


@app.post("/remove_task")
async def remove_task():
    """删除任务"""
    return {"message": "Hello World"}


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# fastapi dev main.py
