from rest_framework import viewsets

from .serializers import ImageSerializer
from api.models import Original


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Original.objects.all().order_by('-last_opened')
    serializer_class = ImageSerializer
