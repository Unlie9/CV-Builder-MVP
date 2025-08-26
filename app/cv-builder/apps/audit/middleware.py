import time
from apps.audit.models import RequestLog
from django.http import HttpResponseServerError


class AuditLogsMiddleware:

  def __init__(self, get_response) -> None:
    self._get_response = get_response

  def __call__(self, request):
    start_time = time.time()

    request_log = RequestLog.objects.create(
      http_method=request.method,
      status=200,
      ip_address=request.META.get('REMOTE_ADDR'),
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

