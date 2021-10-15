from django.urls import path
from . import views

urlpatterns = [
    
    path('login', views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('userdisplay', views.userdisplay,name='userdisplay'),
    path('logout', views.logout,name='logout'),
    path('product/<id>', views.product,name='product'),
    path('cart', views.cart,name='cart'),
    

]