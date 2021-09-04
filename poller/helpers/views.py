from django.urls import reverse_lazy
from poller.forms import PollForm
from poller.models import Poll


class PollAttrsMixin:
    """Base attrs for create and update views of Poll model"""
    object = None
    model = Poll
    template_name = 'polls/poll.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.pk})
