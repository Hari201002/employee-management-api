from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Employee
from rest_framework import status

class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin123'
        )
        token_resp = self.client.post('/api/token/', {
            'username': 'admin',
            'password': 'admin123'
        })
        self.token = token_resp.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )

    def test_create_employee(self):
        resp = self.client.post('/api/employees/', {
            "name": "Alice",
            "email": "alice@test.com",
            "department": "HR",
            "role": "Manager"
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_duplicate_email(self):
        Employee.objects.create(
            name="Bob", email="bob@test.com"
        )
        resp = self.client.post('/api/employees/', {
            "name": "Bob2",
            "email": "bob@test.com"
        })
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_employee_404(self):
        resp = self.client.get('/api/employees/999/')
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_employee(self):
        emp = Employee.objects.create(
            name="Del",
            email="del@test.com"
        )
        resp = self.client.delete(f'/api/employees/{emp.id}/')
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

