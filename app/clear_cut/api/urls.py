from django.urls import include, path

from clear_cut.api.views import (
    ListCreateClearCutConfigView,
    RetrieveUpdateDestroyClearCutConfigView,
)


urlpatterns = [
    path(
        'config-items/<int:pk>/',
        RetrieveUpdateDestroyClearCutConfigView.as_view(),
        name='retrieve_update_destroy_clear_cut_config',
    ),
    path(
        'config-items/',
        ListCreateClearCutConfigView.as_view(),
        name='list_create_clear_cut_config',
    ),
]