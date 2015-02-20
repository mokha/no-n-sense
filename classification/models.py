from django.db import models
import os, sys;

class Classifications(models.Model):

	_slp_path = os.path.join(os.path.dirname(__file__), "classifiers/category.slp")
	_nb_path = os.path.join(os.path.dirname(__file__), "classifiers/rating.nb")

	text = models.CharField(max_length=65535)
	predicted_category = models.CharField(max_length=5)
	predicted_rate = models.IntegerField()
	#is_positive = models.BooleanField() #not implemented yet

	def __init__(self):
		pass

	def classify(self, text):
		from pattern.vector import NB, SLP, Document

		self.text = text

		slp = SLP.load(Classifications._slp_path)
		self.predicted_category = slp.classify(Document(text))

		nb = NB.load(Classifications._nb_path)
		self.predicted_rate = nb.classify(Document(text))


