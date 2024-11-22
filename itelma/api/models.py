from django.db import models


class Image(models.Model):
    name = models.CharField(primary_key=True)
    last_called = models.DateTimeField()
