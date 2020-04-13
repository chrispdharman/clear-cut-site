from django.http import HttpResponse
from django.template import loader

from media_management.models import MediaItem
from media_management.api.serializers import MediaItemSerializer


def index(request):
    template = loader.get_template('dashboard/index.html')

    recent_media_items = MediaItem.objects.order_by('-id')
    serializer = MediaItemSerializer(recent_media_items[0])

    context = {
        'media_items': recent_media_items,
        'serializer': serializer,
    }
    return HttpResponse(template.render(context, request))
