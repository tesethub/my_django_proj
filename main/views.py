from django.shortcuts import render

# Create your views here.
def index(request):
    title_page='Обо мне'
    return render(request, 'index.html', {'title_page':title_page})

def study(request):
    title_page='Обучение'
    return render(request, 'study.html', {'title_page':title_page})

def jobs(request):
    title_page='Работа'
    return render(request, 'jobs.html', {'title_page':title_page})

def not_found(request):
    return render(request, 'page_not_found.html')