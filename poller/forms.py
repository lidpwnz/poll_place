from django.forms import models
from django import forms
from poller.models import Poll


class PollForm(models.ModelForm):
    class Meta:
        model = Poll
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3'
            }),
        }
