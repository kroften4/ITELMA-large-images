from django.db import models


class Image(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    last_opened = models.DateTimeField()
