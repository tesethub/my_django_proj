from django.shortcuts import render
from django.http import Http404
from  mainapp.models import *
import datetime

# Create your views here.
def index(request):
    title_page='Обо мне'
    person=Person.objects.all()[0]
    skills=Skills.objects.all()
    hobbies=Hobbies.objects.all()
    return render(request, 'index.html', {'person':person, 'skills':skills, 'hobbies':hobbies})

def study(request):
    title_page='Обучение'
    courses=Course.objects.all()
    high_education=HighEducation.objects.all()
    return render(request, 'study.html', {'title_page':title_page,  'high_education': high_education, 'courses':courses})

def jobs(request):
    title_page='работа'
    if request.POST:
        if request.POST.get('name')=='ajax':
            jobs_list=Jobs.objects.order_by('-date_from')[3:]
            template='ajax.html'
        else:
            raise Http404
    else:
        jobs_list=Jobs.objects.order_by('-date_from')[0:3]
        template='jobs.html'

    return render(request, template, {'title_page':title_page,  'jobs_list':jobs_list})

# def jobs2(request):
#
#     jobs_list=Jobs.objects.order_by('date_from')[3:]
#     return render(request, 'ajax.html', {'jobs_list':jobs_list})


def show_organization(request, organization):
    try:
        organization=Organization.objects.get(id=organization)
    except:
        raise Http404
    return render(request, 'show_org.html', {'organization':organization})

def not_found(request):
    raise Http404
    return render(reguest)