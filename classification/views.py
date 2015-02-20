from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):    
    return render(request, 'index.html', {})


def results(request):    
    return render(request, 'results.html', {})

def statistics(request):    
    return render(request, 'statistics.html', {})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
	


def api(request):
	return HttpResponse('Coming Soon!')