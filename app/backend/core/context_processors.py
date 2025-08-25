from django.conf import settings


def settings_context(request):
    return {
        'DEBUG': settings.DEBUG,
        'LANGUAGE_CODE': settings.LANGUAGE_CODE,
        'TIME_ZONE': settings.TIME_ZONE,
        'USE_I18N': settings.USE_I18N,
        'USE_TZ': settings.USE_TZ,
    }