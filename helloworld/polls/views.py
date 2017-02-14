#coding:utf-8
from django.shortcuts import render

from django.http import HttpResponse
from django.template import  loader
from .models import Question
from .models import XXLcolrow


def index(request):
    '''
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    template =loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)
    '''
    myrecord=XXLcolrow.objects.order_by('-last_date')[:1]
    template =loader.get_template('polls/index.html')
    context={
        'myrecord':10,
        }
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    return HttpResponse("You are looking at question %s."%question_id)
def results(request,question_id):
    response="you are looking at the results of question %s."
    return HttpResponse(response%question_id)
def vote(reqest,question_id):
    return HttpResponse("you are voting on question %s."%question_id)

# Create your views here.
