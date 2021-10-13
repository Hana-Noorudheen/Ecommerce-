from django.urls import path
from . import views

urlpatterns = [

    path('adminlogin', views.adminlogin,name='adminlogin'),
    path('display', views.display,name='display'),
    path('logout', views.logout,name='logout'),
    path('delete/<username>/', views.delete,name='delete'),
    path('update/<username>/', views.update,name='update'),
    path('products',views.products,name='products'),
    path('productdelete/<id>/',views.productdelete,name='productdelete'),
    path('productupdate/<id>/',views.productupdate,name='productupdate'),
    path('addproduct', views.addproduct,name='addproduct'),

]