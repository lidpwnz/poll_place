from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from poller.helpers.views import PollAttrsMixin
from poller.models import Poll


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


class DeletePoll(PollAttrsMixin, DeleteView):
    def get_success_url(self):
        return reverse_lazy('polls_list')
