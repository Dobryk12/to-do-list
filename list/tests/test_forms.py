from django.test import TestCase
from list.forms import TagForm, TaskForm, TaskFormForCreate
from list.models import Task, Tag

class TagFormTest(TestCase):
    def test_tag_form_fields(self):
        form = TagForm()
        self.assertEqual(form.Meta.model, Tag)
        self.assertEqual(form.Meta.fields, "__all__")


class TaskFormTest(TestCase):
    def test_task_form_fields(self):
        form = TaskForm()
        self.assertEqual(form.Meta.model, Task)
        self.assertEqual(form.Meta.fields, ["status"])

    def test_task_form_status_label(self):
        form = TaskForm()
        self.assertEqual(form.fields['status'].label, "Complete?")


class TaskFormForCreateTest(TestCase):
    def test_task_form_for_create_fields(self):
        form = TaskFormForCreate()
        self.assertEqual(form.Meta.model, Task)
        self.assertEqual(form.Meta.fields, "__all__")
