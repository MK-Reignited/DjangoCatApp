from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage': '[List of students and their cats go here]'}

    return render(request, 'cat_app/index.html', context=context_dict)

def pets(request):

    context_dict = {'boldmessage': '[List of all cats go here]'}

    return render(request, 'cat_app/pets.html', context=context_dict)