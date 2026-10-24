from datetime import date
from textwrap import dedent

from minutes.meetings import load_meetings


def write(root, rel_path, text):
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(text).lstrip())


MEETING = """
    ---
    date: 2025-01-06
    members:
      - Carlton Gibson
      - Lily Foote
    other_attendees:
      - Jacob Kaplan-Moss
    ---

    ## Agenda

    1. Introductions
    """


def test_reads_yaml_front_matter(tmp_path):
    write(tmp_path, "2025/2025-01-06-steering-council.md", MEETING)

    [meeting] = load_meetings(tmp_path)

    assert meeting.slug == "2025/2025-01-06-steering-council"
    assert meeting.date == date(2025, 1, 6)
    assert meeting.members == ["Carlton Gibson", "Lily Foote"]
    assert meeting.other_attendees == ["Jacob Kaplan-Moss"]


def test_other_attendees_is_optional(tmp_path):
    write(
        tmp_path,
        "2025/2025-01-13-steering-council.md",
        """
        ---
        date: 2025-01-13
        members:
          - Tim Schilling
        ---
        Body
        """,
    )

    [meeting] = load_meetings(tmp_path)

    assert meeting.other_attendees == []


def test_sorted_newest_first(tmp_path):
    write(tmp_path, "2025/2025-01-06-steering-council.md", MEETING)
    write(
        tmp_path,
        "2026/2026-02-02-steering-council.md",
        MEETING.replace("2025-01-06", "2026-02-02"),
    )

    meetings = load_meetings(tmp_path)

    assert [m.slug for m in meetings] == [
        "2026/2026-02-02-steering-council",
        "2025/2025-01-06-steering-council",
    ]


def test_ignores_files_outside_year_folders(tmp_path):
    write(tmp_path, "2025/2025-01-06-steering-council.md", MEETING)
    write(tmp_path, "template.md", MEETING)

    assert len(load_meetings(tmp_path)) == 1


def test_titles(tmp_path):
    write(tmp_path, "2025/2025-01-06-steering-council.md", MEETING)
    write(
        tmp_path,
        "2025/2025-03-31-steering-council-fellows.md",
        MEETING.replace("2025-01-06", "2025-03-31"),
    )
    write(
        tmp_path,
        "2025/2025-09-01-steering-council-with-fellows.md",
        MEETING.replace("2025-01-06", "2025-09-01"),
    )

    titles = {m.slug: (m.title, m.short_title) for m in load_meetings(tmp_path)}

    assert titles == {
        "2025/2025-01-06-steering-council": (
            "Steering Council meeting, 6 Jan 2025",
            "2025-01-06",
        ),
        "2025/2025-03-31-steering-council-fellows": (
            "Steering Council meeting, 31 Mar 2025 (with Fellows)",
            "2025-03-31 (with Fellows)",
        ),
        "2025/2025-09-01-steering-council-with-fellows": (
            "Steering Council meeting, 1 Sep 2025 (with Fellows)",
            "2025-09-01 (with Fellows)",
        ),
    }


def html_for(tmp_path, body):
    write(
        tmp_path,
        "2025/2025-01-06-steering-council.md",
        "---\ndate: 2025-01-06\nmembers: []\n---\n" + dedent(body),
    )
    [meeting] = load_meetings(tmp_path)
    return meeting.html


def test_two_space_indented_list_stays_nested(tmp_path):
    html = html_for(tmp_path, "- Fellows:\n  - Django 6.0\n")

    assert "<li>Fellows:\n<ul>\n<li>Django 6.0</li>" in html


def test_four_space_indented_list_stays_nested(tmp_path):
    html = html_for(tmp_path, "- Our Q4 Season\n    - DEP 10\n")

    assert "<li>Our Q4 Season\n<ul>\n<li>DEP 10</li>" in html


def test_strikethrough(tmp_path):
    html = html_for(tmp_path, "django ~~community~~ commons\n")

    assert "django <s>community</s> commons" in html


def test_headings_get_ids(tmp_path):
    html = html_for(tmp_path, "## Action items\n")

    assert '<h2 id="action-items">Action items</h2>' in html


def test_quotes_are_curly(tmp_path):
    html = html_for(tmp_path, "It's \"done\"\n")

    assert "It’s “done”" in html
