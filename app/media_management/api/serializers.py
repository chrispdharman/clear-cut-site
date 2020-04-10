from rest_framework import serializers

from media_management.models import MediaItem


class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = '__all__'
    