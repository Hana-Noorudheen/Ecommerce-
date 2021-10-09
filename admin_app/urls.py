from django.urls import path
from . import views

urlpatterns = [

    path('adminlogin', views.adminlogin,name='adminlogin'),
    path('display', views.display,name='display'),
    path('logout', views.logout,name='logout'),

]