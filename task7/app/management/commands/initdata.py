from django.core.management.base import BaseCommand, CommandError
from app.models import User


class Command(BaseCommand):
    help = 'Create test data: users'

    def handle(self, *args, **options):
        print('Start!')

        # clear all users
        User.objects.all().delete()

        # Insert new users
        User.objects.create(
            first_name='James',
            last_name='Karter',
            email='james.karter@gmail.com',
            status=1,
        )
        User.objects.create(
            first_name='Mike',
            last_name='Hitch',
            email='mike.hith@gmail.com',
            status=5,
        )
        User.objects.create(
            first_name='Kate',
            last_name='Monson',
            email='kate@gmail.com',
            status=9,
        )
        User.objects.create(
            first_name='Alex',
            last_name='Midlton',
            email='alex.com',
            status=5,
        )
        count = User.objects.all().count()
        print(f'Success! Inserted records: {count}')
