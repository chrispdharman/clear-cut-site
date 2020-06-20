from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.template import loader

from clear_cut.models import ClearCutConfig


class CustomLoginView(LoginView):
    extra_context = {
        'splash_image_initial': 'https://clear-cut.s3.eu-west-2.amazonaws.com/results/test/manual-clear-cut-logo/0001_size_reduced_image.png',
        'splash_image_final': 'https://clear-cut.s3.eu-west-2.amazonaws.com/results/test/manual-clear-cut-logo/0008_edge_masked_image.png',
    }


def index(request):
    clear_cut_configs = ClearCutConfig.objects.order_by('-is_default')
    template = loader.get_template('configurator/index.html')
    context = {
        'clear_cut_configs': clear_cut_configs,
    }
    return HttpResponse(template.render(context, request))
