from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'list', views.ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('previews/<str:img_name>', views.get_preview),
    path('tiles/<str:img_name>', views.get_tile),
    path('upload/', views.ImgUploadAPIview.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
