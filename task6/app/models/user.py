from .database import db
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=100), nullable=False, unique=True)
    password = Column(String(length=100), nullable=False)
    name = Column(String(length=100), nullable=False)


# class User(UserMixin):
#     id = 364
#     username = 'tardis'
#     password = '1111'
#
#     @property
#     def is_authenticated(self):
#         return True
#
#     @property
#     def is_active(self):
#         return True
#
#     @property
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.id
