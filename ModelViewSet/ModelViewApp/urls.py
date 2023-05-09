from django.contrib import admin
from django.urls import path , include 
from rest_framework.routers  import DefaultRouter
from ModelViewApp import views

router = DefaultRouter()
router.register('books', views.bookViewSet , basename='book' )


urlpatterns = [
    path(' ', include(router.urls))
]