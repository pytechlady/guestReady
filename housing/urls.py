from django.urls import path
from .views import *


urlpatterns = [
    path('bookingview', BookingView.as_view(), name='booking')
]
