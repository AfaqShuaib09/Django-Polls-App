''' Funtion based views of project sampsite '''

from django.shortcuts import render

def home(request):
    ''' Display the start app buttom on home page to start the app '''
    return render(request, 'polls/home.html')
