from django.db import models

# Create your models here.

class People(models.Model):
    name=models.CharField(null=True,blank=True,max_length=10)
    job=models.CharField(null=True,blank=True,max_length=30)
    def __str__(self):
        return self.name
