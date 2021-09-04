from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from poller.forms import ChoiceForm
from poller.models import Choice


class ChoiceCreate(CreateView):
    model = Choice
    extra_context = {'btn_text': 'Создать'}
    form_class = ChoiceForm

    def form_valid(self, form):
        form.instance.question_id = self.get_question_pk()
        return super(ChoiceCreate, self).form_valid(form)

    def get_question_pk(self):
        return self.kwargs.get('question_pk')

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.question.poll_id})


class ChoiceUpdate(UpdateView):
    model = Choice
    template_name = 'choices/choice.html'
    form_class = ChoiceForm
    extra_context = {'btn_text': 'Обновить'}

    def get_context_data(self, **kwargs):
        url = reverse_lazy('choice_update', kwargs={'pk': self.object.pk})
        return super(ChoiceUpdate, self).get_context_data(url=url)

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.question.poll_id})


class ChoiceDelete(DeleteView):
    model = Choice

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.question.poll_id})
