from django.urls import include, path

from media_management import views


urlpatterns = [
    path('api/', include('media_management.api.urls')),
    path('upload/', views.uploader, name='item_uploader'),
    path('', views.index, name='index'),
]