
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.audit.views import (
  RequestLogListView, 
)

app_name = 'audit'

urlpatterns = [
    path('logs/', RequestLogListView.as_view(), name='request_logs'),
]
