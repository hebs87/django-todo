from django.test import TestCase
from .models import Item

# Create your tests here.
# CREATE CLASS THAT INHERITS TestCase
class TestItemModel(TestCase):


    # Tests if 'done' property not selected when creating item, value = False
    def test_done_defaults_to_False(self):
        # Create instance of the item model
        item = Item(name="Create a Test")
        item.save()
        # Checks item name is "Create a Test"
        self.assertEqual(item.name, "Create a Test")
        # Checks item done value = False
        self.assertFalse(item.done)


    # Tests we can create item with value of done = True
    def test_can_create_an_item_with_a_name_and_status(self):
        # Create instance of the item model and set done to True
        item = Item(name="Create a Test", done=True)
        item.save()
        # Checks item name is "Create a Test"
        self.assertEqual(item.name, "Create a Test")
        # Checks item done value = True
        self.assertTrue(item.done)


    # We want to test that the model instance is the same name and the one
    # we give the object, for the returned values in the admin site
    # Tests the def __str__(self) function in models.py
    def test_item_as_a_string(self):
        # We create an item
        item = Item(name="Create a Test")
        # Ensures the string in the admin site is the same as the item name
        self.assertEqual("Create a Test", str(item))
