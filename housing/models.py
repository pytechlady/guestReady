from django.db import models

# Create your models here.


class Flat(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    previous_booking_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.checkin} - {self.checkout}"
