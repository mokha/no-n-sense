from django import forms

class FeedbackReviewForm(forms.Form):
	CHOICES = (('1', '',), ('0', '',)) #choices for the feedback

	category = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)
	rate = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)
	rate_nlp = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)
	positivity = forms.ChoiceField(widget=forms.RadioSelect(attrs={'required': 'true'}), choices=CHOICES)