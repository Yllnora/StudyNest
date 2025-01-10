from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Verbindung zum Benutzer
    name = models.CharField(max_length=100)  # Name der reservierenden Person
    email = models.EmailField()  # Kontakt-Email
    start_date = models.DateTimeField()  # Startdatum und -uhrzeit der Reservierung
    end_date = models.DateTimeField()  # Enddatum und -uhrzeit der Reservierung
    number_of_people = models.IntegerField()  # Anzahl der Personen (1–4)
    table_height = models.IntegerField(default=75)  # Optional: Tischhöhe
    light_intensity = models.IntegerField(default=50)  # Optional: Lichtintensität

    def __str__(self):
        return f"Reservation for {self.name} on {self.start_date} to {self.end_date}"
