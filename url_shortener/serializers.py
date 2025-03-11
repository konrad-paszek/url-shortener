import hashlib

from rest_framework import serializers
from .models import ShortenedURL


class UrlSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    class Meta:
        model = ShortenedURL
        fields = [
            "original_url",
            "short_url"
        ]

    def get_short_url(self, obj):
        return obj.get_short_url()

    def create(self, validated_data):
        validated_data['short_hash'] = hashlib.md5(validated_data['original_url'].encode()).hexdigest()[:10]
        return super().create(validated_data)