from django.test import TestCase
from app.models import User, Profile
import json


class UserViewTestCase(TestCase):

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

    def test_index_content(self):
        response = self.client.get('/')
        users = response.context['users']
        page = response.context['page']

        self.assertEqual(users.count(), 5)
        self.assertEqual(page, 'users')
        self.assertNotEqual(page, 'about')

    def test_detail_content(self):
        # get user from base
        user = User.objects.filter(email__exact='alex@gmail.com').first()

        # get user from view
        response = self.client.get(f'/detail/{user.id}/')
        user_page = response.context['user']
        page = response.context['page']

        # -
        self.assertEqual(user, user_page)
        self.assertEqual(page, 'users')

    def test_detail_not_found_content(self):
        response = self.client.get(f'/detail/90000/')

        self.assertEqual(response.status_code, 404)

    def test_create_content(self):
        # get user
        profile = Profile.objects.create(department='СЕО', secure_code='328-ULQ-127', status=9)
        user = User.objects.create(first_name='Harry1', last_name='Gordon1', email='harry1@gmail.com', profile=profile)

        # create
        response = self.client.post(f'/create/', data=user, content_type='json')
        self.assertEqual(response.status_code, 200)

        # get user from view
        response = self.client.get(f'/detail/{user.id}/')
        user_page = None
        if 'user' in response.context:
            user_page = response.context['user']

        # -
        self.assertEqual(user, user_page)
        self.assertEqual(response.status_code, 200)

    def test_about_content(self):
        response = self.client.get('/about/')
        page = response.context['page']

        self.assertEqual(page, 'about')
        self.assertNotEqual(page, 'contacts')


