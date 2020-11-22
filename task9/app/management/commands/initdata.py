from django.core.management.base import BaseCommand, CommandError
from app.models import User, Profile
from app.const.models import UserStatuses, UserDepartment
from faker import Faker


class Command(BaseCommand):
    help = 'Create test data: users'

    def handle(self, *args, **options):
        faker = Faker()

        # clear all users
        User.objects.all().delete()
        Profile.objects.all().delete()

        # Insert new data
        profile = Profile.objects.create(department=UserDepartment.HR.value, secure_code=faker.ssn(),
                                         status=UserStatuses.User)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(),
                            profile=profile)

        profile = Profile.objects.create(department=UserDepartment.IT.value, secure_code=faker.ssn(),
                                         status=UserStatuses.Developer)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(),
                            profile=profile)

        profile = Profile.objects.create(department=UserDepartment.CEO.value, secure_code=faker.ssn(),
                                         status=UserStatuses.Developer)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(),
                            profile=profile)

        profile = Profile.objects.create(department=UserDepartment.IT.value, secure_code=faker.ssn(),
                                         status=UserStatuses.Admin)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(),
                            profile=profile)

        profile = Profile.objects.create(department=UserDepartment.CEO.value, secure_code=faker.ssn(),
                                         status=UserStatuses.Admin)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(),
                            profile=profile)

        # result
        count = User.objects.all().count()
        print(f'Success! Inserted records: {count}')
