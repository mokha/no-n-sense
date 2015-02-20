from data_helpers import *

#based on the analysis from data processsing

#this file will train the classifiers and save them

#class -> SLP2
#rating -> NB

#amount of data will be used for training
total_data = 50000 #the maximum amount of reviews to get
#the data contains three classes, with reviews
classification_data = {
  'musics' : { #Music reviews (6,396,350 reviews)
    'path': "data/Music.txt.gz",
    'totalReviews': 6396350,
    'reviews': get_data('data/Music.txt.gz', total_data)
  }, 
  'movies': { #Movie & TV reviews (7,850,072 reviews)
    'path': "data/Movies_&_TV.txt.gz",
    'totalReviews': 7850072,
    'reviews': get_data('data/Movies_&_TV.txt.gz', total_data)
  },
  'games': { #Video Game reviews (463,669 reviews)
    'path': "data/Video_Games.txt.gz",
    'totalReviews': 463669,
    'reviews': get_data('data/Video_Games.txt.gz', total_data)
  }
}

#as testing will depend on real new values

from pattern.vector import Document, MAJORITY, MULTINOMIAL, COSINE, LINEAR, CLASSIFICATION
from pattern.vector import NB, KNN, SLP, SVM, kfoldcv
from random import shuffle
import timeit
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))


f = os.path.join(os.path.dirname(__file__), "classifiers/category.slp")
data = []
data.extend(asDocumentClass(classification_data['musics']['reviews'], 'music'))
data.extend(asDocumentClass(classification_data['movies']['reviews'], 'movie'))
data.extend(asDocumentClass(classification_data['games']['reviews'], 'game'))
shuffle(data)

total_data_size = len(data)
training_size = total_data_size
print 'Total Size: ' + str(total_data_size)
print 'Training Size: ' + str(training_size)

#train for category
slp = SLP(train=data[:training_size], baseline=MAJORITY, iterations=2)
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
data = []
#review data
data.extend(asDocumentReview(classification_data['musics']['reviews']))
data.extend(asDocumentReview(classification_data['movies']['reviews']))
data.extend(asDocumentReview(classification_data['games']['reviews']))
shuffle(data)

#train for category
nb = NB(train=data[:training_size], baseline=MAJORITY, method=MULTINOMIAL, alpha=0.0001)
nb.finalize()
#save
nb.save(f, True)
new_nb = NB.load(f)
#test classifying
print new_nb.classify(Document('I would watch this movie again'))
print new_nb.classify(Document('very bad'))
print new_nb.classify(Document('play'))