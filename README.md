# FastAPI Task Manager

Task Manager Web Application built using FastAPI with JWT Authentication and SQLite database.

## Features

### Authentication
- User Registration
- User Login
- JWT Authentication
- Password Hashing (bcrypt)

### Task Management
- Create Task
- View Tasks
- View Single Task
- Update Task Status
- Delete Task
- User-specific task access

### Extra Features
- Pagination
- Task filtering
- Docker support
- Frontend integration
- Unit testing with pytest

## Tech Stack

Backend:
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Passlib bcrypt

Frontend:
- HTML
- CSS
- JavaScript

## Project Structure

```text
backend/
 ├── app/
 ├── tests/
 ├── Dockerfile
 ├── requirements.txt

frontend/
 ├── login.html
 ├── dashboard.html
 ├── app.js
 ├── style.css
```

## Run Locally

Backend:

```bash
cd backend

uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend

python -m http.server 5500
```

Open:

Backend Docs:

http://127.0.0.1:8000/docs

Frontend:

http://localhost:5500/login.html

## Docker

Build:

```bash
docker build -t taskmanager .
```

Run:

```bash
docker run -p 8000:8000 taskmanager
```

## Testing

```bash
pytest
```

## GitHub Repository

https://github.com/nagasakthi/FastApi-Task-Manager