from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from models import Question, Answer

def test(request):

    print("DEBUG: {}".format(request.GET.get('name')))
    return HttpResponse('OK {}'.format(request.GET))


def question(request):

    questions = Question.objects.order_by("-added_at")
    limit = 10
    page = request.GET.get("page", 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)

    context = {'page': page,
               'paginator': paginator,
               'questions': questions,
               }

    return render(request, 'index.html', context)


def pop_question(request):

    questions = Question.objects.order_by("-rating")
    limit = 10
    page = request.GET.get("page", 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)

    context = {'page': page,
               'paginator': paginator,
               'questions': questions,
               }

    return render(request, 'index.html', context)


def m_question(request, id):

    q = Question.objects.get(id=id)

    context = {'q': q,
               }

    return render(request, 'index.html', context)