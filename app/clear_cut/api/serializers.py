from rest_framework import serializers

from clear_cut.models import ClearCutConfig


class ClearCutConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearCutConfig
        fields = '__all__'
        depth = 1
    