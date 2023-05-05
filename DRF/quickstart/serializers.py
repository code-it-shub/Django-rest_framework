from .models import Employees
from django.contrib.auth.models import User
from rest_framework import serializers



# class EmployeesSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=30)
    # email = serializers.EmailField(max_length=30)
    # password = serializers.CharField(max_length=30)
    # phone = serializers.CharField(max_length=10)
     
    # def create(self, validated_data):
    #     return Employees.objects.create(**validated_data)
    # def update(self, employee , validated_data):
    #     updatedEmp = Employees(**validated_data)
    #     updatedEmp.id = employee.id
    #     updatedEmp.save()
    #     return updatedEmp

class EmployeesSerializer(serializers.ModelSerializer):  # we can use ModelSerializer
    class Meta:
        model = Employees
        fields = '__all__'


# class UsersSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=30)
#     email = serializers.EmailField(max_length=30)
#     password = serializers.CharField(max_length=30)

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'