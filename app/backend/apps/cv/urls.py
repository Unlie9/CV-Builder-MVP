from django.urls import path

from apps.cv.views import index


urlpatterns = [
    path('index/', index, name='index'),
]
