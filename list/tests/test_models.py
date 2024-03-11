from datetime import date
from django.test import TestCase
from list.models import Task, Tag


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(content='Test task', date=date.today(), deadline=date.today())

    def test_content_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_date_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_deadline_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('deadline').verbose_name
        self.assertEqual(field_label, 'deadline')

    def test_status_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_tags_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('tags').verbose_name
        self.assertEqual(field_label, 'tags')

    def test_content_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('content').max_length
        self.assertEqual(max_length, 255)


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Test Tag')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_str_representation(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(str(tag), tag.name)
