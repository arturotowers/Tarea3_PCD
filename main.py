from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import Model
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Optional

app = FastAPI()

# Crea las tablas en la base de datos
Model.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserCreate(BaseModel):
    user_name: str = Field(min_length=1, max_length=100)
    user_id: int
    user_email: str = Field(min_length=1, max_length=100)
    age: Optional[int] = None
    recommendations: List[str]
    ZIP: Optional[str] = None


# Endpoint para crear un usuario
@app.post("/user/create")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Corregido el filtro para usar Model.User
    db_user = db.query(Model.User).filter(Model.User.user_email == user.user_email).first()
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    # Corregido para usar Model.User
    db_user = Model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Endpoint para actualizar un usuario
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    # Corregido el filtro para usar Model.User
    db_user = db.query(Model.User).filter(Model.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=400, detail='User not found')

    # Actualizando los campos del usuario
    db_user.user_name = user.user_name
    db_user.user_email = user.user_email
    db_user.age = user.age
    db_user.recommendations = user.recommendations
    db_user.ZIP = user.ZIP

    db.commit()
    db.refresh(db_user)
    return db_user


# Endpoint para obtener un usuario
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Corregido el filtro para usar Model.User
    db_user = db.query(Model.User).filter(Model.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=400, detail='User not found')
    return db_user


# Endpoint para eliminar un usuario
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Corregido el filtro para usar Model.User
    db_user = db.query(Model.User).filter(Model.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=400, detail='User not found')

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}
"""
Ejemplos de uso:
METODO POST
http://127.0.0.1:8000/user/create
{
    "user_name": "arturotowers",
    "user_id": 1,
    "user_email": "arturo.torres@iteso.mx",
    "age": 20,
    "recommendations": [],
    "ZIP": ""
}
METODO GET
http://127.0.0.1:8000/users/1

METODO PUT
{
    "user_name": "arturotowers12",
    "user_id": 1,
    "user_email": "arturo.torres@iteso.mx",
    "age": 21,
    "recommendations": [],
    "ZIP": ""
}

METODO DELETE
http://127.0.0.1:8000/users/1

"""
