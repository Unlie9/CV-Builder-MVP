from django.shortcuts import render
from django.views import generic

from apps.audit.models import RequestLog


class RequestLogListView(generic.ListView):
  model = RequestLog
  queryset = RequestLog.objects.all().order_by('-id')
  template_name = "request_logs/list.html"
  paginate_by = 11
