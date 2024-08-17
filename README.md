### Booking System API

## Project Description
- This project is a Django-based API designed for managing flat bookings. The API allows users to create bookings for specific flats, with each booking linked to the previous booking for the same flat, if one exists. This allows for tracking the booking history of each flat, ensuring no overlaps, and maintaining a seamless booking experience.

## Features
- Flat Management: Automatically creates or retrieves a flat based on the name provided in the booking request.
- Booking Management: Handles the creation of new bookings, associating each with a flat and optionally linking it to the previous booking for the same flat.
- Booking History: Links each booking to the most recent prior booking for the same flat, if one exists.

## Prerequisites
Python 3.9+: Ensure that Python is installed on your machine.
Django: The web framework used for the API.

## Setup Instructions
- Clone the Repository: start by cloning the repository to your local machine.
- Install the required Python packages using pip: 'pip install -r requirements.txt'.
- Run the following commands to apply migrations and set up your database:
    - python manage.py makemigrations
    - python manage.py migrate
- Start the Django development server: 'python manage.py runserver'.
- The API will be accessible locally at 'http://127.0.0.1:8000/booking/bookingview'

## Usage
- To create a booking, make a POST request to /booking/bookingview with the following JSON body;
        {
            "flat_name": "Flat A",
            "checkin": "2024-08-20",
            "checkout": "2024-08-25"
        }   
