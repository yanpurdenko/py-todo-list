import datetime

from django.test import TestCase
from django.urls import reverse

from app.models import Task, Tag

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


class TaskManagingTests(TestCase):

    def setUp(self) -> None:
        self.task = Task.objects.create(
            title="test",
            created_at=datetime.datetime.now(),
            is_done=False,
        )

    def test_complete_task(self):
        response = self.client.post(reverse("app:complete-task", args=[self.task.pk]))

        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.is_done, True)

    def test_undo_task(self):
        response = self.client.post((reverse("app:undo-task", args=[self.task.pk])))

        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.is_done, False)

    def test_create_task(self):
        response = self.client.post(
            reverse("app:task-create"),
            {
                "title": "test1",
                "created_at": datetime.datetime.now(),
                "is_done": False,
            }
        )

        db_tasks = Task.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(db_tasks.count(), 2)

    def test_task_update(self):
        payload = {
            "title": "test2",
            "created_at": datetime.datetime.now(),
            "is_done": False,
        }
        response = self.client.post(reverse("app:task-update", args=[self.task.pk]), payload)

        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, payload["title"])

    def test_delete_task(self):
        response = self.client.delete(reverse("app:task-delete", args=[self.task.pk]))
        db_task_id_1 = Task.objects.filter(id=1)

        self.assertEqual(db_task_id_1.count(), 0)
        self.assertEqual(response.status_code, 302)


class TagManagingTests(TestCase):

    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test")

    def test_create_tag(self):
        response = self.client.post(reverse("app:tag-create"), {"name": "test1"})

        db_tags = Tag.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(db_tags.count(), 2)

    def test_tag_update(self):
        payload = {"name": "test2"}
        response = self.client.post(reverse("app:tag-update", args=[self.tag.pk]), payload)

        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, payload["name"])

    def test_delete_tag(self):
        response = self.client.delete(reverse("app:tag-delete", args=[self.tag.pk]))
        db_task_id_1 = Tag.objects.filter(id=1)

        self.assertEqual(db_task_id_1.count(), 0)
        self.assertEqual(response.status_code, 302)
