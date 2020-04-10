from django.urls import path

from clear_cut import views

urlpatterns = [
    path('', views.index, name='index'),
]