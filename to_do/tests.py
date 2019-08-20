from django.test import TestCase

# Create your tests here.

# THE CLASS MUST INHERIT TestCase
class TestDjango(TestCase):

    # TEST MUST START WITH 'test_'
    def test_is_this_thing_on(self):
        # Test that 1 is equal to 1
        self.assertEquals(1, 1)