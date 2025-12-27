
from dataclasses import dataclass, replace
from typing import Optional


class priority:
    Critical = 1
    High = 2
    Medium = 3
    Low = 4


@dataclass
class Task:
    id: str | None = None
    name: str
    compoleted: bool = False

    description: Optional[str] = None
    priority: Optional[int] = None
    tags: Optional[list[str]] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    # def __post_init__(self):
    # if self.id is None:
    # self.id = str(uuid.uuid4())
    # if self.priority is None:
    #     self.priority = DefaultTags.Medium

    def check(self):
        self.compoleted = not self.compoleted

    def replaced_by(self, other):
        """
        返回一个新 User：
        - id 来自当前对象
        - 其他字段来自 other
        """
        # 先复制 other，再把 id 改回 self.id
        return replace(other, id=self.id)
    
    
    
    # def __init__(self, name):
    #     self.id = str(uuid.uuid4())
    #     self.name = name
    #     self.priority = priority

    # def __repr__(self):
    #     return f"Task(name={self.name}, priority={self.priority})"
