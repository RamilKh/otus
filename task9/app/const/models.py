from django.db import models
from enum import Enum


class UserStatuses(models.IntegerChoices):
    User = 1
    Admin = 5
    Developer = 9


class UserDepartment(Enum):
    IT = 'IT'
    HR = 'HR'
    CEO = 'CEO'
