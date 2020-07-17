from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home_page'),
    path('MiraclesApp/Registration.html', views.registration, name='Registration'),
]