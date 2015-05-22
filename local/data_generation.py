from data_helpers import *
from pattern.vector import Document, MAJORITY, MULTINOMIAL, COSINE, LINEAR, CLASSIFICATION
from pattern.vector import POLYNOMIAL
from pattern.vector import NB, KNN, SLP, SVM, kfoldcv
from random import shuffle
import timeit
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

#based on the analysis from data processsing

#this file will train the classifiers and save them

#class -> SLP3
#rating -> SLP3
#rating_nlp -> svm
#sentiment -> NB

#amount of data will be used for training
total_data = 100000 #the maximum amount of reviews to get
#the data contains three classes, with reviews
# classification_data = {
#   'musics' : { #Music reviews (6,396,350 reviews)
#     'path': "data/Music.txt.gz",
#     'totalReviews': 6396350,
#     'reviews': get_data('data/Music.txt.gz', total_data)
#   }, 
#   'movies': { #Movie & TV reviews (7,850,072 reviews)
#     'path': "data/Movies_&_TV.txt.gz",
#     'totalReviews': 7850072,
#     'reviews': get_data('data/Movies_&_TV.txt.gz', total_data)
#   },
#   'games': { #Video Game reviews (463,669 reviews)
#     'path': "data/Video_Games.txt.gz",
#     'totalReviews': 463669,
#     'reviews': get_data('data/Video_Games.txt.gz', total_data)
#   }
# }

classifications_file = 'data/classification_data.cpickle'
# save_pickle(classifications_file, classification_data)
classification_data = load_pickle(classifications_file)
#as testing will depend on real new values


# f = os.path.join(os.path.dirname(__file__), "classifiers/category.slp")
# data = []
# data.extend(asDocumentClass(classification_data['musics']['reviews'], 'music'))
# data.extend(asDocumentClass(classification_data['movies']['reviews'], 'movie'))
# data.extend(asDocumentClass(classification_data['games']['reviews'], 'game'))
# shuffle(data)
# #train for category
# slp = SLP(train=data[:len(data)], baseline=MAJORITY, iterations=3)
# slp.finalize()
# #save
# slp.save(f, True)

# print '--------------------'
# #train for rating
# f = os.path.join(os.path.dirname(__file__), "classifiers/rating.slp")
# data = []
# #review data
# data.extend(asDocumentReview(classification_data['musics']['reviews']))
# data.extend(asDocumentReview(classification_data['movies']['reviews']))
# data.extend(asDocumentReview(classification_data['games']['reviews']))
# shuffle(data)

# #train for category
# slp = SLP(train=data[:len(data)], baseline=MAJORITY, iterations=3)
# slp.finalize()
# #save
# slp.save(f, True)

# print '--------------------'
# #training for rating rating_nlp
f = os.path.join(os.path.dirname(__file__), "classifiers/rating_nlp.svm")
data = []
data.extend(asDocumentReviewNLP(classification_data['musics']['reviews']))
data.extend(asDocumentReviewNLP(classification_data['movies']['reviews']))
data.extend(asDocumentReviewNLP(classification_data['games']['reviews']))
shuffle(data)
svm = SVM(train=data[:len(data)], type=CLASSIFICATION, kernel=POLYNOMIAL)
svm.finalize()
#save
svm.save(f, True)

# print '--------------------'
# #training for sentiment 
# f = os.path.join(os.path.dirname(__file__), "classifiers/sentiment.nb")
# data = []
# data.extend(asDocumentReviewNLP(classification_data['musics']['reviews']))
# data.extend(asDocumentReviewNLP(classification_data['movies']['reviews']))
# data.extend(asSentiment(classification_data['games']['reviews']))
# shuffle(data)
# nb = NB(train=data[:len(data)], baseline=MAJORITY, method=MULTINOMIAL, alpha=0.0001)
# nb.finalize()
# #save
# nb.save(f, True)
