from django.db import models
from app.const.models import USER_STATUSES


class User(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(max_length=100, default='-')
    last_name = models.CharField(max_length=100, default='-')
    email = models.EmailField(unique=True, null=False)
    status = models.SmallIntegerField(choices=USER_STATUSES, default=1)
