
from django.db import transaction
from rest_framework import serializers

from apps.cv.models import (
  CV, 
  Header, 
  BodySection
)


class HeaderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Header
    fields = (
      'id',
      'full_name',
      'position',
      'linkedin_url'
    )


class BodySectionsSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(required=False)

  class Meta:
    model = BodySection
    fields = (
      'id',
      'name',
      'description'
    )


class CvSerializer(serializers.ModelSerializer):
  header = HeaderSerializer()
  body_sections = BodySectionsSerializer(many=True, required=False)

  class Meta:
    model = CV
    fields = (
      'id',
      'filename',
      'header',
      'body_sections'
    )

  @transaction.atomic()
  def create(self, validated_data):
    header_data = validated_data.pop('header')
    body_sections_data = validated_data.pop('body_sections', [])

    header = Header.objects.create(**header_data)
    cv = CV.objects.create(header=header, **validated_data)

    for body_section_data in body_sections_data:
      BodySection.objects.create(cv_id=cv.id, **body_section_data)

      return cv

  @transaction.atomic()
  def update(self, instance, validated_data):  
    header_data = validated_data.pop('header')
    body_sections_data = validated_data.pop('body_sections', [])
   
    if header_data:
      instance.header.update(**header_data)

    if body_sections_data:
      for body_section_data in body_sections_data:
          
          section_id = body_section_data.get('id', None)

          if section_id:
              BodySection.objects.filter(id=section_id, cv_id=instance.id).update(**body_section_data)
          else:
              BodySection.objects.create(cv_id=instance.id, **body_section_data)

    instance.update(**validated_data)
      
    return instance
