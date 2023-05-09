from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import book, Serializedbook

# Create your views here.

class bookViewSet(ModelViewSet):
    queryset = book.objects.all()
    serializer_class= Serializedbook
    