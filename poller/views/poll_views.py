from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from poller.forms import ChoiceForm
from poller.helpers.views import PollAttrsMixin
from poller.models import Poll, Answer


def redirect_to_polls(request):
    return redirect('polls_list')


class ListPolls(ListView):
    model = Poll
    template_name = 'polls/list.html'
    paginate_by = 5
    context_object_name = 'polls'
    ordering = ['-created_at']


class CreatePoll(PollAttrsMixin, CreateView):
    extra_context = {'btn_text': 'Create', 'url': reverse_lazy('polls_create')}


class UpdatePoll(PollAttrsMixin, UpdateView):
    extra_context = {'btn_text': 'Update'}

    def get_context_data(self, **kwargs):
        url = reverse_lazy('polls_update', kwargs={'pk': self.object.pk})
        return super(UpdatePoll, self).get_context_data(url=url)


class DetailPoll(PollAttrsMixin, DetailView):
    template_name = 'polls/detail.html'
    extra_context = {'btn_text': 'Добавить'}

    def get_context_data(self, **kwargs):
        return super(DetailPoll, self).get_context_data(form=ChoiceForm(), questions=self.get_stat_context())

    def get_questions(self):
        return self.object.question_set.all()

    def get_total_count(self):
        return sum([item.answer_set.count() for item in self.get_questions()])

    def get_choice_data(self, question):
        question_data = {
            'question': question,
            'choices_stats': []
        }

        for choice in question.choice_set.all():
            count = choice.answer_set.count()
            choice_stat = {
                'choice': choice,
                'count': count,
                'percent_part': f'{(count / self.get_total_count()) * 100}%' if count else '0%'
            }
            question_data['choices_stats'].append(choice_stat)

        return question_data

    def get_stat_context(self):
        context = []
        questions = self.get_questions()

        for question in questions:
            context.append(self.get_choice_data(question))

        return context


class DeletePoll(PollAttrsMixin, DeleteView):
    def get_success_url(self):
        return reverse_lazy('polls_list')


class CreateAnswer(TemplateView):
    template_name = 'answers/index.html'
    success_url = reverse_lazy('polls_list')
    poll = None

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(poll=self.poll)

    def get_poll(self):
        return get_object_or_404(Poll, pk=self.kwargs.get('poll_pk'))

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')

        for answer in data:
            question_id = int(answer[0])
            choice_id = int(data[answer][0])
            Answer.objects.create(question_id=question_id, choice_id=choice_id).save()
        return redirect('polls_list')
