from django.test import TestCase
from list.models import Task, Tag


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(content='Test task', status=False)

    def test_content_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_content_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('content').max_length
        self.assertEqual(max_length, 255)

    def test_status_default(self):
        task = Task.objects.get(id=1)
        self.assertFalse(task.status)


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Test tag')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
