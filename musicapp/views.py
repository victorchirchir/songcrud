from django.shortcuts import render
from django.http import HttpResponse
from pipes import Template
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse('Welcome to my Music App')

class HomePageView(TemplateView):
    template_name='index.html'

