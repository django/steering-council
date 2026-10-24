from dataclasses import dataclass, field
from datetime import date
from functools import cached_property
from pathlib import Path

import yaml
from django.urls import reverse
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin

# CommonMark nests lists like Jekyll's kramdown GFM (2- or 4-space indents).
# Strikethrough, heading ids and curly quotes match it too.
markdown = (
    MarkdownIt("commonmark", {"typographer": True})
    .enable(["strikethrough", "smartquotes", "replacements"])
    .use(anchors_plugin, max_level=6)
)


@dataclass
class Meeting:
    slug: str
    date: date
    members: list[str]
    body: str
    other_attendees: list[str] = field(default_factory=list)

    @property
    def with_fellows(self) -> bool:
        return "fellows" in self.slug.rsplit("/", 1)[-1]

    @property
    def title(self) -> str:
        title = f"Steering Council meeting, {self.date.day} {self.date:%b %Y}"
        return title + (" (with Fellows)" if self.with_fellows else "")

    @property
    def short_title(self) -> str:
        return f"{self.date:%Y-%m-%d}" + (" (with Fellows)" if self.with_fellows else "")

    @cached_property
    def html(self) -> str:
        return markdown.render(self.body)

    def get_absolute_url(self) -> str:
        return reverse("meeting", args=self.slug.split("/"))


def parse_meeting(path: Path, root: Path) -> Meeting:
    _, front_matter, body = path.read_text().split("---\n", 2)
    data = yaml.safe_load(front_matter)
    return Meeting(
        slug=str(path.relative_to(root).with_suffix("")),
        date=data["date"],
        members=data["members"],
        other_attendees=data.get("other_attendees") or [],
        body=body,
    )


def load_meetings(root: Path) -> list[Meeting]:
    """Every meeting under root/<year>/, newest first."""
    meetings = [parse_meeting(p, root) for p in root.glob("20*/*.md")]
    return sorted(meetings, key=lambda m: m.date, reverse=True)
