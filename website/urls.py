from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home view
    path('login/', views.home, name='login'),  # URL for the login view
    path('logout/', views.logout_user, name='logout'),  # URL for the logout view
    path('register/', views.register_user, name='register'),
]
