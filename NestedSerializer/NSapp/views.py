from django.shortcuts import render
from rest_framework import generics
from .serializers import serializedInstructor, serializedCourse
from .models import Instructor,Course

# Create your views here.

class InstructorListView(generics.ListCreateAPIView):
    queryset= Instructor.objects.all()
    serializer_class=serializedInstructor
    

class CoursesListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = serializedCourse
   

