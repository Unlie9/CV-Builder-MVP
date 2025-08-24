from django.shortcuts import render
from django.views import generic

from apps.cv.models import (
    CV,
    Header,
    BodySection
)

class IndexView(generic.ListView):
  cv_queryset = CV.objects.select_related('header').prefetch_related('body_sections').all()
  template_name = 'index/index.html'    

  def get(self, request, *args, **kwargs):
    context = self.get_context_data()
    return render(request=request, template_name=self.template_name, context=context)
  
  def get_context_data(self):
     context = {
        'queryset': self.get_queryset()
     }
     return context
    
  def get_queryset(self):
    return self.cv_queryset 
  

class CvDetailView(generic.DetailView):
  model = CV
  template_name = 'cv_detail/detail.html'

