from django.contrib.auth.models import User
from rest_framework import serializers

from clear_cut.api.serializers import ClearCutConfigSerializer
from clear_cut.models import ClearCutConfig
from media_management import constants
from media_management.models import MediaItem, MediaImage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )


class MediaItemReadOnlySerializer(serializers.ModelSerializer):
    media_type_name = serializers.SerializerMethodField()

    clear_cut_config = ClearCutConfigSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = MediaItem
        fields = (
            'id',
            'description',
            'label',
            'media_type_name',
            'clear_cut_config',
            'user',
        )
        depth = 1
    
    def get_media_type_name(self, obj):
        for element in constants.ALLOWED_MEDIA_TYPES:
            if element[0] == obj.media_type:
                return element[1]


class MediaImagesReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ('media_url_original', 'media_url_clear_cut', )
        depth = 1


class MediaItemSerializer(serializers.ModelSerializer):
    clear_cut_image = MediaImagesReadOnlySerializer(read_only=True, many=True)
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


class MediaImageSerializer(serializers.ModelSerializer):
    media_item = MediaItemReadOnlySerializer(read_only=True, many=False)

    class Meta:
        model = MediaImage
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        media_item_pk = self.context['view'].kwargs['pk']
        validated_data['media_item'] = MediaItem.objects.get(pk=media_item_pk)
        return super(MediaImageSerializer, self).create(validated_data)
