from django.urls import path
from . import views

app_name = 'articlericot'

urlpatterns = [
    path('', views.index, name='index'),
]
