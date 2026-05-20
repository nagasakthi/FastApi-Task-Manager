from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User

from app.schemas.user import (
    UserRegister,
    UserLogin
)

from app.utils.security import (
    hash_password,
    verify_password
)

from app.utils.jwt_handler import (
    create_access_token
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing = db.query(
        User
    ).filter(
        User.email == user.email
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    try:

        hashed = hash_password(
            user.password
        )

        new_user = User(
            username=user.username,
            email=user.email,
            password=hashed
        )

        db.add(
            new_user
        )

        db.commit()

        db.refresh(
            new_user
        )

        return {
            "message":
            "Registered"
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(
        User
    ).filter(
        User.email == user.email
    ).first()

    if not db_user:

        raise HTTPException(
            401,
            "Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):

        raise HTTPException(
            401,
            "Invalid credentials"
        )

    token = create_access_token(
        {
            "user":
            db_user.id
        }
    )

    return {
        "access_token":
        token
    }