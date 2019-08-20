# WE DON'T NEED TO DO THIS, IT IS JUST AN EXAMPLE

from django.apps import apps
from django.test import TestCase
from .apps import ToDoConfig

class TestTodoConfig(TestCase):
    
    
    # Test the name is equal to the TodoConfig name
    def test_app(self):
        self.assertEqual("to_do", ToDoConfig.name)
        # Test we can get the app config from Django
        # self.assertEqual('to_do', apps.get_app_config('to_do'))