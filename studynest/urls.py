from django.contrib import admin
from django.urls import path, include
from reservations import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='reservations/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('reservations.urls')),  
]
