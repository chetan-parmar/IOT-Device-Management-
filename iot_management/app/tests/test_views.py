from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from app.models import Device

class UserRegistrationViewTest(APITestCase):
    def test_user_registration(self):
        url = reverse('user-registration')
        data = {'username': 'test_user', 'password': 'test_password', 'role': 'LEV_OPERATOR'}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        
        user = get_user_model().objects.get(username='test_user')
        self.assertTrue(user.check_password('test_password'))

class DeviceViewSetTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_create_device(self):
        url = '/app/devices/'
        data = {'name': 'Test Device', 'description': 'Test Description', 'telemetry_data': {'key': 'value'}}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.objects.count(), 1)
        self.assertEqual(Device.objects.first().name, 'Test Device')

    def test_list_devices(self):
        url = '/app/devices/'
        Device.objects.create(name='Device 1', description='Description 1')
        Device.objects.create(name='Device 2', description='Description 2')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
