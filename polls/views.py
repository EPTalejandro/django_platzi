from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

def index(request):
    lastest_question_list = Question.objects.all()
    return render(request,"polls/index.html",{
        'lastest_question_list': lastest_question_list
    })


def detail(request, question_id):
    
    question = get_object_or_404(Question, id = question_id)
    return render(request, "polls/detail.html", {
        'question': question
    })


def results(request, question_id):
    return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")


def vote(request, question_id):
    
    question = get_object_or_404(Question, id = question_id)
    try:
        selected_choice = question.choice_set.get(id = request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            "error_message": 'no elegiste una respuesta'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        