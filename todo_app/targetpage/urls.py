from django.urls import path, include
from . import views

app_name = 'target'

urlpatterns = [
    path('add_form/', views.add_target, name='add_form'),
]