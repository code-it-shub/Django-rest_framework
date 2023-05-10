from django.db import models
from rest_framework import serializers

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Course(models.Model):
    title= models.CharField(max_length=30)
    rating = models.IntegerField(default=0)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE, related_name='courses')
