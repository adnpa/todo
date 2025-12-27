from collections import UserList


class TaskList(UserList):
    """A list of tasks."""

    def __init__(self, name: str, iterable=None):
        self.name = name
        super().__init__(iterable or [])

    def __repr__(self) -> str:
        return f"NamedList(name={self.name!r}, data={list(self.data)!r})"
