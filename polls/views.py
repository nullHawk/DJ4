from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View

# Create your views here.
def index(request):
    return render(request , 'polls/index.html')

def funcky(request):
    response=''' Hii '''
    return HttpResponse(response)

def google(request):
    return HttpResponseRedirect("www.google.co.in")

def danger(request,guess):
    response = ''' Your guess was ''' + escape(guess)
    return HttpResponse(response)

class GameView(View):
    def get(self, request):
        context = {'txt' : "<b>bold</b>"}
        return render(request, 'polls/cond.html', context)