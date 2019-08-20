from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
# CREATE CLASS THAT INHERITS TestCase
class TestToDoItemForm(TestCase):
    
    
    # Tests that we can create an item with just a name
    def test_can_create_an_item_with_just_a_name(self):
        # Create a new form - instantiate it from ItemForm
        # Create a dictionary with a key of name and vaule of 'Create Tests'
        form = ItemForm({'name': 'Create Tests'})
        # Test that the form is valid
        self.assertTrue(form.is_valid())


    # Tests that we can't crate an item without a name
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        # Test that the form is valid
        self.assertFalse(form.is_valid())
        # Test that the error message is displayed that field required
        # Asserts that there is an error in the name and the message value
        # This should be exact match to what is displayed, or test will fail
        self.assertEqual(form.errors['name'], [u'This field is required.'])