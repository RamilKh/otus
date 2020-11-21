from django.test import TestCase
from app.models import User, Profile


class UserModelTestCase(TestCase):

    def setUp(self):
        profile = Profile.objects.create(department='HR', secure_code='009-ULQ-827', status=1)
        User.objects.create(first_name='James', last_name='Karter', email='james.karter@gmail.com', profile=profile)

        profile = Profile.objects.create(department='IT', secure_code='109-ULQ-828', status=5)
        User.objects.create(first_name='Mike', last_name='Hitch', email='mike.hith@gmail.com', profile=profile)

        profile = Profile.objects.create(department='CEO', secure_code='509-PLQ-127', status=5)
        User.objects.create(first_name='Kate', last_name='Monson', email='kate@gmail.com', profile=profile)

        profile = Profile.objects.create(department='IT', secure_code='009-ULQ-827', status=9)
        User.objects.create(first_name='Alex', last_name='Midlton', email='alex@gmail.com', profile=profile)

        profile = Profile.objects.create(department='СЕО', secure_code='728-ULQ-827', status=9)
        User.objects.create(first_name='Harry', last_name='Gordon', email='harry@gmail.com', profile=profile)

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
        Profile.objects.create(department='HR', secure_code='009-ULQ-827', status=1)
        Profile.objects.create(department='IT', secure_code='109-ULQ-828', status=5)
        Profile.objects.create(department='СЕО', secure_code='509-PLQ-127', status=5)
        Profile.objects.create(department='IT', secure_code='009-ULQ-827', status=9)
        Profile.objects.create(department='СЕО', secure_code='728-ULQ-827', status=9)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_get_department_count(self):
        self.assertEqual(Profile.get_department_count('СЕО'), 2)
        self.assertEqual(Profile.get_department_count('HR'), 1)
        self.assertEqual(Profile.get_department_count('IT'), 2)
