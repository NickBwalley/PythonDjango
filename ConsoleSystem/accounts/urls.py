from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name = "login"),
    path('register/', views.register_page, name = "register"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    
    path('create_order/<str:pk>', views.create_order, name="create_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
]