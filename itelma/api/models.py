from django.db import models
from pathlib import Path


class Image(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    last_opened = models.DateTimeField()
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)


class Preview(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    file = models.ImageField(upload_to=f"{name}/preview/")
    original = models.ForeignKey(Image, on_delete=models.CASCADE)


def upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f"{instance.name}/scale_{instance.scale}/t_{instance.x}_{instance.y}.{extension}"


class ScaleTile(models.Model):
    scale = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    original = models.ForeignKey(Image, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=upload_path)
