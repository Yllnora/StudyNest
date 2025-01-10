
from django.contrib.auth.models import User
from django.db import models

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    light_intensity = models.IntegerField(default=50)
    table_height = models.IntegerField(default=75)
    seat_count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
