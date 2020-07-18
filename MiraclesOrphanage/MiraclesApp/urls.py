from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home_page'),
    path('', views.login, name='login')
]