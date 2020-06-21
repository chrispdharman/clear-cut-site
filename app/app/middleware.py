import re
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

EXEMPT_URLS = [settings.LOGOUT_REDIRECT_URL.lstrip('/')]


class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemption urls can be specified in EXEMPT_URLS.
    See https://stackoverflow.com/questions/3214589/django-how-can-i-apply-the-login-required-decorator-to-my-entire-site-excludin.
    and https://stackoverflow.com/questions/42232606/django-exception-middleware-typeerror-object-takes-no-parameters.
    """
    def process_request(self, request):
        assert hasattr(request, 'user')

        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(re.match(url, path) for url in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
