# from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import AnonymousUser
# Create your tests here.
class FlightTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    def test_flight_list_as_non_authenticated_user(self):
        request = self.factory.get('/flight/flights/')
        request.user = AnonymousUser()