from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home-Route
    path('login/', LoginView.as_view(template_name='reservations/login.html'), name='login'),  # Login-Route
    path('register/', views.register, name='register'),  # Register-Route
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard-Route
    path('configure/', views.configure, name='configure'),  # Configure-Route
    path('success/', views.reservation_success, name='reservation_success'),  # Erfolgsseite
    path('admin/reservations/', views.admin_reservations, name='admin_reservations'),  # Admin-Seite
    path('logout/', views.logout_view, name='logout'),  # Logout-Route
    path('reservations/', views.user_reservations, name='user_reservations'),  # Benutzerreservierungen
]
