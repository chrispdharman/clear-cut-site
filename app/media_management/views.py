from django.http import HttpResponse
from django.template import loader

from media_management.api.serializers import MediaItemSerializer
from media_management.models import MediaItem


def _parse_context(additional_context=None):
    context = {
        'menu_logo': 'https://clear-cut.s3.eu-west-2.amazonaws.com/results/test/manual-clear-cut-logo/0008_edge_masked_image.png',
    }

    if additional_context:
        context.update(additional_context)

    return context


def index(request):
    template = loader.get_template('manage/index.html')

    recent_media_items = MediaItem.objects.order_by('-id')

    context = _parse_context({
        'media_items': recent_media_items,
    })
    return HttpResponse(template.render(context, request))


def uploader(request):
    template = loader.get_template('manage/uploader.html')

    context = _parse_context({
        'serializer': MediaItemSerializer(),
    })
    return HttpResponse(template.render(context, request))
