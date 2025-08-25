from django.shortcuts import render


def settings_view(request):
  template_name = 'settings/main.html'
  return render(request=request, template_name=template_name)
