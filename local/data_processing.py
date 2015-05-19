from data_helpers import *
from testing_helpers import *
from random import shuffle

total_data = 5000 #the maximum amount of reviews to get
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


#class data
data = []
data.extend(asDocumentClass(classification_data['musics']['reviews'], 'music'))
data.extend(asDocumentClass(classification_data['movies']['reviews'], 'movie'))
data.extend(asDocumentClass(classification_data['games']['reviews'], 'game'))
shuffle(data)
test(data, 'Categories')


#review data
data = []
data.extend(asDocumentReview(classification_data['musics']['reviews']))
data.extend(asDocumentReview(classification_data['movies']['reviews']))
data.extend(asDocumentReview(classification_data['games']['reviews']))
shuffle(data)
test(data, 'Rating')

#review data with NLP
data = []
data.extend(asDocumentReviewNLP(classification_data['musics']['reviews']))
data.extend(asDocumentReviewNLP(classification_data['movies']['reviews']))
data.extend(asDocumentReviewNLP(classification_data['games']['reviews']))
shuffle(data)
test(data, 'Rating NLP')

data = []
data.extend(asDocumentReviewNLP(classification_data['musics']['reviews']))
data.extend(asDocumentReviewNLP(classification_data['movies']['reviews']))
data.extend(asSentiment(classification_data['games']['reviews']))
shuffle(data)
test(data, 'Rating Sentiment')
