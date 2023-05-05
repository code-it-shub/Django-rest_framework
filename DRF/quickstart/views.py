from django.shortcuts import render
# from django.http import JsonResponse,HttpResponse
from .models import Employees
from .serializers import EmployeesSerializer,UsersSerializer
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @csrf_exempt
@api_view(['GET' , 'POST'])
def employeesAPI(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializedEmployees = EmployeesSerializer(employees, many=True)
        return Response(serializedEmployees.data)
    elif request.method =='POST':
        # parsed = JSONParser().parse(request)
        # serializedEmployees = EmployeesSerializer(data = parsed)
        serializedEmployees = EmployeesSerializer(data = request.data)
        if serializedEmployees.is_valid():
            serializedEmployees.save()
            return Response(serializedEmployees.data) 
        else:
            return Response(serializedEmployees.errors)

# @csrf_exempt 
@api_view(['GET' , 'POST'])     
def usersAPI(request):
    if request.method == 'GET':
        users=User.objects.all()
        serializedUser = UsersSerializer(users, many=True)
        # return JsonResponse(serializedUser.data , safe=False)
        return Response (serializedUser.data)
    elif request.method == 'POST':
        # parsed = JSONParser().parse(request)
        # serializedUser = UsersSerializer(data=parsed)
        serializedUser = UsersSerializer(data=request.data)   # AFTER USING APIVIEW DECORATOR WE DON'T NEED TO PARSE THE DATA USING JSONParser
        if serializedUser.is_valid():
            serializedUser.save()
            # return JsonResponse (serializedUser.data , safe=False)
            return Response (serializedUser.data)
        else:
            # return JsonResponse(serializedUser.errors, safe=False)
            return Response (serializedUser.errors)


# @csrf_exempt
@api_view(['GET','PUT','DELETE'])  
def EmployeeDetailView(request, pk): 
    try:
        employee=Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=404)

    if request.method == 'GET':
        serialized = EmployeesSerializer(employee)
        # return JsonResponse(serialized.data,safe=False)
        return Response(serialized.data)
    elif request.method == 'PUT':
        # parsed = JSONParser().parse(request)
        # serializedUser = EmployeesSerializer(employee,data=parsed)
        serializedUser = EmployeesSerializer(employee,data=request.data)
        if serializedUser.is_valid():
            serializedUser.save()
            # return JsonResponse (serializedUser.data , safe=False)
            return Response (serializedUser.data)
        else:
            # return JsonResponse(serializedUser.errors, safe=False)
            return Response (serializedUser.errors)
    elif request.method == 'DELETE':
        employee.delete()
        # return HttpResponse(status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_204_NO_CONTENT)
