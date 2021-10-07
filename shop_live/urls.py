from django.urls import path
from . import views

urlpatterns = [
    
    path('login', views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('display', views.display,name='display'),
    path('adminlogin', views.admin,name='admin'),

]