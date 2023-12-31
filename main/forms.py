# forms.py
from django import forms
from multiupload.fields import MultiFileField
from .models import HomeWork


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ['theme']

    attachments = MultipleFileField()
    def save(self, commit=True):
        instance = super(MyForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
 
