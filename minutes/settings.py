import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# `just up` sets DJANGO_DEBUG=1 so the dev server shows errors and serves static.
DEBUG = os.environ.get("DJANGO_DEBUG") == "1"

SECRET_KEY = "not-secret-static-site-only"
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "django_distill",
    "minutes",
]

ROOT_URLCONF = "minutes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "minutes.context_processors.site",
            ],
        },
    }
]

USE_TZ = True
TIME_ZONE = "UTC"

SITE_TITLE = "Django Steering Council Meeting Minutes"
SITE_DESCRIPTION = "Meeting minutes of the Django Steering Council"
SITE_URL = "https://django.github.io"

# GitHub Pages serves the site under /steering-council/, so every URL carries it.
# (FORCE_SCRIPT_NAME doesn't work: distill requests the prefixed path and 404s.)
URL_PREFIX = "steering-council/"

MEETINGS_DIR = BASE_DIR / "meetings"

STATIC_URL = f"/{URL_PREFIX}static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
