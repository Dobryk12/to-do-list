from django import forms
from list.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
