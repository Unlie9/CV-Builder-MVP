from django.contrib import admin
from apps.audit.models import RequestLog

@admin.register(RequestLog)
class AuditAdmin(admin.ModelAdmin):
    list_display = (
      "user",
      "http_method", 
      "status", 
      "path",
      "ip_address",
      "duration", 
      "created_at", 
      "updated_at"
    )
    list_filter = ("user", "created_at")
    search_fields = ("status", "http_method")
