from django import forms

from links.models import Link


class LinkCreateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['text']
