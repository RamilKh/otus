from django.test import TestCase
from app.models import User, Profile
from app.const.models import UserStatuses, UserDepartment
from faker import Faker


class UserModelTestCase(TestCase):

    def setUp(self):
        faker = Faker()

        profile = Profile.objects.create(department=UserDepartment.HR.value, secure_code=faker.ssn(), status=UserStatuses.User)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(), profile=profile)

        profile = Profile.objects.create(department=UserDepartment.IT.value, secure_code=faker.ssn(), status=UserStatuses.Developer)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(), profile=profile)

        profile = Profile.objects.create(department=UserDepartment.CEO.value, secure_code=faker.ssn(), status=UserStatuses.Developer)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(), profile=profile)

        profile = Profile.objects.create(department=UserDepartment.IT.value, secure_code=faker.ssn(), status=UserStatuses.Admin)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(), profile=profile)

        profile = Profile.objects.create(department=UserDepartment.CEO.value, secure_code=faker.ssn(), status=UserStatuses.Admin)
        User.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), email=faker.ascii_safe_email(), profile=profile)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_admins_count(self):
        self.assertEqual(User.get_admins_count(), 2)

    def test_developers_count(self):
        self.assertEqual(User.get_developers_count(), 2)

    def test_users_count(self):
        self.assertEqual(User.get_users_count(), 1)


class ProfileModelTestCase(TestCase):

    def setUp(self):
        faker = Faker()

        Profile.objects.create(department=UserDepartment.HR.value, secure_code=faker.ssn(),  status=UserStatuses.User)
        Profile.objects.create(department=UserDepartment.IT.value, secure_code=faker.ssn(),  status=UserStatuses.Developer)
        Profile.objects.create(department=UserDepartment.IT.value, secure_code=faker.ssn(), status=UserStatuses.Admin)
        Profile.objects.create(department=UserDepartment.CEO.value, secure_code=faker.ssn(), status=UserStatuses.Developer)
        Profile.objects.create(department=UserDepartment.CEO.value, secure_code=faker.ssn(), status=UserStatuses.Admin)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_get_department_count(self):
        self.assertEqual(Profile.get_department_count(UserDepartment.CEO.value), 2)
        self.assertEqual(Profile.get_department_count(UserDepartment.HR.value), 1)
        self.assertEqual(Profile.get_department_count(UserDepartment.IT.value), 2)
