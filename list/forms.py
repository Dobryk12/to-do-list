from django import forms

from list.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
