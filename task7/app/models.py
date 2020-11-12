from django.db import models


class User(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    STATUS_CHOICES = [
        (1, 'User'),
        (5, 'Admin'),
        (9, 'Developer'),
    ]

    first_name = models.CharField(max_length=100, default='-')
    last_name = models.CharField(max_length=100, default='-')
    email = models.EmailField(unique=True, null=False)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
