from rest_framework.views import APIView
from rest_framework import status, viewsets
from django.views import generic

from apps.cv.models import CV
from apps.cv.serializers import CvSerializer


class IndexView(generic.ListView):
  queryset = CV.objects.select_related('header').prefetch_related('body_sections').all()
  template_name = 'index/index.html'      


class CvDetailView(generic.DetailView):
  model = CV
  template_name = 'cv_detail/detail.html'


class CvViewSet(viewsets.ModelViewSet):
  model = CV
  queryset = CV.objects.select_related('header').prefetch_related('body_sections').all()
  serializer_class = CvSerializer
