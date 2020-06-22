from django.urls import include, path

from media_management.api.views import (
    ListCreateMediaImageView,
    ListCreateMediaItemView,
    RetrieveUpdateDestroyMediaItemView,
)


urlpatterns = [
    path(
        'media-items/<int:pk>/clear-cut-images/',
        ListCreateMediaImageView.as_view(),
        name='list_create_media',
    ),
    path(
        'media-items/<int:pk>/',
        RetrieveUpdateDestroyMediaItemView.as_view(),
        name='retrieve_update_destroy_media',
    ),
    path(
        'media-items/',
        ListCreateMediaItemView.as_view(),
        name='list_create_media',
    ),
]