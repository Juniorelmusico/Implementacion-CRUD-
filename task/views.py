from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import tasks
# Create your views here.
class taskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = tasks.objects.all()
