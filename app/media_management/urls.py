from django.urls import include, path

from media_management import views


urlpatterns = [
    path('api/', include('media_management.api.urls')),
    path('', views.index, name='index'),
]