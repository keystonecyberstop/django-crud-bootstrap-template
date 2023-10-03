from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=128, unique=True)
    address = models.TextField()
    designation = models.CharField(max_length=128)

    def __str__(self):
        return self.name