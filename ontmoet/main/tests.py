from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Question, Choice


########################################
# view
########################################

class IndexViewTests(TestCase):

    def test_shows_hello_world(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World')


########################################
# models
########################################


class QuestionModelTest(TestCase):

    def test_has_timestamps(self):
        q = Question()
        q.save()
        self.assertIsInstance(q.created_at, datetime)
        self.assertIsInstance(q.updated_at, datetime)

