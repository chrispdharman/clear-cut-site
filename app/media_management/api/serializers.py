from django.contrib.auth.models import User
from rest_framework import serializers

from clear_cut.api.serializers import ClearCutConfigSerializer
from clear_cut.models import ClearCutConfig
from media_management import constants
from media_management.models import MediaItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )


class MediaItemSerializer(serializers.ModelSerializer):
    media_type_name = serializers.SerializerMethodField()

    clear_cut_config = ClearCutConfigSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = MediaItem
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        validated_data['clear_cut_config'] = ClearCutConfig.objects.get(is_default=True)
        validated_data['user'] = self.context['request'].user
        return super(MediaItemSerializer, self).create(validated_data)

    def get_media_type_name(self, obj):
        for element in constants.ALLOWED_MEDIA_TYPES:
            if element[0] == obj.media_type:
                return element[1]
    