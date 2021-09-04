from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from poller.forms import QuestionForm
from poller.models import Question


class CreateQuestion(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'questions/question.html'
    extra_context = {'btn_text': 'Добавить'}

    def form_valid(self, form):
        form.instance.poll_id = self.get_poll_pk()
        return super(CreateQuestion, self).form_valid(form)

    def get_poll_pk(self):
        return self.kwargs.get('poll_pk')

    def get_context_data(self, **kwargs):
        url = reverse_lazy('question_create', kwargs={'poll_pk': self.get_poll_pk()})
        return super(CreateQuestion, self).get_context_data(url=url)

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.poll_id})


class UpdateQuestion(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'questions/question.html'
    extra_context = {'btn_text': 'Обновить'}

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.poll_id})


class DeleteQuestion(DeleteView):
    model = Question

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.poll_id})
