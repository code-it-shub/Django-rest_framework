from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializers import SerializedCourse
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def courseDetail(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serialized = SerializedCourse(courses, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = SerializedCourse(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)

@api_view(['GET' , 'PUT' , 'DELETE'])
def courseDetailView(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = SerializedCourse(course)
        return Response(serialized.data)
    elif request.method =='PUT':
        serialized = SerializedCourse(course , data= request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status.HTTP_200_OK)

    
