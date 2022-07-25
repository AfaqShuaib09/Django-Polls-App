''' View.py of Project'''

import random

from django.http import HttpResponse


def hello_world(request):
    ''' Printing Hello World to the page '''
    return HttpResponse("Hello World")


def random_number(request, num):
    ''' Printing a random number to the page '''
    msg = f'Random number between 1 and {num} is {random.randint(1, num)}'
    return HttpResponse(msg)


def home(request):
    ''' Printing a home page to the page '''
    return HttpResponse("<h1>Home Page</h1>")
