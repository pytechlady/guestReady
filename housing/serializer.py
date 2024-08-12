from rest_framework import serializers
from .models import Flat, Booking
from django.db.models import Q


class BookingSerializer(serializers.ModelSerializer):
    flat_name = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['flat', 'previous_booking_id']
        
    def validate(self, attrs):
        flat_name = attrs.get('flat_name')
        check_in = attrs.get('checkin')
        check_out = attrs.get('checkout')
    
        check_booking = Booking.objects.filter(flat__name=flat_name)
        if check_booking.filter(Q(checkin=check_in) & Q(checkout=check_out)):
            raise serializers.ValidationError({"flat":
                "Flat not available for these dates"})
        
        return attrs
    
    # To order the bookings according to the flat id i.e, it will list all the bookings from one id before the next id
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['flatname'] = instance.flat.name
        data['flat_id'] = instance.flat.id
        return data
        
    def create(self, validated_data):
        try:
            flat_obj, created = Flat.objects.get_or_create(name=validated_data.get('flat_name'))
            if Booking.objects.exists():
                booking_id = Booking.objects.last().id
            if Booking.objects.filter(flat__name=validated_data.get('flat_name')).exists():
                previous_booking_id = booking_id
            else:
                previous_booking_id = '-'
            new_booking = Booking.objects.create(flat=flat_obj, checkin=validated_data.get('checkin'), checkout=validated_data.get('checkout'), previous_booking_id = previous_booking_id)
            
            return new_booking
        except Exception as e:
            print(f"Create error, {e}")
            

        