from django.test import TestCase
from django.urls import reverse

from app.models import Task

INDEX_VIEW_URL = reverse("app:index")
TAG_LIST_URL = reverse("app:tag-list")


class AccessibilityViewTests(TestCase):

    def test_retrieve_index_page(self):
        response = self.client.get(INDEX_VIEW_URL)
        queryset = Task.objects.prefetch_related("tags")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["task_list"]), list(queryset))
        self.assertTemplateUsed(response, "app/index.html")

    def test_retrieve_tag_list_page(self):
        response = self.client.get(TAG_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/tag_list.html")
