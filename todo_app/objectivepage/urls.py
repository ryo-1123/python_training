from django.urls import path, include
from . import views

app_name = 'objective'

urlpatterns = [
    path('add_form/', views.add_object, name='add_form'),
    path('edit_form/<int:object_id>', views.edit_object, name='edit_object'),
]