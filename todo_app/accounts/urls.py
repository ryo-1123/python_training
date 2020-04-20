from django.urls import path
from . import views

# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'accounts'

urlpatterns = [
    # ex: /accounts/signup/
    path('/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]