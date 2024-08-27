"""
URL configuration for EMP_ADMIN_LOGIN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Admin_Login.views import Admin_Login, logout_ad
from Employee_Login.views import Employee_Action
from Landing_EMP.views import employee_list
from Emp_Specific.views import employee_listfor1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Employee Login/',Employee_Action),
    path('Admin Login/',Admin_Login),
    path('employees/', employee_list),
    path('empfor1/<int:EmployeeID>/',employee_listfor1),
    path('logout',logout_ad),
]
