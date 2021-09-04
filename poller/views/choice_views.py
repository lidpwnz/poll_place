from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from poller.forms import ChoiceForm
from poller.models import Choice, Question


class ChoiceCreate(CreateView):
    model = Choice
    extra_context = {'btn_text': 'Создать'}
    form_class = ChoiceForm
    template_name = 'polls/detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.get_question_pk()
        return super(ChoiceCreate, self).form_valid(form)

    def form_invalid(self, form):
        return redirect(self.get_success_url())

    def get_question_pk(self):
        return self.kwargs.get('question_pk')

    def get_success_url(self):
        pk = Question.objects.get(pk=self.get_question_pk()).poll_id
        return reverse_lazy('polls_detail', kwargs={'pk': pk})


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
