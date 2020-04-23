from django.urls import path, include
from . import views

app_name = 'target'

urlpatterns = [
    path('create_form/', views.create_target, name='create_form'),
    path('edit_form/<int:target_id>', views.edit_target, name='edit_target'),
    path('delete/', views.delete_target, name='delete_target'),
]