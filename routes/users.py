from fastapi import APIRouter
from typing import List
from models import User,Role
from uuid import UUID, uuid4

user = APIRouter()


db: List[User] = [
    User(
        id="93a7880b-a44b-4d97-a6d6-fd4c4e638852", 
        first_name='Juan',
        last_name='Perez',
        role=[Role.admin]
        ),
    User(
        id="a2d85996-ac22-4799-b4b3-d65836af86c5", 
        first_name='Alex',
        last_name='Doe',
        role=[Role.admin, Role.user]
        )
]

@user.get('/api/v1/users')
def fetch_users():
    return db

@user.post('/api/v1/users')
def register_user(user: User):
    db.append(user)
    return db


@user.delete('api/v1/users/{user_id}')
def remove_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
