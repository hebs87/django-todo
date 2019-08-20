from django.contrib import admin
# Import the Item class from models.py
from .models import Item

# Register your models here.
# Register the Item table in the admin site
admin.site.register(Item)