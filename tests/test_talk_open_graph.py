import unittest
from pathlib import Path
from types import SimpleNamespace

from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader


class TalkOpenGraphTests(unittest.TestCase):
    def setUp(self):
        template_dir = Path(__file__).resolve().parents[1] / "theme" / "overrides"
        parent = (
            '{% block analytics %}{% endblock %}'
            '{% for tag in page.meta.meta %}'
            '<meta {% for key, value in tag.items() %}{{ key }}="{{ value }}" {% endfor %}>'
            '{% endfor %}'
            '{% block extrahead %}{% endblock %}'
        )
        self.env = Environment(loader=ChoiceLoader([
            DictLoader({"main.html": parent}),
            FileSystemLoader(template_dir),
        ]))
        self.env.filters["url"] = lambda value: value

    def render(self, **meta):
        meta["meta"] = [
            {"property": "og:image", "content": "https://example.com/generated.png"},
            {"name": "twitter:image", "content": "https://example.com/generated.png"},
            {"name": "other", "content": "preserved"},
        ]
        page = SimpleNamespace(
            meta=meta, title="Example", canonical_url="https://example.com/talk/"
        )
        return self.env.get_template("talk.html").render(page=page)

    def test_custom_image_overrides_deck_and_generated_cards(self):
        output = self.render(
            ogImage="https://example.com/custom.png?a=1&b=2", speakerdeckId="deck"
        )
        self.assertIn('property="og:image" content="https://example.com/custom.png?a=1&amp;b=2"', output)
        self.assertIn('name="twitter:image" content="https://example.com/custom.png?a=1&amp;b=2"', output)
        self.assertNotIn("generated.png", output)
        self.assertNotIn("files.speakerdeck.com", output)
        self.assertIn('name="other"', output)

    def test_custom_image_without_deck(self):
        output = self.render(ogImage="https://example.com/custom.png")
        self.assertIn('property="og:image" content="https://example.com/custom.png"', output)

    def test_speakerdeck_first_slide_fallback(self):
        output = self.render(speakerdeckId=["first", "second"])
        self.assertIn('property="og:image" content="https://files.speakerdeck.com/presentations/first/slide_0.jpg"', output)
        self.assertNotIn("second/slide_0.jpg", output)
        self.assertNotIn("generated.png", output)

    def test_generated_social_card_fallback(self):
        output = self.render()
        self.assertIn("https://example.com/generated.png", output)


if __name__ == "__main__":
    unittest.main()
