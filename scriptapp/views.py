from django.shortcuts import render
from mainapp.models import *


# Create your views here.
def ins(request):

    input=open('input.txt', 'r', encoding='utf-8')
    file=input.read()
    file=file.split('\n')
    separator=file[1]
    fields=file[2].split(',')
    input.close()
    message=""



    for string_ent in file[3:]:
        obj_inst=HighEducation()#hard-code!!
        string_array=string_ent.split(separator)
        for index, fieldname in enumerate(fields):
            obj_inst.__dict__[fieldname]=string_array[index]

        obj_inst.full_clean()
        obj_inst.save()
    return render(request,'script.html', {'message':message})

   # job.employer=job_ent['employer']
        # job.position=job_ent['position']
        # job.date_from=job_ent['date_from']
        # job.date_to=job_ent['date_to']