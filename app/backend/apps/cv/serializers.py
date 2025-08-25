
from rest_framework import serializers

from apps.cv.models import (
  CV, 
  Header, 
  BodySection
)


class CvListSerializer(serializers.ModelSerializer):

  class Meta:
    model = CV
    fields = (
      'id',
      'filename'
    )


class CvCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = CV
    fields = (
      'id',
      'filename',
      'header'
    )
