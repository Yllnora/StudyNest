from django.contrib import admin
from django.urls import path, include
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservations.urls')),  # Home, Login, Registrierung
    path('booking/', include('booking.urls')),  # Buchungsfunktionen
]