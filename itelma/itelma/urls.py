from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'list', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('previews/<str:img_name>/', views.get_preview)
]
