"""Project1TaskOnlineCart1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Customers.urls')),
    path('', views.showIndex, name='home'),
    path('Admin_log_in/', views.Admin_log_in, name='Admin_log_in'),
    path('Stocker_page/', views.Stocker_page, name='Stocker_page'),
    path('Dispacher_page/', views.Dispacher_page, name='Dispacher_page'),
    path('Add_Stocker/', views.Add_Stocker, name='Add_Stocker'),
    path('Display_Stockers/', views.Display_Stockers, name='Display_Stockers'),
    path('Dispacher_registers/', views.Dispacher_registers, name='Dispacher_registers'),
    path('Display_Dispachers/', views.Display_Dispachers, name='Display_Dispachers'),
    path('delete_Dispacher/', views.delete_Dispacher, name='delete_Dispacher'),
    path('Delete_Stocker/', views.Delete_Stocker, name='Delete_Stocker'),
    path('Stocker_login/', views.Stocker_login, name='Stocker_login'),
    path('Stocker_log_test/', views.Stocker_log_test, name='Stocker_log_test'),
    path('Dispatcher_login/', views.Dispatcher_login, name='Dispatcher_login'),
    path('Dispatchar_login_success/', views.Dispatchar_login_success, name='Dispatchar_login_success'),
    path('Stocker_Add_Products/', views.Stocker_Add_Products, name='Stocker_Add_Products'),
    path('Stocker_Add_Products_save/', views.Stocker_Add_Products_save, name='Stocker_Add_Products_save'),
    path('Show_All_Products/', views.Show_All_Products, name='Show_All_Products'),
    path('Stocker_Change_Password/', views.Stocker_Change_Password, name='Stocker_Change_Password'),
    path('Delete_Product/', views.Delete_Product, name='Delete_Product'),
    path('Delete_Search_idnumber/', views.Delete_Search_idnumber, name='Delete_Search_idnumber'),
    path('Deleted_Product/', views.Deleted_Product, name='Deleted_Product'),
    path('Stacker_Changed_Password/', views.Stacker_Changed_Password, name='Stacker_Changed_Password'),
    path('Dispacher_Add_Products/', views.Dispacher_Add_Products, name='Dispacher_Add_Products'),
    path('Dispacher_Add_Products_sucess/', views.Dispacher_Add_Products_sucess, name='Dispacher_Add_Products_sucess'),
]
