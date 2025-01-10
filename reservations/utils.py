# utils.py
from .models import Reservation

def is_reservation_available(start_date, end_date):
    """
    Prüft, ob eine Reservierung im angegebenen Zeitraum möglich ist.
    """
    conflicting_reservations = Reservation.objects.filter(
        start_date__lt=end_date,  # Startdatum der bestehenden Reservierung ist vor dem Enddatum der neuen
        end_date__gt=start_date   # Enddatum der bestehenden Reservierung ist nach dem Startdatum der neuen
    )
    return not conflicting_reservations.exists()  # Verfügbar, wenn keine Konflikte existieren
