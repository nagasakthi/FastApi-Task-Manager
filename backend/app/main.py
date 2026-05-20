from fastapi import FastAPI
from app.database import (Base,engine)
from app.models.user import User
from app.models.task import Task
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth import (router as auth_router)
from app.routes.tasks import (router as task_router)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Task Manager API"
)

# this for FrontEnd
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

app.include_router(
    auth_router
)

app.include_router(
    task_router
)

@app.get("/")

def home():

    return {

        "message":
        "Task Manager Running"
    }