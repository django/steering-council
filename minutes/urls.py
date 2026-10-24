from django.conf import settings
from django.urls import include, path
from django_distill import distill_path

from . import views
from .feeds import MeetingsFeed
from .meetings import load_meetings


def meeting_urls():
    return [m.slug.split("/") for m in load_meetings(settings.MEETINGS_DIR)]


site_urls = [
    distill_path("", views.index, name="index"),
    distill_path(
        "meetings/<int:year>/<slug:name>/",
        views.meeting,
        name="meeting",
        distill_func=meeting_urls,
    ),
    distill_path("feed.xml", MeetingsFeed(), name="feed"),
]

urlpatterns = [path(settings.URL_PREFIX, include(site_urls))]
