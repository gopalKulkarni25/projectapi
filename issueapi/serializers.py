from dataclasses import field
from rest_framework import serializers

from .models import Issue

from projectapi.serializers import ProjectSerializer

class IssueSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Issue
        fields = '__all__'