from django.urls import path, include
from poller.views.question_views import CreateQuestion, UpdateQuestion, DeleteQuestion

urlpatterns = [
    path('<int:poll_pk>/add', CreateQuestion.as_view(), name='question_create'),
    path('<int:pk>/update', UpdateQuestion.as_view(), name='question_update'),
    path('<int:pk>/delete', DeleteQuestion.as_view(), name='question_delete'),

    path('choices/', include('poller.urls.choice_urls'))
]