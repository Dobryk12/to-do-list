from django import forms

from list.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    status = forms.BooleanField(
        label="Complete?")
    class Meta:
        model = Task
        fields = ["status"]


class TaskFormForCreate(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
