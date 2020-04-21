from django.test import TestCase
from django.urls import reverse
from .models import *


class IndexPageTestCase(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)


class DetailPageTestCase(TestCase):

    def setUp(self):
        impossible = Travel.objects.create(destination="Lourdes", price=500, picture = "..")
        self.travel = Travel.objects.get(destination="Lourdes")

    def test_detail_page_returns_200(self):
        travel_id = self.travel.id 
        response = self.client.get(reverse('detail', args=(travel_id,)))
        self.assertEqual(response.status_code, 200)


    def test_detail_page_returns_404(self):
        travel_id = self.travel.id +1
        response = self.client.get(reverse('detail', args=(travel_id,)))
        self.assertEqual(response.status_code, 404)

class BookingPageTestCase(TestCase):

    def setUp(self):
        Contact.objects.create(name="jean", email="jean@free.fr")
        Travel.objects.create(destination="Lourdes", price=500, picture = "..")
        self.travel = Travel.objects.get(destination="Lourdes")
        self.contact = Contact.objects.get(name="jean")

    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()
        travel_id = self.travel.id
        name = self.contact.name
        email = self.contact.email
        reponse = self.client.post(reverse('reservation', args=(travel_id,)), 
        {
            'name' : name,
            'email' : email
        })
        new_bookings = Booking.objects.count()
        self.assertEqual(new_bookings, old_bookings +1)

class ContactPageTestCase(TestCase):
    

    def test_new_contact_is_registered(self):
        old_contacts = Contact.objects.count()
        reponse = self.client.post(reverse('contact'), 
        {
            'name' : "jean",
            'email' : "jean@free.fr",
            'message' : "hello"
        })
        new_contacts = Contact.objects.count()
        self.assertEqual(new_contacts, old_contacts +1)