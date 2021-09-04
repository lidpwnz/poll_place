from django.db.models import Count
from django.urls import reverse_lazy
from poller.forms import PollForm
from poller.models import Poll, Answer


class Statistics:
    def __init__(self, queryset, obj_name):
        self.queryset = queryset
        self.object_name = obj_name

    def get_objects_with_count(self, *args, count_attr=None):
        objects = self.queryset
        if count_attr:
            print(objects.values(*args).annotate(count=Count(count_attr)))
            return objects.values(*args).annotate(count=Count(count_attr))

    def get_total_count(self):
        return sum([item.answer_set.count() for item in self.queryset])

    def get_object_info(self, object_text, object_count, choice_id):
        return {
                choice_id: object_text,
                'count': object_count,
                'percent_part': f'{(object_count / self.get_total_count()) * 100}%'
            }

    def get_statistic(self):
        for i in self.get_objects_with_count('choice__text', 'choice__id', count_attr='choice'):
            pass


class PollAttrsMixin:
    """Base attrs for create and update views of Poll model"""
    object = None
    model = Poll
    template_name = 'polls/poll.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse_lazy('polls_detail', kwargs={'pk': self.object.pk})
