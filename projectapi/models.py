from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)