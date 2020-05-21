from faker import Factory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from .models import BirthDay
from .model_factory import BirthDayFactory

faker = Factory.create()

class BirthdayTestCase(APITestCase):

    def setUp(self):
        self.birthday = BirthDayFactory()
        self.url = '/api/v1/birthdays/'

        self.payload = [{
            'birthday' : faker.date(pattern='%d.%m.%Y'),
            'email' : faker.email(),
            'first_name' : faker.first_name(),
            'last_name' : faker.last_name()
        }]

    def test_birthday_api_success(self):
        response = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data'][0]['birthday'], self.payload[0]['birthday'])
        self.assertEqual(response.data['data'][0]['email'], self.payload[0]['email'])

    def test_invalid_email_address(self):
        self.payload[0].update({'email' : 'invaildmail@address'})
        response_should = ErrorDetail(string='Enter a valid email address.', code='invalid')

        response = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0]['email'][0], response_should)

    def test_invalid_date_format(self):
        self.payload[0].update({'birthday' : '01-01-2020'})

        response_should = ErrorDetail(
            string='Date has wrong format. Use one of these formats instead: DD.MM.YYYY.',
            code='invalid'
        )

        response = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0]['birthday'][0], response_should)


class LetterDigitTestCase(APITestCase):
    def test_letter_digit(self):
        url = '/api/v1/get-upper-lowercase-variation/a2B/'
        response = self.client.get(url)

        self.assertEqual(len(response.data['result']), 4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
