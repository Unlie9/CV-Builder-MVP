from django.shortcuts import render
from django.views import generic

from apps.cv.models import (
    CV,
    Header,
    BodySection
)

def index(request):
    
    return render(request, 'index.html', {})


# class CvBase:
#     model = CV

class IndexView(generic.View):
  cv_queryset = CV.objects.all()
  template_name = 'index/index.html'    

  def get(self, request, *args, **kwargs):
     
    print(request.user)
  
    context = self.get_context_data()

    for item in context['queryset']:
       print(item.header.__dict__)

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

