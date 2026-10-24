from datetime import UTC, datetime, time

from django.conf import settings
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

from .meetings import load_meetings


def absolute(path):
    # Build requests come from "localhost", so give the feed full URLs.
    return settings.SITE_URL + path


class MeetingsFeed(Feed):
    feed_type = Atom1Feed
    title = settings.SITE_TITLE
    subtitle = settings.SITE_DESCRIPTION

    def link(self):
        return absolute(reverse("index"))

    def feed_url(self):
        return absolute(reverse("feed"))

    def items(self):
        return load_meetings(settings.MEETINGS_DIR)[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html

    def item_link(self, item):
        return absolute(item.get_absolute_url())

    def item_pubdate(self, item):
        return datetime.combine(item.date, time(), tzinfo=UTC)
