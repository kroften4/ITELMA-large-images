from rest_framework import serializers
from .models import Original


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Original
        fields = ['name', 'last_opened']
