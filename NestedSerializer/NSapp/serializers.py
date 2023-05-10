from . import models
from rest_framework import serializers

class serializedCourse(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'
class serializedInstructor(serializers.ModelSerializer):
    courses= serializedCourse(many=True, read_only = True)
    class Meta:
        model = models.Instructor
        fields = '__all__' 