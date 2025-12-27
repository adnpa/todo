from fastapi import FastAPI

app = FastAPI()

@app.get("/tasks")
async def tasks():
    """获取任务列表"""

@app.get("/task_detail/")
async def task_detail(list_id: int, task_id: int):
    """获取任务详细信息"""
    return {"message": "Hello World"}

@app.post("/create_task_list")
async def create_task_list():
    """创建新任务列表"""
    return {"message": "Hello World"}

@app.post("/delete_task_list")
async def delete_task_list():
    """删除任务列表"""
    return {"message": "Hello World"}



@app.post("/add_task")
async def add_task():
    """添加新任务"""
    return {"message": "Hello World"}

@app.post("/remove_task")
async def remove_task():
    """删除任务"""
    return {"message": "Hello World"}



# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# fastapi dev main.py
