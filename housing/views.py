from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import BookingSerializer
from .utils import convert_to_error_message, convert_to_success_message_with_data
from rest_framework.permissions import AllowAny
from .models import Booking

# Create your views here.

class BookingView(generics.GenericAPIView):
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    
    # Endpoint to create a new booking
    def post(self, request):
        try:
            serialized_input = self.serializer_class(data=request.data)
            if not serialized_input.is_valid():
                return Response(
                    convert_to_error_message(
                            serialized_input.errors
                        ), status=status.HTTP_400_BAD_REQUEST)
                
            serialized_input.save()
            return Response(
                convert_to_success_message_with_data(
                    "Booking successfully created", serialized_input.data
                ), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                convert_to_error_message(
                    str(e)
                ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Endpoint to fetch all bookings        
    def get(self, request):
        try:
            bookings = Booking.objects.select_related('flat').order_by('flat__id', 'checkin')
            bookings_data = self.serializer_class(bookings, many=True)
            return Response(
                convert_to_success_message_with_data(
                    "Booking fetched successfully", bookings_data.data
                ), status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    convert_to_error_message(
                            str(e)
                        ), status=status.HTTP_400_BAD_REQUEST)
            
            
    