from django.core.management.base import BaseCommand, CommandError
from app.models import User, Profile


class Command(BaseCommand):
    help = 'Create test data: users'

    def handle(self, *args, **options):
        print('Start!')

        # clear all users
        User.objects.all().delete()
        Profile.objects.all().delete()

        # Insert new data
        profile = Profile.objects.create(department='HR', secure_code='009-ULQ-827', status=1)
        User.objects.create(first_name='James', last_name='Karter', email='james.karter@gmail.com', profile=profile)

        profile = Profile.objects.create(department='IT', secure_code='109-ULQ-828', status=5)
        User.objects.create(first_name='Mike', last_name='Hitch', email='mike.hith@gmail.com', profile=profile)

        profile = Profile.objects.create(department='CEO', secure_code='509-PLQ-127', status=5)
        User.objects.create(first_name='Kate', last_name='Monson', email='kate@gmail.com', profile=profile)

        profile = Profile.objects.create(department='IT', secure_code='009-ULQ-827', status=9)
        User.objects.create(first_name='Alex', last_name='Midlton', email='alex@gmail.com', profile=profile)

        # result
        count = User.objects.all().count()
        print(f'Success! Inserted records: {count}')
