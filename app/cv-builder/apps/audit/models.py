from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth.models import User


class RequestLog(BaseModel):
  http_method = models.CharField(max_length=32)
  status = models.IntegerField(null=True)
  path = models.CharField(max_length=128)
  ip_address = models.CharField(max_length=128)
  duration = models.CharField(null=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  class Meta:
    verbose_name = 'Audit'
    verbose_name_plural = 'Audits'
    db_table = 'request_logs'

  def __str__(self) -> str:
    return f"{self.http_method} - {self.status}"


  

