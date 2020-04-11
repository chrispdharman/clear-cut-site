from django.contrib.auth.models import User
from rest_framework import serializers

from media_management import constants
from media_management.models import MediaItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )


class MediaItemSerializer(serializers.ModelSerializer):
    media_type = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = MediaItem
        fields = '__all__'
        depth = 1

    def get_media_type(self, obj):
        for element in constants.ALLOWED_MEDIA_TYPES:
            if element[0] == obj.media_type:
                return element[1]
    