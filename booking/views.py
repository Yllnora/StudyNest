
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
from django.shortcuts import render

def booking_home(request):
    return render(request, 'booking/booking_home.html', {})
