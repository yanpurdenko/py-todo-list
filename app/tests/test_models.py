from unittest import TestCase

from app.models import Tag, Task


class ModelsTests(TestCase):
    def test_tag_str(self):

        tag = Tag.objects.create(name="work")

        self.assertEqual(str(tag), tag.name)

    def test_task_str(self):

        task = Task.objects.create(title="test")

        self.assertEqual(str(task), task.title)
