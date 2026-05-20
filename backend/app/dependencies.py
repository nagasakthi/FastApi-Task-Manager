from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer

from jose import jwt

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User


SECRET_KEY="SECRET_KEY"

ALGORITHM="HS256"

security=HTTPBearer()


def get_current_user(

    credentials=Depends(
        security
    ),

    db:Session=Depends(
        get_db
    )

):

    token=credentials.credentials

    try:

        payload=jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[
                ALGORITHM
            ]
        )

        user_id=payload.get(
            "user"
        )

    except:

        raise HTTPException(
            401,
            "Invalid token"
        )

    user=db.query(User).filter(
        User.id==user_id
    ).first()

    return user