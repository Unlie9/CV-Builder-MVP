
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.cv.views import (
  IndexView, 
  CvDetailView,
  CvViewSet
)

app_name = 'cv'

router = DefaultRouter()
router.register('cv', CvViewSet, basename='cv')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', IndexView.as_view(), name='index'),
    path('cv-detail/<uuid:pk>/', CvDetailView.as_view(), name='cv-detail'),
]



