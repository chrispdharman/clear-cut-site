from rest_framework import generics, views
from rest_framework.response import Response

from media_management.api.serializers import MediaItemSerializer, MediaImageSerializer
from media_management.models import MediaItem, MediaImage
from media_management.services.clear_cut_processor import ClearCutProcessorService


class ClearCutAPI(views.APIView):
    _clear_cut_service = None

    @property
    def clear_cut_service(self):
        if not self._clear_cut_service:
            self._clear_cut_service = ClearCutProcessorService()
        
        return self._clear_cut_service

    def post(self, request, *args, **kwargs):
        # Receive a request and response accordingly
        self.clear_cut_service.process_image(request.data['image'])

        return Response(data='Successfully processed and stored media.')


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
    