"""Macros for the mkdocs-macros plugin."""

import html
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml

TALKS_DIR = Path("speaking/talks")
CATEGORIES_FILE = Path("speaking/talk-categories.yml")
LINK_LABELS = (
    ("sessionize", "Sessionize"),
    ("youtube", "YouTube"),
    ("speakerdeck", "Speaker Deck"),
)


def _front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def _first(value):
    return value[0] if isinstance(value, list) else value


def _as_list(value):
    if not value:
        return []
    return value if isinstance(value, list) else [value]


def _link_html(meta):
    links = []
    for key, label in LINK_LABELS:
        urls = _as_list(meta.get(key))
        for index, url in enumerate(urls, 1):
            text = f"{label} #{index}" if len(urls) > 1 else label
            links.append(
                f'<a class="talk-badge talk-badge--{key}" href="{html.escape(url)}">{text}</a>'
            )
    return links


def _abstract_html(path):
    text = path.read_text(encoding="utf-8").split("---", 2)[2]
    lines = []
    for line in text.strip().splitlines():
        if line.startswith(("Presented at", "References:")):
            break
        lines.append(line)
    return markdown.markdown("\n".join(lines).strip()).replace("\n", " ")


def _render_item(path, meta):
    title = html.escape(meta["title"])
    slug = quote(path.stem)
    dialog_id = f"talk-{path.stem}"
    markers = ""
    if meta.get("type") == "workshop":
        markers += " <em>(workshop)</em>"
    if meta.get("inactive"):
        markers += " <em>(no longer presented)</em>"
    tags = "".join(
        f'<a class="talk-tag" data-tag="{html.escape(str(t))}" href="?tag={quote(str(t))}">{html.escape(str(t))}</a>'
        for t in meta.get("tag", [])
    )
    links = _link_html(meta)
    links_html = (
        f'<p class="talk-dialog-links">{"".join(links)}</p>' if links else ""
    )
    return (
        "<li>"
        f'<button type="button" class="talk-details" data-talk-dialog="{dialog_id}" '
        f'aria-label="Show details: {title}" title="Show details">+</button>'
        f'<a href="{slug}/">{title}</a>{markers}<br>'
        f'<span class="talk-tags"><span class="talk-tags-label">Tags:</span>{tags}</span>'
        f'<dialog class="talk-dialog" id="{dialog_id}" aria-labelledby="{dialog_id}-title">'
        f'<h3 id="{dialog_id}-title">{title}</h3>'
        f"{links_html}"
        f'<div class="talk-dialog-abstract">{_abstract_html(path)}</div>'
        '<p class="talk-dialog-actions">'
        f'<a class="talk-badge talk-badge--primary" href="{slug}/">Learn more</a> '
        '<button type="button" class="talk-badge talk-dialog-close">Close</button></p>'
        "</dialog></li>"
    )


def define_env(env):
    @env.macro
    def talks_list():
        talks = []
        for path in sorted(TALKS_DIR.glob("*.md")):
            meta = _front_matter(path)
            if meta.get("title"):
                talks.append((path, meta))
        talks.sort(key=lambda item: item[1]["title"].lower())

        categories = yaml.safe_load(CATEGORIES_FILE.read_text(encoding="utf-8")) or []
        categories.append({"name": "Other talks", "tags": []})
        buckets = {c["name"]: [] for c in categories}
        for path, meta in talks:
            tags = set(meta.get("tag", []))
            for category in categories[:-1]:
                if tags & set(category.get("tags", [])):
                    buckets[category["name"]].append((path, meta))
                    break
            else:
                buckets["Other talks"].append((path, meta))

        out = []
        for category in categories:
            items = buckets[category["name"]]
            if not items:
                continue
            section = f"## {category['name']}\n\n"
            if category.get("note"):
                section += f"> {category['note']}\n\n"
            section += "<ul>" + "".join(_render_item(p, m) for p, m in items) + "</ul>\n"
            out.append(section)
        return "\n".join(out)
