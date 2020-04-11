from django.urls import include, path

from clear_cut import views

urlpatterns = [
    path('api/', include('clear_cut.api.urls')),
    path('', views.index, name='index'),
]