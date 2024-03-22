from django.shortcuts import render
from django.http import HttpResponse
from cat_app.models import Student, Pet


def index(request):
    student_list = Student.objects.order_by('last_name')
    pet_list = Pet.objects.order_by('name')

    context_dict = {}
    context_dict['students'] = student_list


    return render(request, 'cat_app/index.html', context=context_dict)

def pets(request):
    pet_list = Pet.objects.order_by('name')

    context_dict = {}
    context_dict['pets'] = pet_list

    return render(request, 'cat_app/pets.html', context=context_dict)