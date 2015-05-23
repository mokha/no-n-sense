from pattern.vector import NB, SLP, SVM, Document, count
from pattern.en import parsetree
import os, sys, operator

class Classifications():

	#static variables
    _category_path = os.path.join(os.path.dirname(__file__), "classifiers/category.slp")
    _rating_path = os.path.join(os.path.dirname(__file__), "classifiers/rating.slp")
    _rating_nlp_path = os.path.join(os.path.dirname(__file__), "classifiers/rating_nlp.svm")
    _sentiment_path = os.path.join(os.path.dirname(__file__), "classifiers/sentiment.nb")

    _category = SLP.load(_category_path)
    _rating = SLP.load(_rating_path)
    _rating_nlp = SVM.load(_rating_nlp_path)
    _sentiment = NB.load(_sentiment_path)

    @staticmethod
    def selectWords(review):
        '''
        a function that gets a review and selects the nouns, adjectives, verbs and exclamation mark
        '''
        review = parsetree(review, lemmata=True)[0] #lemmatize the review
        #select adjectives (JJ), nouns (NN), verbs (VB) and exclamation marks
        review = [w.lemma for w in review if w.tag.startswith(('JJ', 'NN', 'VB', '!'))]
        review = count(review) #a dictionary of (word, count)
        return review

    @staticmethod
    def classify(text):
        predicted_category = Classifications._category.classify(Document(text), discrete=True)
        predicted_rate = Classifications._rating.classify(Document(text), discrete=True)
        predicted_rate_nlp = Classifications._rating_nlp.classify(Classifications.selectWords(text), discrete=True)
        predicted_sentiment_dict = Classifications._sentiment.classify(Classifications.selectWords(text), discrete=False)
        predicted_sentiment = True if str(sorted(predicted_sentiment_dict.items(), key=operator.itemgetter(1), reverse=True)[1][0]) in ['True', '3.0', '4.0', '5.0'] else False

        return {
        'text': text,
        'rate': predicted_rate,
        'category': predicted_category,
        'rate_nlp': predicted_rate_nlp,
        'positivity': predicted_sentiment
        }