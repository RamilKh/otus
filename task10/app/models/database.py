from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from .settings import CONVENTION

metadata = MetaData(naming_convention=CONVENTION)
db = SQLAlchemy(metadata=metadata)

__all__ = [
    "db"
]
