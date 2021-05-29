from django.db import models
from django.utils import timezone
from guest.models import Guest

# Create your models here.
class Confirmation(models.Model):
    ANSWER = (
        ('NA', 'No Asistire'),
        ('ON', 'Un Invitado'),
        ('TW', 'Dos invitados'),
    )
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="guestConfirmation")
    confirmed = models.CharField(max_length=10, choices=ANSWER)
    guestMessage = models.TextField(max_length=100)
    carConfirmation = models.BooleanField(default=False)
