"""Macros for the mkdocs-macros plugin."""

import html
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml

TALKS_DIR = Path("speaking/talks")
WORKSHOPS_DIR = Path("speaking/workshops")
CATEGORIES_FILE = Path("speaking/talk-categories.yml")
TOP_TAGS = 10
LINK_LABELS = (
    ("github", "GitHub"),
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
        if line.startswith(("Presented at",)):
            break
        lines.append(line)
    return markdown.markdown("\n".join(lines).strip()).replace("\n", " ")


def _tag_cloud(items):
    counts = {}
    for _, meta in items:
        for tag in meta.get("tag", []):
            counts[str(tag)] = counts.get(str(tag), 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

    def link(t, n, extra=""):
        return (
            f'<a class="talk-tag{extra}" data-tag="{html.escape(t)}" href="?tag={quote(t)}" '
            f'title="{n} item{"s" if n > 1 else ""}">{html.escape(t)}</a>'
        )

    tags = "".join(link(t, n) for t, n in ranked[:TOP_TAGS])
    if len(ranked) > TOP_TAGS:
        tags += (
            f'<button type="button" class="talk-details talk-tags-toggle" aria-expanded="false" '
            f'title="Show all tags">+</button>'
        )
        tags += "".join(link(t, n, " talk-tag-extra") for t, n in ranked[TOP_TAGS:])
    return f'<p class="talk-tags talk-tag-cloud"><span class="talk-tags-label">Browse by tag:</span>{tags}</p>\n\n'


def _render_item(path, meta, base):
    title = html.escape(meta["title"])
    rel = path.relative_to(base).with_suffix("")
    slug = "/".join(quote(part) for part in rel.parts)
    dialog_id = "talk-" + "-".join(rel.parts)
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
    deck = _first(meta.get("speakerdeckId"))
    thumb = (
        f'<a class="talk-thumb" href="{slug}/" tabindex="-1" aria-hidden="true">'
        f'<img loading="lazy" alt="" src="https://files.speakerdeck.com/presentations/{deck}/slide_0.jpg"></a>'
        if deck
        else ""
    )
    links_html = (
        f'<p class="talk-dialog-links">{"".join(links)}</p>' if links else ""
    )
    dialog_image = (
        f'<a class="talk-dialog-image" href="{slug}/"><img loading="lazy" alt="{title}" '
        f'src="https://files.speakerdeck.com/presentations/{deck}/slide_0.jpg"></a>'
        if deck
        else ""
    )
    desc = meta.get("description")
    desc_html = f'<span class="talk-desc">{html.escape(str(desc))}</span><br>' if desc else ""
    return (
        f'<li class="talk-item{" has-thumb" if deck else ""}">'
        f"{thumb}"
        f'<button type="button" class="talk-details" data-talk-dialog="{dialog_id}" '
        f'aria-label="Show details: {title}" title="Show details">+</button>'
        f'<a href="{slug}/">{title}</a>{markers}<br>'
        f"{desc_html}"
        f'<span class="talk-tags"><span class="talk-tags-label">Tags:</span>{tags}</span>'
        f'<dialog class="talk-dialog" id="{dialog_id}" aria-labelledby="{dialog_id}-title">'
        f'<h3 id="{dialog_id}-title">{title}</h3>'
        f"{dialog_image}"
        f"{links_html}"
        f'<div class="talk-dialog-abstract">{_abstract_html(path)}</div>'
        f'<p class="talk-tags"><span class="talk-tags-label">Tags:</span>{tags}</p>'
        '<p class="talk-dialog-actions">'
        f'<a class="talk-badge talk-badge--primary" href="{slug}/">Learn more</a> '
        '<button type="button" class="talk-badge talk-dialog-close">Close</button></p>'
        "</dialog></li>"
    )


def _load(directory):
    items = []
    for path in sorted(directory.rglob("*.md")):
        meta = _front_matter(path)
        if meta.get("title"):
            items.append((path, meta))
    items.sort(key=lambda item: item[1]["title"].lower())
    return items


def define_env(env):
    @env.macro
    def workshops_list():
        items = _load(WORKSHOPS_DIR)
        return _tag_cloud(items) + "<ul>" + "".join(_render_item(p, m, WORKSHOPS_DIR) for p, m in items) + "</ul>\n"

    @env.macro
    def talks_list():
        talks = []
        for path in sorted(TALKS_DIR.rglob("*.md")):
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

        out = [_tag_cloud(talks)]
        for category in categories:
            items = buckets[category["name"]]
            if not items:
                continue
            section = f"## {category['name']}\n\n"
            if category.get("note"):
                section += f"> {category['note']}\n\n"
            section += "<ul>" + "".join(_render_item(p, m, TALKS_DIR) for p, m in items) + "</ul>\n"
            out.append(section)
        return "\n".join(out)
