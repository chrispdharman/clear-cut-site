from rest_framework import generics

from media_management.models import MediaItem, MediaImage
from media_management.api.serializers import MediaItemSerializer, MediaImageSerializer


class ListCreateMediaImageView(generics.ListCreateAPIView):
    queryset = MediaImage.objects.all()
    serializer_class = MediaImageSerializer

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        } 


class ListCreateMediaItemView(generics.ListCreateAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }  

class RetrieveUpdateDestroyMediaItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
    