from django.shortcuts import render
from django.views import generic

from apps.cv.models import CV

class IndexView(generic.ListView):
  queryset = CV.objects.select_related('header').prefetch_related('body_sections').all()
  template_name = 'index/index.html'      

class CvDetailView(generic.DetailView):
  model = CV
  template_name = 'cv_detail/detail.html'
