from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from .serializers import OriginalSerializer, PreviewSerializer, ScaleTileSerializer
from api.models import Original, Preview, ScaleTile
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Original.objects.all().order_by('-last_opened')
    serializer_class = OriginalSerializer


class ImgUploadAPIview(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        qs_serializer = OriginalSerializer(
            data={
                "name": request.data.get("name"),
                "file": request.FILES.get("file"),
            },
            context={"request": request},
        )
        if qs_serializer.is_valid():
            original = qs_serializer.save()

            # Create tiles
            for scale in range(3):
                for x in range(10):
                    for y in range(10):
                        # create tile file
                        # ...

                        tile = ScaleTile(x=x, y=y, original=original)

                        # add existing file path
                        tile.file.name = f"images/{original.name}/scale_{scale}/t_{x}_{y}.png"

                        tile.save()

            # Create preview
            preview = Preview(original=original)
            preview.file.name = f"images/{original.name}/preview.png"
            preview.save()

            return Response(
                {
                    "message": "Media uploaded successfully.",
                    "data": qs_serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": qs_serializer.errors, "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        qs = Original.objects.all()
        qs_serializer = OriginalSerializer(qs, many=True)
        return Response(qs_serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@renderer_classes((JSONRenderer, BrowsableAPIRenderer))
def get_preview(request, img_name):
    qs = Preview.objects.get(original__name=img_name)
    qs_serializer = PreviewSerializer(qs)
    return Response(qs_serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
@renderer_classes((JSONRenderer, BrowsableAPIRenderer))
def get_tile(request, img_name):
    x = request.GET.get('x')
    y = request.GET.get('y')
    qs = ScaleTile.objects.get(original__name=img_name, x=x, y=y)
    qs_serializer = ScaleTileSerializer(qs)
    return Response(qs_serializer.data, status=status.HTTP_200_OK)
