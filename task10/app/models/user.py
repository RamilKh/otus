from .database import db
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=100), nullable=False, unique=True)
    password = Column(String(length=100), nullable=False)
    name = Column(String(length=100), nullable=False)
