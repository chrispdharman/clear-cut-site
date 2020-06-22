from django.http import HttpResponse
from django.template import loader

from media_management.api.serializers import MediaItemSerializer
from media_management.models import MediaItem


def index(request):
    template = loader.get_template('manage/index.html')

    recent_media_items = MediaItem.objects.order_by('-id')

    context = {
        'media_items': recent_media_items,
    }
    return HttpResponse(template.render(context, request))

def uploader(request):
    template = loader.get_template('manage/uploader.html')

    recent_media_items = MediaItem.objects.order_by('-id')
    serializer = MediaItemSerializer(recent_media_items[0])

    context = {
        'media_items': recent_media_items,
        'serializer': serializer,
    }
    return HttpResponse(template.render(context, request))
