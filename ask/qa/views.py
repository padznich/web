from datetime import datetime, timedelta
import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from models import Question, Answer, User, Session
from forms import AskForm, AnswerForm, LoginForm


def login(request):
    error = ''
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        url = request.POST.get('continue', '/')
        sessid = do_login(login, password)
        if sessid:
            response = HttpResponseRedirect(url)
            response.set_cookie('sessid', sessid, domain='.site.com', httponly=True,
                                expires=datetime.now()+timedelta(days=5)
                                )
            return response
        else:
            error = u'Wrong Login / Password'
    return render(request, 'login.html', {'error': error, 'form': form})


def do_login(login, password):
    try:
        user = User.objects.get(login=login)
    except User.DoesNotExist:
        return None
    hashed_pass = salt_and_hash(password)
    if user.password != hashed_pass:
        return None
    session = Session()
    session.key = generate_long_random_key()
    session.user = user
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key

def salt_and_hash(sd):
    return len(sd)

def generate_long_random_key():
    return (''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
                     for x in range(60)]))


def ask(request):

    if request.method == "POST":
        ask_form = AskForm(request.POST or None)
        ask_form._user = request.user
        if ask_form.is_valid():
            post = ask_form.save()
            url = post.get_url()
            print("____DEBUG: {}".format(url))
            return HttpResponseRedirect(url)
    else:
        ask_form = AskForm()

    context = {
        "ask_form": ask_form,
    }

    return render(request, 'ask.html', context)


def test(request):

    print("DEBUG: {}".format(request.GET.get('name')))
    return HttpResponse('OK {}'.format(request.GET))


def question(request):

    questions = Question.objects.order_by("-id")
    limit = 10
    page = request.GET.get("page", 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)

    context = {'page': page,
               'paginator': paginator,
               'questions': page.object_list,
               }

    return render(request, 'home.html', context)


def pop_question(request):

    questions = Question.objects.order_by("-rating")
    limit = 10
    page = request.GET.get("page", 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)

    context = {'page': page,
               'paginator': paginator,
               'questions': page.object_list,
               }
    return render(request, 'popular_questions.html', context)


def m_question(request, id):

    q = Question.objects.get(id=id)
    a = Answer.objects.filter(question=id)

    context = {'q': q,
               'a': a,
               }

    return render(request, 'question.html', context)
