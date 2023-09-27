from fastapi import APIRouter, Form, HTTPException, UploadFile
from app.db import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Profile, User

router = APIRouter()


@router.post("/register/")
async def register_user(
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    phone: str = Form(...),
    profile_picture: UploadFile = Form(...),
):
    try:
        with SessionLocal() as db:
            profile_picture_data = await profile_picture.read()
            new_user = create_user_db(
                db, full_name, email, phone, password, profile_picture_data)
            return {"user_id": new_user.id, "message": "User registered successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/user/{user_id}/")
def get_user(user_id: int):
    try:
        with SessionLocal() as db:
            stmt = select(User, Profile).join(
                User, User.id == Profile.user_id).where(User.id == user_id)
            result = db.scalars(stmt).one_or_none()

            if result is None:
                raise HTTPException(status_code=404, detail="User not found")

            return result

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def create_user_db(db: Session, full_name: str, email: str, phone: str, password: str, profile_picture_data: bytes) -> User:
    existing_user = db.query(User).filter(
        (User.email == email) | (User.phone == phone)).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Email already registered")

    new_user = User(
        full_name=full_name,
        email=email,
        phone=phone,
        password=password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    new_profile = Profile(
        profile_picture=profile_picture_data,
        user_id=new_user.id
    )
    db.add(new_profile)
    db.commit()

    return new_user
