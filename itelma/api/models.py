from django.db import models


def original_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f"{instance.name}/original.{extension}"


class Original(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    last_opened = models.DateTimeField()
    file = models.ImageField(upload_to=original_upload_path)


def preview_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f"{instance.name}/preview.{extension}"


class Preview(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    file = models.ImageField(upload_to=preview_upload_path)
    original = models.ForeignKey(Original, on_delete=models.CASCADE)


def tile_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f"{instance.name}/scale_{instance.scale}/t_{instance.x}_{instance.y}.{extension}"


class ScaleTile(models.Model):
    scale = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    original = models.ForeignKey(Original, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=tile_upload_path)
