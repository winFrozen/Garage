from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='car/img')

    def __str__(self):
        return self.name

class Latest(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='car/img1')

    def __str__(self):
        return self.name