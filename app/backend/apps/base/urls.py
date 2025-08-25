
from django.urls import path

from apps.base.views import (
  settings_view, 
)

app_name = 'base'

urlpatterns = [
    path('settings/', settings_view, name='settings'),
]
