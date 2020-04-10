from django.urls import include, path

from media_management.api.views import (
    ListCreateMediaItemView,
)


urlpatterns = [
    path('media-items/', ListCreateMediaItemView.as_view(), name='list_create_media'),
]