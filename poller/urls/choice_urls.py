from django.urls import path
from poller.views.choice_views import ChoiceCreate, ChoiceDelete, ChoiceUpdate

urlpatterns = [
    path('<int:question_pk>/create', ChoiceCreate.as_view(), name='choice_create'),
    path('<int:pk>/delete', ChoiceDelete.as_view(), name='choice_delete'),
    path('<int:pk>/update', ChoiceUpdate.as_view(), name='choice_update'),
]