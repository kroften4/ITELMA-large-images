from django.db import models


class Image(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    last_opened = models.DateTimeField()
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
