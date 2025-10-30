from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.CharField(max_length=255, blank=True, null=True)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking-{self.id}'

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
