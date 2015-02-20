from data_helpers import *

#based on the analysis from data processsing

#this file will train the classifiers and save them

#class -> SLP2
#rating -> NB

#all available data will be used for training
classification_data = {
  'music' : { #Music reviews (6,396,350 reviews)
    'path': "data/Music.txt.gz",
    'totalReviews': 6396350,
  }, 
  'movie': { #Movie & TV reviews (7,850,072 reviews)
    'path': "data/Movies_&_TV.txt.gz",
    'totalReviews': 7850072,
  },
  'game': { #Video Game reviews (463,669 reviews)
    'path': "data/Video_Games.txt.gz",
    'totalReviews': 463669,
  }
}

#as testing will depend on real new values

from pattern.vector import Document, MAJORITY, MULTINOMIAL, COSINE, LINEAR, CLASSIFICATION
from pattern.vector import NB, KNN, SLP, SVM, kfoldcv
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))


f = os.path.join(os.path.dirname(__file__), "classifiers/category.slp")
#train for category
slp = SLP(train=[], baseline=MAJORITY, iterations=2)
for c in classification_data.keys():
	for r in parse(classification_data[c]['path']):
		v = Document(r['review/text'], type=str(c), stopwords=True)
		slp.train(v)
slp.finalize()
#save
slp.save(f, True)


#create new classifier
#load
new_slp = SLP.load(f)
#test classifying
print new_slp.classify(Document('I would watch this movie again'))
print new_slp.classify(Document('I would listen to it'))
print new_slp.classify(Document('play'))


#train for rating
f = os.path.join(os.path.dirname(__file__), "classifiers/rating.nb")
#train for category
nb = NB(train=[], baseline=MAJORITY, method=MULTINOMIAL)
for c in classification_data.keys():
	for r in parse(classification_data[c]['path']):
		v = Document(r['review/text'], type=float(r['review/score']), stopwords=True)
		nb.train(v)
nb.finalize()
#save
nb.save(f, True)
new_nb = NB.load(f)
#test classifying
print new_nb.classify(Document('I would watch this movie again'))
print new_nb.classify(Document('I would listen to it'))
print new_nb.classify(Document('play'))