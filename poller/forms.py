from django.forms import models
from django import forms
from poller.models import Poll, Question, Choice


class PollForm(models.ModelForm):
    class Meta:
        model = Poll
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3'
            }),
        }


class QuestionForm(models.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control mb-3'
            }),
        }


class ChoiceForm(models.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control mb-3'
            })
        }
