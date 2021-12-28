from django.urls import path
from .import views


path('/increase',views.increase, name='increase'),
path('/increase',views.decrease, name='increase')

