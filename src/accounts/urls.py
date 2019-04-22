from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('authentication/', views.Authentication.as_view(), name='authentication'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
