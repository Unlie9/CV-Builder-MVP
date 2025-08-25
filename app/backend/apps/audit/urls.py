
from django.urls import path

from apps.audit.views import (
  RequestLogListView, 
)

app_name = 'audit'

urlpatterns = [
    path('logs/', RequestLogListView.as_view(), name='request_logs'),
]
