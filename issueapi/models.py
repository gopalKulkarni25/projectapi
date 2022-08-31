from django.db import models

from projectapi.models import Project

# Create your models here.
# class Status(models.Model):
#     status = models.CharField(max_length=50)
#     id = models.IntegerField(primary_key=True)

class Issue(models.Model):
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    reporter = models.CharField(max_length=100)
    assignee = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

