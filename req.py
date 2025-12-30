
from pydantic import BaseModel
# Common


# List
class UpdateListNameReq(BaseModel):
    id: int
    name: str


class AddListReq(BaseModel):
    name: str


class DeleteListReq(BaseModel):
    id: int

# Task


class UpdateTaskNameReq(BaseModel):
    id: int
    name: str


class AddTaskReq(BaseModel):
    id: int
    name: str


class DeleteTaskReq(BaseModel):
    id: int


class ReverseCompleteReq(BaseModel):
    id: int
