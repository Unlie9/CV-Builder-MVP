from django.shortcuts import render
from django.views import generic

from apps.cv.models import (
    CV,
    Header,
    BodySection
)

def index(request):
    
    return render(request, 'index.html', {})


class CvBase:
    model = CV

class IndexView(CV, generic.View):
  cv_queryset = CV.objects.all()
  template_name = 'index.html'    

  def get(self, request, *args, **kwargs):
     
    print(request.user)
  
    context = self.get_context_data()
    context['queryset'] = self.get_queryset()

    return render(request=request, template_name=self.template_name, context={})


  def get_queryset(self):
     return self.cv_queryset
  
  def get_context_data(self):
     context = {
        
     }

     return context
    
