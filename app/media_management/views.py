from django.http import HttpResponse
from django.template import loader

from media_management.models import MediaItem


def index(request):
    recent_media_items = MediaItem.objects.order_by('-id')
    template = loader.get_template('dashboard/index.html')
    context = {
        'media_items': recent_media_items,
    }
    return HttpResponse(template.render(context, request))
