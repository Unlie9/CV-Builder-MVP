import uuid

from django.db import models
from django.contrib.auth.models import User

from apps.base.models import BaseModel


class Header(BaseModel):

  '''
  
  Header model.

    related models:
      CV OneToOne Header
  
  '''
  
  # avatar = ""
  full_name = models.CharField(max_length=128, blank=True)
  position = models.CharField(max_length=128, blank=True)
  linkedin_url = models.URLField(max_length=255, blank=True)

  def __str__(self) -> str:
    return self.full_name
  
  class Meta:
    db_table = "header"


class CV(BaseModel):
  
  '''
  
  CV model.

    filename: name of the CV file. The user can enter it manually, or it will be generated automatically.
    header: header of cv page.
    user: authorized user owner of cv creation.
    
    related models:
      BodySection ManyToOne CV 
      
  '''
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  filename = models.CharField(max_length=48, default="", blank=True, verbose_name='File name')
  header = models.OneToOneField(Header, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Header', help_text='Header of cv page')
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cv_files')

  def __str__(self) -> str:
    return self.filename
  
  def __repr__(self) -> str:
    return f"Cv of user: {self.user}"
  
  class Meta:
    db_table = "cv"
    ordering = ['-updated_at']


class BodySection(BaseModel):

  '''
  
  Model BodySection.
    
    name: name of section.
    description: description of section.
  
  '''
  
  # icon = ''
  cv = models.ForeignKey(CV, on_delete=models.CASCADE, null=True, blank=True, related_name='body_sections')
  name = models.CharField(max_length=32)
  description = models.TextField()

  def __str__(self) -> str:
    return self.name
  
  class Meta:
    db_table = "body_section"
    ordering = ['created_at']
