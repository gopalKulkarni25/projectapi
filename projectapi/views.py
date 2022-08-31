from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.decorators import api_view

from .models import Project

from .serializers import ProjectSerializer

@api_view(['GET'])
def getData(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getByTitle(request):
    title_req = request.GET.get('title')
    print(title_req)
    items = Project.objects.filter(title__icontains=title_req)
    serializer = ProjectSerializer(items, many=True)
    return Response(serializer.data)
