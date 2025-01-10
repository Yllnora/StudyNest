from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home-Route
    path('login/', LoginView.as_view(template_name='reservations/login.html'), name='login'),  # Login-Route
    path('register/', views.register, name='register'),  # Register-Route
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard-Route
    path('configure/', views.configure, name='configure'),  # Configure-Route
    path('success/', views.reservation_success, name='reservation_success'),
    path('logout/', views.logout_view, name='logout')  # Logout mit Bestätigungsseite

]