from django.conf import settings


def site(request):
    return {
        "site_title": settings.SITE_TITLE,
        "site_description": settings.SITE_DESCRIPTION,
    }
