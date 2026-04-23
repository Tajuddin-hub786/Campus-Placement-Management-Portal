from django.test import TestCase

from django.contrib.auth.models import User
class StudentRegistrationTestCase(TestCase):

    def test_student_registration(self):
        student = Student.objects.create(
            full_name="Test Student",
            email="test@student.com",
            roll_number="CSE001",
            department="CSE",
            year="2025",
            password="test@123",
            phone="9876543210",
            gender="Male"
        )

        # Assertions (checks)
        self.assertEqual(student.full_name, "Test Student")
        self.assertEqual(student.email, "test@student.com")
        self.assertEqual(student.roll_number, "CSE001")
        self.assertEqual(student.department, "CSE")
        self.assertEqual(student.year, "2025")
        self.assertEqual(student.password, "test@123")
        self.assertEqual(student.phone, "9876543210")
        self.assertEqual(student.gender, "Male")
from django.test import TestCase
from django.urls import reverse
from .models import Student
class StudentLoginViewTestCase(TestCase):

    def setUp(self):
        # Create a test student
        self.student = Student.objects.create(
            full_name="Login Student",
            email="login@student.com",
            roll_number="CSE002",
            department="CSE",
            year="2025",
            password="login@123",
            phone="9876543211",
            gender="Female"
        )
    def test_student_login_view(self):
        response = self.client.post(reverse('student_login'),
                                   {
                                       'roll_number': 'CSE002',
                                       'password': 'login@123'
                                   })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['roll_number'], 'CSE002')
        self.assertRedirects(response, reverse('student_dashboard'))
    def test_student_login_view_invalid_credentials(self):
        response = self.client.post(reverse('student_login'),
                                   {
                                       'roll_number': 'CSE002',
                                       'password': 'wrongpassword'
                                   })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid credentials")
class AdminLoginViewTestCase(TestCase):

    def setUp(self):
        # Create a test admin user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin@123',
        )

    def test_admin_login_view(self):
        response = self.client.post(reverse('admin_login'),
                                   {
                                       'username': 'admin',
                                       'password': 'admin@123'
                                   })
        self.assertEqual(response.status_code, 200)
    def test_admin_login_view_invalid_credentials(self):
        response = self.client.post(reverse('admin_login'),
                                   {
                                       'username': 'wrongadmin',
                                       'password': 'wrongpassword'
                                   })
        self.assertEqual(response.status_code, 200)
