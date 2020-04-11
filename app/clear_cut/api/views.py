from rest_framework import generics

from clear_cut.models import ClearCutConfig
from clear_cut.api.serializers import ClearCutConfigSerializer


class ListCreateClearCutConfigView(generics.ListCreateAPIView):
    queryset = ClearCutConfig.objects.all()
    serializer_class = ClearCutConfigSerializer

class RetrieveUpdateDestroyClearCutConfigView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClearCutConfig.objects.all()
    serializer_class = ClearCutConfigSerializer
    