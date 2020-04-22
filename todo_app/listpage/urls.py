from django.urls import path, include
from . import views

app_name = 'list'

urlpatterns = [
    path('display_list/', views.display_list, name='display_list'),
]