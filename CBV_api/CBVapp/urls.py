from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('items',views.itemShow.as_view()),
    path('items/<int:pk>',views.itemDetail.as_view())

]
