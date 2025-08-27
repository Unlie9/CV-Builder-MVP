from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from apps.cv.models import (
    CV, 
    Header, 
    BodySection
)

class CVViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.header = Header.objects.create(
            full_name="John Doe", 
            position="Developer", 
            linkedin_url="https://linkedin.com/in/johndoe"
        )
        self.cv = CV.objects.create(header=self.header)
        self.body_section = BodySection.objects.create(
            cv=self.cv, 
            name="Experience", 
            description="Worked at XYZ"
        )

    def test_index_view_status_code(self):
        response = self.client.get(reverse('cv:index')) 
        self.assertEqual(response.status_code, 200)

    def test_cv_detail_view_status_code(self):
        response = self.client.get(reverse('cv:cv-detail', args=[self.cv.pk]))
        self.assertEqual(response.status_code, 200)


class CvModelTests(TestCase):

    def setUp(self):
        self.header = Header.objects.create(
            full_name="John Doe",
            position="Developer",
            linkedin_url="https://linkedin.com/in/johndoe"
        )
        self.cv = CV.objects.create(header=self.header, filename="My CV")
        self.body_section = BodySection.objects.create(
            cv=self.cv,
            name="Experience",
            description="Worked at XYZ"
        )

    def test_cv_str(self):
        self.assertEqual(str(self.cv), "My CV")

    def test_header_str(self):
        self.assertEqual(str(self.header), "John Doe")

    def test_body_section_str(self):
        self.assertEqual(str(self.body_section), "Experience")


class CvApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.header = Header.objects.create(
            full_name="John Doe",
            position="Developer",
            linkedin_url="https://linkedin.com/in/johndoe"
        )
        self.cv = CV.objects.create(header=self.header, filename="My CV")
        self.body_section = BodySection.objects.create(
            cv=self.cv,
            name="Experience",
            description="Worked at XYZ"
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My CV")

    def test_cv_detail_view(self):
        response = self.client.get(reverse('cv-detail', args=[self.cv.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")


class CvApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.header_data = {
            "full_name": "Jane Doe",
            "position": "Designer",
            "linkedin_url": "https://linkedin.com/in/janedoe"
        }
        self.cv_data = {
            "filename": "CV Jane",
            "header": self.header_data,
            "body_sections": [
                {"name": "Experience", "description": "Worked at ABC"}
            ]
        }

    def test_create_cv_api(self):
        response = self.client.post("/api/v1/cv/", self.cv_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CV.objects.count(), 1)
        self.assertEqual(CV.objects.first().header.full_name, "Jane Doe")

    def test_list_cv_api(self):
        header = Header.objects.create(**self.header_data)
        CV.objects.create(header=header, filename="CV Jane")
        response = self.client.get("/api/v1/cv/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

