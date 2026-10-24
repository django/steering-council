from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from .meetings import load_meetings, parse_meeting


def index(request):
    meetings = load_meetings(settings.MEETINGS_DIR)
    return render(request, "index.html", {"meetings": meetings})


def meeting(request, year, name):
    path = settings.MEETINGS_DIR / str(year) / f"{name}.md"
    if not path.is_file():
        raise Http404
    meeting = parse_meeting(path, settings.MEETINGS_DIR)
    return render(request, "meeting.html", {"meeting": meeting})
