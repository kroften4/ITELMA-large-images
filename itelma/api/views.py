from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer
from pathlib import Path
from django.http import HttpResponse
from itelma.settings import IMAGES_DIR


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-last_opened')
    serializer_class = ImageSerializer


def get_preview(request, img_name):
    preview_image = open(Path(IMAGES_DIR, img_name, "preview.png"), 'rb')
    return HttpResponse(preview_image, content_type="image/png")
