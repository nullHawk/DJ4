from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Page(TemplateView):
    template_name = "secret_santa/index.html"
    def get(self, request, *args, **kwargs):
        # Your GET request handling logic here
        names = ['John', 'Paul', 'George', 'Ringo']
        context={'names':names}
        return render(request, self.template_name, context)
        
    def post(self, request):
        context = self.template_name

        # Generating random user
        
        names = ['John', 'Paul', 'George', 'Ringo']
        context={'names':names}
        return render(request, self.template_name, context)
