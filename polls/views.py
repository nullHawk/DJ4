from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View

# Create your views here.
def index(request):
    response='''
    <html>
        <head>
            <title>Eureka!!!</title>
        </head>
        <body>
            <h1 align='center'> Greetings!</h1>
            <p align='center'> by Suryansh Shakya </p>
        </body>
    </html>
    '''
    return HttpResponse(response)

def funcky(request):
    response=''' Hii '''
    return HttpResponse(response)

def google(request):
    return HttpResponseRedirect("www.google.co.in")

def danger(request,guess):
    response = ''' Your guess was ''' + escape(guess)
    return HttpResponse(response)

class GameView(View):
    def get(self, request, guess):
        x = {'guess':int(guess)}
        return render(request, 'polls/cond.html', x)