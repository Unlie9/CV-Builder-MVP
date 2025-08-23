from django.urls import path

from apps.cv.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
