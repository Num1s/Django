from django.db import models

# Create your models here.
class HouseModel(models.Model):
    title_name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.title_name