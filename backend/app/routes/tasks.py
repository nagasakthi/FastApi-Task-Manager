from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.dependencies import (
    get_current_user
)

from app.models.task import Task

from app.schemas.task import (
    TaskCreate,
    TaskUpdate
)

router = APIRouter()


@router.post("/tasks")

def create_task(

    task: TaskCreate,

    db: Session = Depends(
        get_db
    ),

    current_user = Depends(
        get_current_user
    )

):

    new_task = Task(

        title=task.title,

        owner_id=current_user.id
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task


@router.get("/tasks")

def get_tasks(

    page: int = 1,

    limit: int = 5,

    completed: bool = None,

    db: Session = Depends(
        get_db
    ),

    current_user = Depends(
        get_current_user
    )

):

    q = db.query(Task).filter(

        Task.owner_id ==
        current_user.id

    )

    if completed is not None:

        q = q.filter(
            Task.completed ==
            completed
        )

    offset = (
        page - 1
    ) * limit

    return q.offset(
        offset
    ).limit(
        limit
    ).all()


@router.get(
    "/tasks/{id}"
)

def get_task(

    id: int,

    db: Session = Depends(
        get_db
    ),

    current_user = Depends(
        get_current_user
    )

):

    task = db.query(
        Task
    ).filter(

        Task.id == id,

        Task.owner_id ==
        current_user.id

    ).first()

    if not task:

        raise HTTPException(
            404,
            "Task not found"
        )

    return task


@router.put(
    "/tasks/{id}"
)

def update_task(

    id: int,

    data: TaskUpdate,

    db: Session = Depends(
        get_db
    ),

    current_user = Depends(
        get_current_user
    )

):

    task = db.query(
        Task
    ).filter(

        Task.id == id,

        Task.owner_id ==
        current_user.id

    ).first()

    if not task:

        raise HTTPException(
            404
        )

    task.completed = data.completed

    db.commit()

    db.refresh(task)

    return task


@router.delete(
    "/tasks/{id}"
)

def delete_task(

    id: int,

    db: Session = Depends(
        get_db
    ),

    current_user = Depends(
        get_current_user
    )

):

    task = db.query(
        Task
    ).filter(

        Task.id == id,

        Task.owner_id ==
        current_user.id

    ).first()

    if not task:

        raise HTTPException(
            404
        )

    db.delete(task)

    db.commit()

    return {
        "message":
        "Deleted"
    }