from django.db import models
from pattern.vector import NB, SLP, Document
import os, sys;

class Classifications(models.Model):

	#static variables
	_slp_path = os.path.join(os.path.dirname(__file__), "classifiers/category.slp")
	_nb_path = os.path.join(os.path.dirname(__file__), "classifiers/rating.nb")
	_nb = NB.load(_nb_path)
	_slp = SLP.load(_slp_path)



	text = models.CharField(max_length=65535)
	predicted_category = models.CharField(max_length=5)
	predicted_rate = models.IntegerField()
	is_positive = models.BooleanField()

	def __init__(self):
		pass

	def classify(self, text):
		self.text = text
		self.predicted_category = Classifications._slp.classify(Document(text))
		self.predicted_rate = Classifications._nb.classify(Document(text))



class Statistics(models.Model):

	#predicted

	#category
	#rate
	#positivity

	is_category_accurate = models.BooleanField()
	is_rate_accurate = models.BooleanField()
	is_positivity_accurate = models.NullBooleanField()


	#by (user|amazon_reviews)
	by_user = models.BooleanField()

	pass

