import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import markdown

from speaking.talks import talks_macros


class MacroEnvironment:
    def macro(self, function):
        setattr(self, function.__name__, function)
        return function


class TalkStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.talks = self.root / "talks"
        self.workshops = self.root / "workshops"
        self.talks.mkdir()
        self.workshops.mkdir()
        self.categories = self.root / "categories.yml"
        self.categories.write_text("- name: Testing\n  tags: [testing]\n", encoding="utf-8")
        for name, value in (
            ("TALKS_DIR", self.talks),
            ("WORKSHOPS_DIR", self.workshops),
            ("CATEGORIES_FILE", self.categories),
        ):
            patcher = patch.object(talks_macros, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.env = MacroEnvironment()
        talks_macros.define_env(self.env)

    def write_item(self, directory, filename, title, status=None, tag="testing"):
        status_line = f"status: {status}\n" if status is not None else ""
        (directory / f"{filename}.md").write_text(
            f"---\ntitle: {title}\ntag: [{tag}]\n{status_line}---\nAbstract\n",
            encoding="utf-8",
        )

    def test_talk_statuses_and_category_tag_cloud(self):
        self.write_item(self.talks, "normal", "A normal")
        self.write_item(self.talks, "highlight", "Z highlight", "highlighted")
        self.write_item(self.talks, "collapsed", "B collapsed", "collapsed", "other")
        self.write_item(self.talks, "hidden", "Hidden talk", "hidden", "secret")
        output = self.env.talks_list()
        self.assertNotIn("Hidden talk", output)
        self.assertNotIn('data-tag="secret"', output)
        self.assertLess(output.index("Z highlight"), output.index("A normal"))
        self.assertIn('class="talk-item talk-item--highlighted"', output)
        self.assertIn('data-collapsed="true"', output)
        self.assertIn('aria-expanded="false">More talks</button>', output)
        self.assertIn("## Other talks", output)
        rendered = markdown.markdown(output)
        self.assertIn('</ul>\n<p class="talk-more" hidden>', rendered)

    def test_workshops_use_same_statuses(self):
        self.write_item(self.workshops, "normal", "Normal workshop", "normal")
        self.write_item(self.workshops, "collapsed", "Collapsed workshop", "collapsed")
        self.write_item(self.workshops, "hidden", "Hidden workshop", "hidden")
        output = self.env.workshops_list()
        self.assertIn("Normal workshop", output)
        self.assertIn("Collapsed workshop", output)
        self.assertNotIn("Hidden workshop", output)
        self.assertIn("More talks", output)

    def test_invalid_status_fails_with_path(self):
        self.write_item(self.talks, "invalid", "Invalid", "colapsed")
        with self.assertRaisesRegex(ValueError, "invalid.md: invalid talk status 'colapsed'"):
            self.env.talks_list()

    def test_no_more_button_when_nothing_collapsed(self):
        self.write_item(self.talks, "normal", "Normal")
        self.assertNotIn("talk-more-toggle", self.env.talks_list())

    def test_custom_image_takes_precedence_in_list_and_dialog(self):
        self.write_item(self.talks, "item", "Talk")
        path = self.talks / "item.md"
        image = 'https://example.com/image.jpg?a=1&b=2'
        output = talks_macros._render_item(
            path, {"title": "Talk", "speakerdeckId": "deck", "ogImage": image}, self.talks
        )
        self.assertEqual(output.count('src="https://example.com/image.jpg?a=1&amp;b=2"'), 2)
        self.assertNotIn("files.speakerdeck.com", output)
        self.assertIn("has-thumb", output)

    def test_images_fallback_to_first_speakerdeck_slide_or_none(self):
        self.write_item(self.workshops, "item", "Workshop")
        path = self.workshops / "item.md"
        output = talks_macros._render_item(
            path, {"title": "Workshop", "speakerdeckId": ["first", "second"]}, self.workshops
        )
        self.assertEqual(output.count("https://files.speakerdeck.com/presentations/first/slide_0.jpg"), 2)
        self.assertNotIn("second/slide_0.jpg", output)
        output = talks_macros._render_item(path, {"title": "Workshop"}, self.workshops)
        self.assertNotIn("has-thumb", output)
        self.assertNotIn("talk-dialog-image", output)

    def test_custom_image_without_speakerdeck(self):
        self.write_item(self.workshops, "item", "Workshop")
        output = talks_macros._render_item(
            self.workshops / "item.md",
            {"title": "Workshop", "ogImage": "https://example.com/image.png"},
            self.workshops,
        )
        self.assertIn("has-thumb", output)
        self.assertEqual(output.count('src="https://example.com/image.png"'), 2)


if __name__ == "__main__":
    unittest.main()
