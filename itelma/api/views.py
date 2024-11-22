from images.models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-last_called')
    serializer_class = ImageSerializer
