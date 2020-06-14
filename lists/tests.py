from django.test import TestCase
from django.urls import resolve
from lists.views import home_page 
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows),
            "New to-do did not appear in table"
        )
                                

