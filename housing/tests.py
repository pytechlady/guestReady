from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.

class TestBooking(APITestCase):
    
    def setUp(self):
        self.url = reverse('booking')
        self.booking_data = {
            "flat_name" :'flat-1',
            "checkin" : '2024-08-20',
            "checkout" : '2024-08-22'
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_create_booking_success(self):
        res = self.client.post(self.url, self.booking_data, format='json')
        self.assertEqual(res.status_code, 201)
        self.assertIsNotNone(res.data)
        self.assertEqual(res.data['status'], 'success')
        self.assertEqual(res.data['message'], "Booking successfully created")
        
    def test_create_flat(self):
        res = self.client.post(self.url, self.booking_data, format='json')
        self.assertEqual(res.status_code, 201)
        self.assertIsNotNone(res.data['data']['flat'])
        
    def test_get_bookings(self):
        # booking = self.client.post(self.url, self.booking_data, format='json')
        res = self.client.get(self.url)
        self.assertEquals(res.status_code, 200)
        self.assertIsNotNone(res.data)
        
        
        

        
