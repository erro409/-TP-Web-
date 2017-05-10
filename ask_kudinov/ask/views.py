from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from ask.models import *
from ask.func import *
from . import forms

# Create your views here.
context = {
  'questions' : [],
  'answers' : [],
  'qtags' : [" "],
  'toptags' : [" "],
  'topusers' : [" "],
}
#for i in xrange(1,30):
#    context['questions'].append({
#        'title': 'title question' + str(i),
#        'id': i,
#        'text':'text question' + str(i),
#    }) 
#
#for i in xrange(1,30):
#    context['answers'].append({
#        'title': 'title answer' + str(i),
#        'id': i,
#        'text':'text answer' + str(i),
#    }) 
#
#def pagination(contact_list, page):
#    paginator = Paginator(contact_list,5)
#    try:
#        questions = paginator.page(page)
#    except PageNotAnInteger:
#        questions=paginator.page(1)
#    except EmptyPage:
#        questions=paginator.page(1)
#    return questions

def index(request, page='1'):
    questions=pagination(request, Question.objects.get_by_time(), 20, page)
    questions.paginator.baseurl='/'
    return render(request, './index.html', {'questions' : questions})

def question(request, question_id):
    if request.method=='POST':
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=forms.QuestionForm()
        question = get_object_or_404(Question, pk=question_id)
        answers = question.answer_set.all()
        context['form']=form
        context['question_id']=question_id
	context['current_question']=question
        context['answers']=answers
    return render(request, './question.html', context)

def hot(request, page='1'):
    questions = pagination(request, Question.objects.get_by_rating(), 20, page)
    questions.paginator.baseurl='/hot/'
    return render(request, './hot.html', {'questions' : questions})  #should change index.html to hot.html in which the highlitning changes

def by_tag(request,tag , page='1'):
    questions = pagination(request, Question.objects.get_by_tag(tag), 20, page)
    questions.paginator.baseurl='/tag/' + tag +'/'
    return render(request, './tag.html', {'questions' : questions, 'tag' : tag})  #should fix htmls links

def ask(request):
    if request.method=='POST':
        form = forms.AskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=forms.AskForm()

    return render(request, './ask.html', {'form': form})

def login(request):
    if request.method=='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=forms.LoginForm()

    return render(request, './login.html', {'form': form})

def signup(request):
    if request.method=='POST':
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=forms.SignupForm()

    return render(request, './signup.html', {'form': form})

def settings(request):
    if request.method=='POST':
        form = forms.SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=forms.SettingsForm()

    return render(request, './settings.html', {'form': form})
