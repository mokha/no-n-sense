from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from urllib import unquote

from .models import Classifications

# Create your views here.
def index(request):    
    return render(request, 'index.html', {})


def results(request):    
    return render(request, 'results.html', {})

def statistics(request):    
    return render(request, 'statistics.html', {})

def classify(request):
	if request.GET.get('q'):
		text = request.GET['q']
		text = unquote(text)
		c = Classifications()
		c.classify(text)
		return render(request, 'classify.html', {'text': text, 'rate': c.predicted_rate, 'category': c.predicted_category})
	else:
		return HttpResponseRedirect(reverse('index'))
	

def api(request):
	if request.GET.get('q'):
		text = request.GET['q']
		text = unquote(text)
		c = Classifications()
		c.classify(text)
		return JsonResponse({'Classifications':{'text': text, 'rate': c.predicted_rate, 'category': c.predicted_category}})
	else:
		return JsonResponse({'error':''})