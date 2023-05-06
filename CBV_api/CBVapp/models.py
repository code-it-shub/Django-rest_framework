from django.db import models
from rest_framework import serializers
# Create your models here.

class shop_items(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

# creating serializer here
class serializedItems(serializers.ModelSerializer):
    class Meta:
        model = shop_items
        fields = '__all__'




