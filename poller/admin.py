from django.contrib import admin
from poller.models import Question, Choice, Poll


admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Choice)
