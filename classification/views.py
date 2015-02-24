from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from urllib import unquote
from .models import StatisticsForm

from .classifications import Classifications
import amazonproduct, os


aws_api = amazonproduct.API(cfg={
    'access_key': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
    'associate_tag': os.getenv('AWS_ASSOCIATE_TAG'),
    'locale': os.getenv('AWS_LOCALE')
})



# Create your views here.
def index(request):    
    return render(request, 'index.html', {})


def amazon(request): 
	items = aws_api.item_search('Books', Publisher="O'Reilly")

	for book in items:
		print '%s: "%s"' % (book.ItemAttributes.Author, book.ItemAttributes.Title)
	return render(request, 'amazon_results.html', {})

def statistics(request):    
    return render(request, 'statistics.html', {})

def feedback_review(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = StatisticsForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			statistics = form.save(commit=False)
			#statistics.by_user = False
			# save the data 
			statistics.save()
			
			return HttpResponse('Saved')

	return HttpResponseRedirect(reverse('index'))

def classify(request):
	if request.GET.get('review'):
		text = request.GET['review']
		text = unquote(text)
		c = Classifications()

		form = StatisticsForm()
		form.fields['text'].initial = text

		data = {'form': form }
		data.update(c.classify(text))
		return render(request, 'result.html', data )
	else:
		return render(request, 'classify.html')

def api(request):
	if request.GET.get('review'):
		text = request.GET['review']
		text = unquote(text)
		c = Classifications()
		return JsonResponse({'result': c.classify(text) })
	else:
		return JsonResponse({'error':'Kindly use the GET parameter "review" to pass the review text to the classifier. eg: /api?review=nice movie'})