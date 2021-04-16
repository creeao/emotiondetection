from django.db import models

# Create your models here.


class Upload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
