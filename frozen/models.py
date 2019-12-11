from django.db import models

# Create your models here.
class FrozenItems(models.Model):
    item_name = models.CharField(max_length=50)
    slug = models.SlugField()
    brand = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name