from django.db import models
from django.forms import ModelForm
from django import forms

#how accurate is the prediction
CHOICES = ((1, '',), (0, '',)) #choices for the feedback
#1 means positive, 0 means negative

class Statistics(models.Model):
	text = models.CharField(max_length=65535, unique=True, default='')
	category = models.BooleanField(choices=CHOICES, default=True)
	rate = models.BooleanField(choices=CHOICES, default=True)
	rate_nlp = models.BooleanField(choices=CHOICES, default=True)
	positivity = models.BooleanField(choices=CHOICES, default=True)

	#by (user|amazon_reviews)
	by_user = models.BooleanField(default=True)
	

class StatisticsForm(ModelForm):
	category = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)
	rate = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)
	rate_nlp = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)
	positivity = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)
	text = forms.CharField(max_length=65535, widget=forms.HiddenInput())

	class Meta:
		model = Statistics
		#widgets = {'text': forms.HiddenInput()}
		fields = ['text', 'category', 'rate', 'rate_nlp', 'positivity']