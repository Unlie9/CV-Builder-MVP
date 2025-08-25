from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from apps.audit.models import RequestLog


class RequestLogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.log = RequestLog.objects.create(
            http_method="GET",
            status=200,
            path="/test/",
            ip_address="127.0.0.1",
            duration="0.123",
            user=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.log), "GET - 200")

    def test_fields(self):
        self.assertEqual(self.log.http_method, "GET")
        self.assertEqual(self.log.status, 200)
        self.assertEqual(self.log.path, "/test/")
        self.assertEqual(self.log.ip_address, "127.0.0.1")
        self.assertEqual(self.log.duration, "0.123")
        self.assertEqual(self.log.user, self.user)


class RequestLogListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        for i in range(15):
            RequestLog.objects.create(
                http_method="GET",
                status=200 + i,
                path=f"/test/{i}/",
                ip_address="127.0.0.1",
                duration="0.1",
                user=self.user
            )

    def test_view_status_code(self):
        url = reverse("audit:request_logs")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
