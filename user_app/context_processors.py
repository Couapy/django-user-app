from django.conf import settings


def providers_settings(request):
    return {
        'USER_APP_PROVIDERS': settings.USER_APP_PROVIDERS,
    }
