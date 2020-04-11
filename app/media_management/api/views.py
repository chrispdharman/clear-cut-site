from rest_framework import generics

from media_management.models import MediaItem
from media_management.api.serializers import MediaItemSerializer


class ListCreateMediaItemView(generics.ListCreateAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer

class RetrieveUpdateDestroyMediaItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
    