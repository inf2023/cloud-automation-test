from django.test import TestCase

from .models import Task


class TaskDatabaseTests(TestCase):
    def test_create_persists_defaults(self):
        task = Task.objects.create(title="Run cloud tests")
        task.refresh_from_db()
        self.assertIsNotNone(task.pk)
        self.assertEqual(task.title, "Run cloud tests")
        self.assertFalse(task.completed)
        self.assertEqual(Task.objects.count(), 1)

    def test_read_filters_persisted_tasks(self):
        pending = Task.objects.create(title="Pending")
        Task.objects.create(title="Finished", completed=True)
        self.assertEqual(list(Task.objects.filter(completed=False)), [pending])
        self.assertEqual(Task.objects.get(title="Finished").completed, True)

    def test_update_persists_without_changing_other_tasks(self):
        task = Task.objects.create(title="Draft")
        other = Task.objects.create(title="Untouched")
        task.title = "Ready"
        task.completed = True
        task.save(update_fields=["title", "completed"])
        task.refresh_from_db()
        other.refresh_from_db()
        self.assertEqual(task.title, "Ready")
        self.assertTrue(task.completed)
        self.assertEqual(other.title, "Untouched")
        self.assertFalse(other.completed)
