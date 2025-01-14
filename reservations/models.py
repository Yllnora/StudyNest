from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True) 
    number_of_people = models.IntegerField()
    table_height = models.IntegerField(default=75)
    light_intensity = models.IntegerField(default=50)

    def __str__(self):
        return f"Reservation for {self.name} from {self.start_date} to {self.end_date}"
