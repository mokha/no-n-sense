from data_helpers import *
from testing_helpers import *
from random import shuffle

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


classifications_file = 'data/classification_data_10.cpickle'
save_pickle(classifications_file, classification_data)
#classification_data = load_pickle(classifications_file)

#class data
# data = []
# data.extend(asDocumentClass(classification_data['musics']['reviews'], 'music'))
# data.extend(asDocumentClass(classification_data['movies']['reviews'], 'movie'))
# data.extend(asDocumentClass(classification_data['games']['reviews'], 'game'))
# shuffle(data)
# normal_test(data, 'Categories')
# kfold_categories(data)
#
#
# #review data
# data = []
# data.extend(asDocumentReview(classification_data['musics']['reviews']))
# data.extend(asDocumentReview(classification_data['movies']['reviews']))
# data.extend(asDocumentReview(classification_data['games']['reviews']))
# shuffle(data)
# normal_test(data, 'Rating')
# kfold_rating(data)

#review data with NLP
# data = []
# data.extend(asDocumentReviewNLP(classification_data['musics']['reviews']))
# data.extend(asDocumentReviewNLP(classification_data['movies']['reviews']))
# data.extend(asDocumentReviewNLP(classification_data['games']['reviews']))
# shuffle(data)
# normal_test(data, 'Rating NLP')
# kfold_ratingNLP(data)
#
# data = []
# data.extend(asDocumentReviewNLP(classification_data['musics']['reviews']))
# data.extend(asDocumentReviewNLP(classification_data['movies']['reviews']))
# data.extend(asSentiment(classification_data['games']['reviews']))
# shuffle(data)
# normal_test(data, 'Rating Sentiment')
# kfold_sentiment(data)





