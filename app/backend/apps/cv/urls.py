from django.urls import path

from apps.cv.views import IndexView, CvDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cv-detail/<slug:pk>/', CvDetailView.as_view(), name='cv-detail'),
]

app_name = 'cv'

