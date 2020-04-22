from django.urls import path, include
from . import views

app_name = 'target'

urlpatterns = [
    path('create_form/', views.create_target, name='create_form'),
]