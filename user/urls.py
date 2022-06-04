from django.urls import path
from .views import UserLoginView, ShowIndexView, UserRegistrationView

# User's Urls
urlpatterns = [
    path('', ShowIndexView.as_view(), name='home_index'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', UserLoginView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),

] 