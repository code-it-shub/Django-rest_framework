from django.shortcuts import render
from rest_framework import generics
from .models import Instructor, Courses
from .serializers import SerializedInstructor, SerializedCourse

# Create your views here.

class InstructorView(generics.ListCreateAPIView):
    serializer_class = SerializedInstructor
    queryset = Instructor.objects.all()
    

class CourseView(generics.ListCreateAPIView):
    serializer_class = SerializedCourse
    queryset = Courses.objects.all()
    
class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializedInstructor
    queryset=Instructor.objects.all()

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializedCourse
    queryset = Courses.objects.all()
    

