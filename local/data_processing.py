import gzip
import simplejson


def parse(filename):
  '''
  A function to parse the data obtained from Stanford's Amazon reviews
  '''

  f = gzip.open(filename, 'r')
  entry = {}
  for l in f:
    l = l.strip()
    colonPos = l.find(':')
    if colonPos == -1:
      yield entry
      entry = {}
      continue
    eName = l[:colonPos]
    rest = l[colonPos+2:]
    entry[eName] = rest
  yield entry

def get_data(filename, limit=100):
  ''' 
  a function that parses the data file and returns the first rows in a list
  '''
  i = 0
  data = []
  for e in parse(filename):
    if i >= limit:
      break
    data.append(e)
    i += 1
  return data




def asDocumentReview(data):
  '''
  a function that converts list of reviews to Documents to be used by Pattern
  '''
  data = [(r['review/text'], float(r['review/score'])) for r in data]
  data = [Document(review, type=rating, stopwords=True) for review, rating in data]
  return data

def asDocumentClass(data, classification):
  '''
  a function that converts list of reviews to Documents to be used by Pattern
  '''
  data = [(r['review/text'], str(classification)) for r in data]
  data = [Document(review, type=classification, stopwords=True) for review, classification in data]
  return data


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
data.extend(asDocumentClass(classification_data['musics']['reviews'], 'music'))
data.extend(asDocumentClass(classification_data['movies']['reviews'], 'movie'))
data.extend(asDocumentClass(classification_data['games']['reviews'], 'game'))
shuffle(data)


total_data_size = len(data)
training_size = int(round(total_data_size/3))
test_size = training_size

print 'Total Size: ' + str(total_data_size)
print 'Training Size: ' + str(training_size)
print 'Test Size: ' + str(test_size)

print 'Training Started!'
classification_methods = {
  'NB' :  NB(train=data[:training_size], baseline=MAJORITY, method=MULTINOMIAL),
  'KNN2' : KNN(train=data[:training_size], baseline=MAJORITY, k=2, distance=COSINE),
  'KNN3' : KNN(train=data[:training_size], baseline=MAJORITY, k=3, distance=COSINE),
  'KNN4' : KNN(train=data[:training_size], baseline=MAJORITY, k=4, distance=COSINE),
  'KNN5' : KNN(train=data[:training_size], baseline=MAJORITY, k=5, distance=COSINE),
  'KNN6' : KNN(train=data[:training_size], baseline=MAJORITY, k=6, distance=COSINE),
  'KNN7' : KNN(train=data[:training_size], baseline=MAJORITY, k=7, distance=COSINE),
  'KNN8' : KNN(train=data[:training_size], baseline=MAJORITY, k=8, distance=COSINE),
  'KNN9' : KNN(train=data[:training_size], baseline=MAJORITY, k=9, distance=COSINE),
  'KNN10' : KNN(train=data[:training_size], baseline=MAJORITY, k=10, distance=COSINE),
  'SLP1' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=1),
  'SLP2' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=2),
  'SLP3' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=3),
  'SVM' : SVM(train=data[:training_size], type=CLASSIFICATION, kernel=LINEAR),
}

print 'Testing Started!'
#you can shuffle the data
for classification in classification_methods.keys():
  #measure the time it takes to classify!
  start = timeit.default_timer()
  #normal test
  #accuracy, precision, recall, f1 = classification_methods[classification].test(data[training_size:training_size+test_size])
  #test using cross-validation
  accuracy, precision, recall, f1 = kfoldcv(NB, data[:100], folds=10)
  stop = timeit.default_timer()
  print '*' + classification + '*'
  print 'Accuracy: ' + str(accuracy)
  print 'Precision: ' + str(precision)
  print 'Recall: ' + str(recall)
  print 'F1-score: ' + str(f1)
  print 'Time: ' + str(stop - start)
  print