from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # ex: /accounts/signup/
    # path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]