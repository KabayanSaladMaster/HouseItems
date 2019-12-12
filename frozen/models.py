from django.db import models

# Create your models here.
class FrozenItem(models.Model):
    item_name = models.CharField(max_length=50)
    slug = models.SlugField()
    brand = models.CharField(default='N/A', max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=1000,decimal_places=3)


    def __str__(self):
        return self.item_name