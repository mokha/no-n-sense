from pattern.vector import NB, SLP, Document
import os, sys;

class Classifications():

	#static variables
	_slp_path = os.path.join(os.path.dirname(__file__), "classifiers/category.slp")
	_nb_path = os.path.join(os.path.dirname(__file__), "classifiers/rating.nb")
	_nb = NB.load(_nb_path)
	_slp = SLP.load(_slp_path)

	@staticmethod
	def classify(text):
		predicted_category = Classifications._slp.classify(Document(text), discrete=True)
		predicted_rate = Classifications._nb.classify(Document(text), discrete=True)

		return {'text': text, 'rate': predicted_rate, 'category': predicted_category}