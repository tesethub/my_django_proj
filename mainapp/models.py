from django.db import models

# Create your models here.
class Jobs(models.Model):
     employer=models.CharField(verbose_name='Наименование работодателя', max_length=255)
     position=models.CharField(verbose_name='Должность', max_length=255)
     employer_site=models.URLField(verbose_name='Сайт', blank=True)
     date_from=models.DateField(verbose_name='Начало периода работы')
     date_to=models.DateField(verbose_name='Окончание периода работы')

class Course(models.Model):
    name=models.CharField(verbose_name='Наименование курса', max_length=255)
    vendor=models.CharField(verbose_name='Образовательное учреждение или учебный центр', max_length=255)
    vendor_site=models.URLField(blank=True)
    period=models.DateField(verbose_name='Год обучения')
    relevant=models.BooleanField(verbose_name='Отношение к рассматриваемой теме', default=False)

class HighEducation (models.Model):

    name=models.CharField(verbose_name='Наименование ВУЗА', max_length=255)
    faculty=models.CharField(verbose_name='Факультет', max_length=100)
    department=models.CharField(verbose_name='Факультет', max_length=50, choices=(('дневное', 'дневное'), ('вечернее', 'вечернее'),('заочное', 'заочное')), default=('дневное','дневное'))



class Person (models.Model):
    first_name=models.CharField(verbose_name='Имя', max_length=50)
    next_name=models.CharField(verbose_name='Отчество', max_length=50, blank=True)
    last_name=models.CharField(verbose_name='Фамилия', max_length=50)
    nickname=models.CharField(verbose_name='Псевдоним(ы)', max_length=100, blank=True)
    img=models.CharField(verbose_name='Путь к файлу фотографии', max_length=100, blank=True)
    descriptions=models.TextField(verbose_name='Личные качества', blank=True)
    date_of_birth=models.DateField(verbose_name='Дата рождения', blank=True, default='0000-00-00')
    location=models.CharField(verbose_name='Место жительства', max_length=50 , blank=True)
    nationality=models.CharField(verbose_name='Гражданство', max_length=50 , blank=True)
    education=models.CharField(verbose_name='Образование', max_length=50 , blank=True)
    email=models.EmailField(blank=True)

class Skills(models.Model):
    name=models.CharField(verbose_name='Название', max_length=100)
    content=models.TextField(blank=True)

class Hobbies (models.Model):
    name=models.CharField(verbose_name='Название', max_length=100)