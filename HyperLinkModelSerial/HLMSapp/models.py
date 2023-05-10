from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name = models.CharField(max_length=30)
    rate = models.IntegerField(default=0)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='courses')
    price = models.IntegerField(default=0)
        
    