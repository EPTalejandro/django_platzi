from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice


def index(request):
    lastest_question_list = Question.objects.all()
    return render(request,"polls/index.html",{
        'lastest_question_list': lastest_question_list
    })


def detail(request, question_id):
    return HttpResponse(f"estas viendo la pregunta numero {question_id}")


def results(request, question_id):
    return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")


def vote(request, question_id):
    return HttpResponse(f"estas votando a la pregunta numero {question_id}")