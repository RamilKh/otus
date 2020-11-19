from django.db import models
from app.const.models import UserStatuses


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    department = models.CharField(max_length=100, null=False)
    secure_code = models.CharField(max_length=50)
    status = models.SmallIntegerField(choices=UserStatuses.choices, default=1)

    def __str__(self):
        return f'{self.department} - {self.secure_code}'


class User(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(max_length=100, default='-')
    last_name = models.CharField(max_length=100, default='-')
    email = models.EmailField(unique=True, null=False)
    photo = models.ImageField(upload_to='photo', null=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}, {self.email}'

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name}, {self.email}, {self.status}, {self.profile}'


class Token(models.Model):
    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'

    user = models.ForeignKey(User, on_delete=models.CASCADE)

