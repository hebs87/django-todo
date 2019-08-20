from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
# Import Item from models.py
from .models import Item
# Import ItemForm class from forms.py
from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})


def create_an_item(request):
    # This is for the form submission
    if request.method=="POST":
        # Pass the form created in forms.py into the HTML template
        # We want what is in our POST form and also any files that are uploaded
        form = ItemForm(request.POST, request.FILES)
        # If the form input is valid then we want to save our form and redirect to toto_list
        if form.is_valid():
            form.save()

            return redirect(get_todo_list)
    # If form inout is invalid, we want to return a blank form
    else:
        form = ItemForm()
    # Pass in our form to the render request so it renders in the HTML page
    return render(request, "item_form.html", {'form': form})


def edit_an_item(request, id):
    # We want to get the form item by its primary key, or return an error
    item = get_object_or_404(Item, pk=id)
    if request.method=="POST":
        # Request the form and pass in instance of the item
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        # Create an empty form and pass in the instance of the item
        form = ItemForm(instance=item)
    
    return render(request, "item_form.html", {'form': form})


def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    # Flips the status of the item when the button is clicked
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)
