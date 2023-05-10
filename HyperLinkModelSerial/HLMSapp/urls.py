from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('instructors/',views.InstructorView.as_view()),
    path('courses/',views.CourseView.as_view()),
    path('courses/<int:pk>', views.CourseDetailView.as_view(), name='courses-detail'),
    path('instructors/<int:pk>', views.InstructorDetailView.as_view(), name='instructor-detail')
]