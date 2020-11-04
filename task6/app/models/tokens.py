from .database import db
from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint


class Tokens(db.Model):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String(length=100), nullable=False)
    protocol = Column(String(length=10), nullable=False)
    token = Column(String(length=50), nullable=False)
    status = Column(Integer, default=0)
    UniqueConstraint(host, protocol)
