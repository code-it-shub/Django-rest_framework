from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('instructors/',views.InstructorListView.as_view()),
    path('courses/',views.CoursesListView.as_view())
]
