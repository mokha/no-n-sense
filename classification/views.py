from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Classifications

# Create your views here.
def index(request):    
    return render(request, 'index.html', {})


def results(request):    
    return render(request, 'results.html', {})

def statistics(request):    
    return render(request, 'statistics.html', {})

def classify(request):
	import urllib

	if request.GET.get('q'):
		text = request.GET['q']
		text = urllib.unquote(text)
		c = Classifications()
		c.classify(text)
		message = 'You submitted: %r, %r' % (c.predicted_category, c.predicted_rate)
		return HttpResponse(message)
	else:
		return HttpResponseRedirect(reverse('index'))
	


def db(request):
	pass
    # greeting = Greeting()
    # greeting.save()

    # greetings = Greeting.objects.all()

    # return render(request, 'db.html', {'greetings': greetings})
	


def api(request):
	return HttpResponse('Coming Soon!')