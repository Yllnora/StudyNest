# utils.py
from .models import Reservation

def is_reservation_available(start_date, end_date):
    """
    Prüft, ob eine Reservierung im angegebenen Zeitraum möglich ist.
    """
    conflicting_reservations = Reservation.objects.filter(
        start_date__lt=end_date,  
        end_date__gt=start_date  
    )
    return not conflicting_reservations.exists()  
