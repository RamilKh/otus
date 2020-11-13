from django.db import models


class UserStatuses(models.IntegerChoices):
    User = 1
    Admin = 5
    Developer = 9
