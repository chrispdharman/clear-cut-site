from django.http import HttpResponse
from django.template import loader

from clear_cut.models import ClearCutConfig


def index(request):
    clear_cut_configs = ClearCutConfig.objects.order_by('-is_default')
    template = loader.get_template('configurator/index.html')
    context = {
        'clear_cut_configs': clear_cut_configs,
    }
    return HttpResponse(template.render(context, request))
