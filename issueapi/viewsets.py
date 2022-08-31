from rest_framework import viewsets

from . import models

from . import serializers

class IssueViewset(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer

