from sqlalchemy.orm import Session

from app.models.task import Task


def create_task(

    db: Session,

    title: str,

    owner_id: int

):

    task = Task(

        title=title,

        owner_id=owner_id
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task


def get_tasks(

    db: Session,

    owner_id: int

):

    return db.query(
        Task
    ).filter(

        Task.owner_id == owner_id

    ).all()


def delete_task(

    db: Session,

    task_id: int

):

    task = db.query(
        Task
    ).filter(

        Task.id == task_id

    ).first()

    if task:

        db.delete(task)

        db.commit()

    return task