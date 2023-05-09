from django.db import models
from rest_framework import serializers

# Create your models here.

class book(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    author_name = models.CharField(max_length=30)

class Serializedbook(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'


