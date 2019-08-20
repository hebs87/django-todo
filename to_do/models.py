from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)


    def __str__(self):
        '''
        This specifies which column values we want to return in the admin side
        '''
        return self.name