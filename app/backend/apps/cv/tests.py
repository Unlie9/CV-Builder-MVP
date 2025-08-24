from django.test import TestCase, Client
from django.urls import reverse

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

