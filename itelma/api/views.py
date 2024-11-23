from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import OriginalSerializer, PreviewSerializer, ScaleTileSerializer
from api.models import Original, Preview, ScaleTile


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Original.objects.all().order_by('-last_opened')
    serializer_class = OriginalSerializer


# class ImgUploadAPIview(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def post(self, request):
#         qs_serializer = OriginalSerializer(
#             data={
#                 "name": request.data.get("name"),
#                 "image": request.FILES.get("media"),
#             },
#             context={"request": request},
#         )
#         if qs_serializer.is_valid():
#             qs_serializer.save()
#             return Response(
#                 {
#                     "message": "Media uploaded successfully.",
#                     "data": qs_serializer.data
#                 },
#                 status=status.HTTP_200_OK
#             )
#         else:
#             return Response(
#                 {"message": qs_serializer.errors, "data": None},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def get(self, request):
#         qs = Original.objects.all()
#         qs_serializer = OriginalSerializer(qs, many=True)
#         return Response(qs_serializer.data, status=status.HTTP_400_BAD_REQUEST)


def get_preview(request, img_name):
    qs = Preview.objects.get(name=img_name)
    qs_serializer = PreviewSerializer(qs)
    return Response(qs_serializer.data, status=status.HTTP_200_OK)


def get_tile(request, img_name):
    x = request.GET.get('x')
    y = request.GET.get('y')
    qs = ScaleTile.objects.get(name=img_name, x=x, y=y)
    qs_serializer = ScaleTileSerializer(qs)
    return Response(qs_serializer.data, status=status.HTTP_200_OK)
