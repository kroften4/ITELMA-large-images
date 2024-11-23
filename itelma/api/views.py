from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer
from pathlib import Path
from django.http import HttpResponse
from itelma.settings import IMAGES_DIR
from api.models import Image
from math import ceil


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-last_opened')
    serializer_class = ImageSerializer


def get_preview(request, img_name):
    preview_image = open(Path(IMAGES_DIR, img_name, "preview.png"), 'rb')
    return HttpResponse(preview_image, content_type="image/png")


def get_tile(request, img_name):
    scale = request.GET.get('scale')
    x = request.GET.get('x')
    y = request.GET.get('y')
    img = Image.objects.get(pk=img_name)
    width = img.width
    size_x = ceil(width / 2000)
    id = y * size_x + x
    preview_image = open(Path(IMAGES_DIR, img_name, f"tiles_{scale}", f"t{id}.png"), 'rb')
    return HttpResponse(preview_image, content_type="image/png")
