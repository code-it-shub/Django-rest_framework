from django.shortcuts import render
from rest_framework import generics
from .serializers import serializedInstructor, serializedCourse
from .models import Instructor,Course

# Create your views here.


class InstructorListView(generics.ListCreateAPIView):
    serializer_class=serializedInstructor
    queryset= Instructor.objects.all()

class CoursesListView(generics.ListCreateAPIView):
    serializer_class = serializedCourse
    queryset = Course.objects.all()

