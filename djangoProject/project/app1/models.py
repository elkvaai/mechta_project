from django.db import models


class Sales(models.Model):
    photo = models.ImageField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
