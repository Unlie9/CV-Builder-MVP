import time
from apps.audit.models import Audit
from django.http import HttpResponseServerError


class AuditLogsMiddleware:

  def __init__(self, get_response) -> None:
    self._get_response = get_response

  def __call__(self, request):

    start_time = time.time()

    audit = Audit.objects.create(
      http_method=request.method,
      ip_address=request.META.get('REMOTE_ADDR'),
      path=request.path,
      user_id=request.user.id
    )

    try:
        response = self._get_response(request)
        audit.status = response.status_code
    except Exception:
        audit.status = 500
        response = HttpResponseServerError("Internal Server Error")
        raise
    finally:
        audit.duration = str(time.time() - start_time)
        audit.save()

    return response

