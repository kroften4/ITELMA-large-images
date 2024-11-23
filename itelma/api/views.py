from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-last_opened')
    serializer_class = ImageSerializer
