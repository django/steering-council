"""Builds the real site once and checks the output GitHub Pages will serve."""

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ATOM = "{http://www.w3.org/2005/Atom}"


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    out = tmp_path_factory.mktemp("site")
    subprocess.run(
        [sys.executable, "manage.py", "distill", "generate"]
        + ["--output-directory", str(out), "--collectstatic", "--force", "--quiet"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        env={"PATH": "/usr/bin:/bin"},
    )
    # The folder GitHub Pages serves at django.github.io/steering-council/.
    return out / "steering-council"


def source_slugs():
    return sorted(
        str(p.relative_to(ROOT / "meetings").with_suffix(""))
        for p in (ROOT / "meetings").glob("20*/*.md")
    )


def test_every_meeting_has_a_page(site):
    built = sorted(
        str(p.parent.relative_to(site / "meetings"))
        for p in (site / "meetings").glob("*/*/index.html")
    )

    assert built == source_slugs()


def test_meeting_page_content(site):
    html = (
        site / "meetings/2025/2025-09-01-steering-council-with-fellows/index.html"
    ).read_text()

    assert "<h1>Steering Council meeting, 1 Sep 2025 (with Fellows)</h1>" in html
    assert "<li>Emma Delescolle</li>" in html
    assert "<h2>Other attendees</h2>" in html
    assert "<li>Natalia Bidart</li>" in html
    assert '<h2 id="agenda">Agenda</h2>' in html


def test_meeting_without_other_attendees_hides_heading(site):
    html = (site / "meetings/2026/2026-09-21-steering-council/index.html").read_text()

    assert "Other attendees" not in html


def test_links_include_github_pages_prefix(site):
    html = (site / "index.html").read_text()
    hrefs = re.findall(r'href="(/[^"]*)"', html)

    assert hrefs
    assert all(h.startswith("/steering-council/") for h in hrefs), hrefs
    assert 'href="/steering-council/static/css/style.css"' in html
    assert (
        'href="/steering-council/meetings/2025/2025-01-06-steering-council/"' in html
    )


def test_static_files_are_published(site):
    assert (site / "static/css/style.css").is_file()
    assert (site / "static/favicon.svg").is_file()


def test_index_groups_by_year_newest_first(site):
    html = (site / "index.html").read_text()
    years = re.findall(r'<div class="year-label">(\d{4})</div>', html)
    dates = re.findall(r'<span class="minutes-date">([^<]*)</span>', html)

    assert years == ["2026", "2025"]
    assert len(dates) == len(source_slugs())
    assert dates[0] == "2026-10-19"
    assert dates[-1] == "2025-01-06"
    assert "2025-03-31 (with Fellows)" in dates


def test_feed(site):
    feed = ET.parse(site / "feed.xml").getroot()
    entries = feed.findall(f"{ATOM}entry")
    self_link = feed.find(f"{ATOM}link[@rel='self']").get("href")

    assert self_link == "https://django.github.io/steering-council/feed.xml"
    assert len(entries) == 10
    assert entries[0].find(f"{ATOM}link").get("href") == (
        "https://django.github.io/steering-council/meetings/2026/"
        "2026-10-19-steering-council/"
    )
    assert entries[0].find(f"{ATOM}title").text == (
        "Steering Council meeting, 19 Oct 2026"
    )
    assert "<h2" in entries[0].find(f"{ATOM}summary").text
