from rest_framework import serializers
from .models import Original, Preview, ScaleTile


class OriginalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Original
        fields = '__all__'


class PreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preview
        fields = '__all__'


class ScaleTileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScaleTile
        fields = '__all__'
