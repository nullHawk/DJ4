from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return render(request,'polls/index.html')
    http_file='''
    <html>
        <head>
            <title>Eureka!!!</title>
        </head>
        <body>
            <h1 align='center'> Greetings Papa!</h1>
            <p align='center'> by Suryansh Shakya </p>
        </body>
    </html>
    '''
    return HttpResponse(http_file)