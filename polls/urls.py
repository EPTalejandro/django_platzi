from django.urls import path

from . import views

urlpatterns = [
    #ex: /polls/
    path("", views.index, name='index'),
    #ex: /polls/3/
    path("<int:question_id>/", views.detail, name='details'),
    #ex: /polls/4/results/
    path("<int:question_id>/results/", views.results, name='results'),
    #ex: /polls/6/votes
    path("<int:question_id>/vote/", views.vote, name='votes')
]
