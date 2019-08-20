from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item # This is for passing the id in the edit function

# Create your tests here.
# CREATE TESTS TO ENSURE WE GO TO THE CORRECT URL AND TEMPLATE
# CREATE CLASS THAT INHERITS TestCase
class TestViews(TestCase):


    # Tests that we are directed to the homepage
    def test_get_home_page(self):
        # Built in helper function that fakes a request to the URL
        # Pass in argument of the URL (/ in this instance)
        # Store the output in page variable
        page = self.client.get("/")
        # Checks that status code of the URL is successful
        self.assertEqual(page.status_code, 200)
        # Checks that the page uses the correct template
        self.assertTemplateUsed(page, "todo_list.html")


    # Tests the add item page is successful and used the correct template
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")


    # Tests the edit item page is successful and used the correct template
    def test_edit_item_page(self):
        # Create instance of the item model to be passed into the edit URL
        item = Item(name="Create a Test")
        item.save()
        # We then pass the item id into the format method for the placholder
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")


    # Test that we get a 404 error if item doesn't exist on edit page
    def test_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        # Checks status code of page is 404
        self.assertEqual(page.status_code, 404)


    # Test that the post method creates an item
    def test_post_create_an_item(self):
        # Create a response and say it is equal to the POST request
        response = self.client.post("/add", {'name': "Create a Test"})
        # We want to retreive the same item
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)


    # Test that the POST method is working on the edit an item function
    def test_post_edit_an_item(self):
        # Create a new item, store it and store the id in a variable
        item = Item(name="Create a Test")
        item.save()
        id = item.id
        # Create a response, pass in the id and give it a differnt name
        response = self.client.post("/edit/{0}".format(id),
                                     {'name': "A different name"})
        # Retreive the same item
        item = get_object_or_404(Item, pk=id)
        # Asserts that our item name will be equal to the new name
        self.assertEqual("A different name", item.name)


    # Tests that the POST method is working on the toggle status function
    def test_toggle_status(self):
        # Create a new item, store it and store the id in a variable
        item = Item(name="Create a Test")
        item.save()
        id = item.id
        # No need to pass any strings in, as we're not changing the item value
        response = self.client.post("/toggle/{0}".format(id))
        # Retreive the same item
        item = get_object_or_404(Item, pk=id)
        # Asserts that our item done value will equal True
        # We created an item with a default value of False before,
        # so this will be toggled to True
        self.assertEqual(item.done, True)
