from django.urls import path, include

from poller.views.poll_views import ListPolls, DetailPoll, CreatePoll, UpdatePoll, DeletePoll
from poller.views.question_views import CreateQuestion, UpdateQuestion, DeleteQuestion

urlpatterns = [
    path('', ListPolls.as_view(), name='polls_list'),
    path('<int:pk>/detail', DetailPoll.as_view(), name='polls_detail'),
    path('create', CreatePoll.as_view(), name='polls_create'),
    path('<int:pk>/update', UpdatePoll.as_view(), name='polls_update'),
    path('<int:pk>/delete', DeletePoll.as_view(), name='polls_delete'),
    path('questions/', include('poller.urls.question_urls')),

]
