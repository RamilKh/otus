from django.db import models
from app.const.models import UserStatuses
import os


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    department = models.CharField(max_length=100, null=False)
    secure_code = models.CharField(max_length=50)
    status = models.SmallIntegerField(choices=UserStatuses.choices, default=1)

    def __str__(self):
        return f'{self.department} - {self.secure_code}'

    @staticmethod
    def get_department_count(department):
        return Profile.objects.filter(department__exact=department).count()


class User(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(max_length=100, default='-')
    last_name = models.CharField(max_length=100, default='-')
    email = models.EmailField(unique=True, null=False)
    photo = models.ImageField(upload_to='photo', null=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}, {self.email}'

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name}, {self.email}, {self.profile}'

    @staticmethod
    def get_admins_count():
        return User.objects.filter(profile__status=UserStatuses.Admin).count()

    @staticmethod
    def get_developers_count():
        return User.objects.filter(profile__status=UserStatuses.Developer).count()

    @staticmethod
    def get_users_count():
        return User.objects.filter(profile__status=UserStatuses.User).count()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        # delete profile
        if self.profile:
            self.profile.delete()

        # delete photo
        if self.photo and os.path.isfile(self.photo.path):
            os.remove(self.photo.path)
