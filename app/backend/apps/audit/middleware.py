import time
from apps.audit.models import RequestLog
from django.http import HttpResponseServerError
from django.contrib.auth.models import User


class AuditLogsMiddleware:

  def __init__(self, get_response) -> None:
    self._get_response = get_response

  def __call__(self, request):
    start_time = time.time()
    
    request_log = RequestLog.objects.create(
      http_method=request.method,
      status=200,
      ip_address=self.get_client_ip(request),
      path=request.path,
      user_id=request.user.id
    )
    try:
        response = self._get_response(request)
        request_log.status = response.status_code
    except Exception:
        request_log.status = 500
        response = HttpResponseServerError("Internal Server Error")
        raise
    finally:
        request_log.duration = str(time.time() - start_time)
        request_log.save()

    return response
  
  def get_client_ip(self, request):
    ip = request.META.get('HTTP_X_REAL_IP') 
    if not ip:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

    return ip

