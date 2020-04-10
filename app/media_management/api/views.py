from rest_framework import generics

from media_management.models import MediaItem


class ListCreateMediaItemView(generics.ListCreateAPIView):
    queryset = MediaItem.objects.all()
    