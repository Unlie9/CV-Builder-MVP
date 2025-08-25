from django.db import models


class Audit(models.Model):
  http_method = models.CharField(max_length=32)
  status = models.IntegerField()
  path = models.CharField(max_length=128)
  ip_address = models.CharField(max_length=128)
  duration = models.TimeField()


  

