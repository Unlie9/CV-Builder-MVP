from django.db import models



class BaseModel(models.Model):

  '''

  Base model that using for additional information about objects.

    is_active: Shows whether the object is still relevant instead of being deleted.
    created_at: Shows when the object was delete.
    updated_at: Shows when the object was updated.

  '''
  
  is_active = models.BooleanField(default=True, verbose_name='IsActive', help_text='Shows whether the object is still relevant')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 

  class Meta:
    abstract = True
    ordering = '-created_at'

  def update(self, **kwargs):
    for attr, value in kwargs.items():
        setattr(self, attr, value)
    self.save()

