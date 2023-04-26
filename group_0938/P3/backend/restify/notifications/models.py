# Create your models here.
from django.db import models
from reservations.models import Reservation
from properties.models import Property
from django.conf import settings

class ReservationNotification(models.Model):
    # which user this notification is for
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE,null=True, default=None)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    content = models.CharField(max_length=120)

    state = models.CharField(max_length=2, choices=(("R", "Read"), ("U", "Unread"),), default="U")