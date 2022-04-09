from django.db import models

# Create your models here.

class Asset(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    code = models.TextField()
    exchange = models.TextField()
    download_datetime = models.TextField()
