from data_helpers import *

total_data = 10000 #the maximum amount of reviews to get
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


from pattern.vector import Document, MAJORITY, MULTINOMIAL, COSINE, LINEAR, CLASSIFICATION
from pattern.vector import NB, KNN, SLP, SVM, kfoldcv
from random import shuffle
import timeit


#combine all data
data = []

#class data
# data.extend(asDocumentClass(classification_data['musics']['reviews'], 'music'))
# data.extend(asDocumentClass(classification_data['movies']['reviews'], 'movie'))
# data.extend(asDocumentClass(classification_data['games']['reviews'], 'game'))

#review data
# data.extend(asDocumentReview(classification_data['musics']['reviews']))
# data.extend(asDocumentReview(classification_data['movies']['reviews']))
# data.extend(asDocumentReview(classification_data['games']['reviews']))

shuffle(data)


total_data_size = len(data)
training_size = int(round(total_data_size/3))
test_size = training_size

print 'Total Size: ' + str(total_data_size)
print 'Training Size: ' + str(training_size)
print 'Test Size: ' + str(test_size)

print 'Training Started!'
classification_methods = {
  #uncomment based on what classification algorithm you would like to test
  
  # 'NB' :  NB(train=data[:training_size], baseline=MAJORITY, method=MULTINOMIAL),
  # 'KNN2' : KNN(train=data[:training_size], baseline=MAJORITY, k=2, distance=COSINE),
  # 'KNN3' : KNN(train=data[:training_size], baseline=MAJORITY, k=3, distance=COSINE),
  # 'KNN4' : KNN(train=data[:training_size], baseline=MAJORITY, k=4, distance=COSINE),
  # 'KNN5' : KNN(train=data[:training_size], baseline=MAJORITY, k=5, distance=COSINE),
  # 'KNN6' : KNN(train=data[:training_size], baseline=MAJORITY, k=6, distance=COSINE),
  # 'KNN7' : KNN(train=data[:training_size], baseline=MAJORITY, k=7, distance=COSINE),
  # 'KNN8' : KNN(train=data[:training_size], baseline=MAJORITY, k=8, distance=COSINE),
  # 'KNN9' : KNN(train=data[:training_size], baseline=MAJORITY, k=9, distance=COSINE),
  # 'KNN10' : KNN(train=data[:training_size], baseline=MAJORITY, k=10, distance=COSINE),
  # 'SLP1' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=1),
  # 'SLP2' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=2),
  # 'SLP3' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=3),
  # 'SVM' : SVM(train=data[:training_size], type=CLASSIFICATION, kernel=LINEAR),
}

print 'Testing Started!'

# uncomment to start the normal test
# for classification in classification_methods.keys():
#   #measure the time it takes to classify!
#   start = timeit.default_timer()
#   #normal test
#   accuracy, precision, recall, f1 = classification_methods[classification].test(data[training_size:training_size+test_size])
#   stop = timeit.default_timer()
#   print '*' + classification + '*'
#   print 'Accuracy: ' + str(accuracy)
#   print 'Precision: ' + str(precision)
#   print 'Recall: ' + str(recall)
#   print 'F1-score: ' + str(f1)
#   print 'Time: ' + str(stop - start)
#   print
  

#uncomment to test using cross-validation
# start = timeit.default_timer()
# accuracy, precision, recall, f1, stdev = kfoldcv(NB, data, folds=10, method=MULTINOMIAL)
# stop = timeit.default_timer()
# print '*NB*'
# print 'Accuracy: ' + str(accuracy)
# print 'Precision: ' + str(precision)
# print 'Recall: ' + str(recall)
# print 'F1-score: ' + str(f1)
# print 'STDev: ' + str(stdev)
# print 'Time: ' + str(stop - start)
# print

# start = timeit.default_timer()
# accuracy, precision, recall, f1, stdev = kfoldcv(SLP, data, folds=10, iterations=1)
# stop = timeit.default_timer()
# print '*SLP1*'
# print 'Accuracy: ' + str(accuracy)
# print 'Precision: ' + str(precision)
# print 'Recall: ' + str(recall)
# print 'F1-score: ' + str(f1)
# print 'STDev: ' + str(stdev)
# print 'Time: ' + str(stop - start)
# print

# start = timeit.default_timer()
# accuracy, precision, recall, f1, stdev = kfoldcv(SLP, data, folds=10, iterations=2)
# stop = timeit.default_timer()
# print '*SLP2*'
# print 'Accuracy: ' + str(accuracy)
# print 'Precision: ' + str(precision)
# print 'Recall: ' + str(recall)
# print 'F1-score: ' + str(f1)
# print 'STDev: ' + str(stdev)
# print 'Time: ' + str(stop - start)
# print

# start = timeit.default_timer()
# accuracy, precision, recall, f1, stdev = kfoldcv(SLP, data, folds=10, iterations=3)
# stop = timeit.default_timer()
# print '*SLP3*'
# print 'Accuracy: ' + str(accuracy)
# print 'Precision: ' + str(precision)
# print 'Recall: ' + str(recall)
# print 'F1-score: ' + str(f1)
# print 'STDev: ' + str(stdev)
# print 'Time: ' + str(stop - start)
# print