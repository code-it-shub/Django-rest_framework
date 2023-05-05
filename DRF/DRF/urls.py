
from django.contrib import admin
from django.urls import path
from quickstart import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees', views.employeesAPI ),
    path('api/employees/<int:pk>', views.EmployeeDetailView ),
    path('api/users',views.usersAPI)
]
