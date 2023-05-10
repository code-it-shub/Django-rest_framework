from rest_framework import serializers
from .models import Instructor , Courses

class SerializedCourse(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Courses
        fields ='__all__'
    
class SerializedInstructor(serializers.HyperlinkedModelSerializer):
    courses=serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='courses-detail')
    class Meta:
        model = Instructor
        fields='__all__'
