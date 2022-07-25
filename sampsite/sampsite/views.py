''' View.py of Project'''

import random

from django.shortcuts import render

def home(request):
    ''' Printing a home page to the page '''
    return render(request, 'polls/home.html')
