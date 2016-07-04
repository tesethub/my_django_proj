from django.shortcuts import render
from django.http import Http404
from  mainapp.models import *
import datetime

# Create your views here.
def index(request):
    title_page='Обо мне'
    first_name='Александр'
    next_name='сергеевич'
    last_name='Козлов'
    nickname='Alex L, Alex Lastname, Alex Kozlov'

    img='w150.jpg'
    personal_data=[{'name': 'Дата рождения', 'value': datetime.date(1980, 5, 5)},
              {'name': 'Место проживания', 'value': 'г. Казань'},
              {'name': 'Гражданство', 'value': 'РФ'},
              {'name': 'Образование', 'value': 'высшее'}]
    contacts=[{'name': 'Email', 'value': 'e-finder@rambler.ru'},
              {'name': 'Skype', 'value': ' 	user08012013'}]
    about_me=[{'name': 'Личные качества', 'content':'Есть желание обучаться, развиваться '
                                                    'профессионально,  повышать уровень '
                                                    'знаний в данной области, обучаться новым технологиям и уметь применять полученные знания на практике. '}]

    skills=[{'name': 'Back-end', 'content':'Python -знания на среднем уровне, без практического опыта. Джанго- начинал учить самостоятельно, сейчас хочу продолжить. '
                                           'Когда -то знал PHP, даже короткое время работал программистом PHP, но очень давно, уже подзабыл. '},
            {'name': 'Front-end', 'content':'HTML, CSS, Javascript (больше в виде Jquery). C Bootstrap не работал, равно как и с предпроцессорами.'}]
   # hobbies=['Туризм', 'велопрогулки', 'интернет-серфинг']
    #person=Person.objects.get(id=0)
    #skills=Skills.objects.all()
    hobbies=Hobbies.objects.all()
    return render(request, 'index.html', locals())

def study(request):
    title_page='Обучение'
    courses=Course.objects.all()

    high_education=[{'university':'Казанский Государственный Университет им. В. И. Ульянова-Ленина',
                     'department':'дневное',
                     'faculty':'биолого-почвенный'}]


    return render(request, 'study.html', {'title_page':title_page,  'high_education': high_education, 'courses':courses})

def jobs(request):
    title_page='работа'

    page_heading='Работа'
    jobs_list=Jobs.objects.all()
    # jobs_list=[{'employer':'ГБОУ ДПО Казанская Государственная медицинская академия', 'position':' ведущий инженер-программист' , 'period':'2012-2015 г.'},
    #            {'employer':'ООО Clientbase', 'position':' программист' , 'period':'2011 г.'},
    #            {'employer':'ООО ”Строй Стандарт”', 'position':' инженер' , 'period':'2008-2011г.'},
    #            {'employer':'ФГУП “НПО ГИПО”, отдел информационных технологий и защиты информации', 'position':' инженер-программист' , 'period':'2003-2008 г.'}]
    return render(request, 'jobs.html', {'title_page':title_page,  'page_heading':page_heading,'jobs_list':jobs_list})

def not_found(request):
    raise Http404
    return render(reguest)