from django.db import models

# create a Menu table
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)
    

class Logger(models.Model):
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    time_log = models.TimeField(help_text="Enter the exact time")

    def __str__(self):
        return self.last_name
