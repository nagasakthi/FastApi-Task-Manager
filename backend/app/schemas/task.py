from pydantic import BaseModel


class TaskCreate(
    BaseModel
):

    title: str


class TaskUpdate(
    BaseModel
):

    completed: bool


class TaskResponse(
    BaseModel
):

    id: int

    title: str

    completed: bool

    owner_id: int

    class Config:

        from_attributes = True