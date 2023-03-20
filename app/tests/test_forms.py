from django.test import TestCase

from app.forms import TaskForm, TagForm
from app.models import Tag


class FormsTests(TestCase):

    def test_task_form_is_valid(self):

        form_data = {
            "title": "test",
            "deadline": None,
            "is_done": False,
            "tags": Tag.objects.all()
        }
        task_form = TaskForm(data=form_data)

        self.assertTrue(task_form.is_valid())
        first_temp = task_form.cleaned_data.pop("tags")
        second_temp = form_data.pop("tags")
        self.assertEqual(task_form.cleaned_data, form_data)
        self.assertEqual(first_temp.first(), second_temp.first())

    def test_tag_form_is_valid(self):

        form_data = {
            "name": "test",
        }
        tag_form = TagForm(data=form_data)

        self.assertTrue(tag_form.is_valid())
        self.assertEqual(tag_form.cleaned_data, form_data)
