import gzip
import simplejson
from pattern.vector import Document, count
from pattern.en import parsetree

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
        rest = l[colonPos + 2:]
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


def selectWords(review):

    '''
    a function that gets a review and selects the nouns, adjectives, verbs and exclamation mark
    '''
    review = parsetree(review, lemmata=True)[0] #lemmatize the review
    #select adjectives (JJ), nouns (NN), verbs (VB) and exclamation marks
    review = [w.lemma for w in review if w.tag.startswith(('JJ', 'NN', 'VB', '!'))]
    review = count(review) #a dictionary of (word, count)
    return review


def scoreToBool(score):
    '''
    convert the score to true >=3 else false
    '''
    return

def asDocumentReviewNLP(data):
    '''
    a function that converts list of reviews to Documents to be used by Pattern
    '''
    data = [(selectWords(r['review/text']), float(r['review/score'])) for r in data]
    return data

def asSentiment(data):
    '''
    a function that converts list of reviews to Documents to be used by Pattern
    '''
    data = [(selectWords(r['review/text']), float(r['review/score']) >= 3) for r in data]
    return data