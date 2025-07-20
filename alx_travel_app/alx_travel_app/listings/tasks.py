from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Booking


@shared_task
def send_booking_email(user_id, booking_id):
    user = User.objects.get(id=user_id)
    booking = Booking.objects.get(id=booking_id)
    send_mail(
        subject='Your Travel Booking Confirmation',
        message=f'Hi {user.name}, your booking to {booking.destination} is confirmed!',
        recipient_list=[user.email],
        from_email='thatoselepe53@gmail.com'
    )

