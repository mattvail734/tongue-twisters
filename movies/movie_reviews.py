import string
import nltk
import unicodedata
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
# nltk.download('movie_reviews')
# nltk.download('stopwords')

exclude = nltk.corpus.stopwords.words("english") + list(string.punctuation)
positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')


def build_bag(words):
    word_dict = {}
    for word in words:
        if word not in exclude:
            word = unicodedata.normalize(
                'NFKD', word).encode('ascii', 'ignore')
            word_dict[word] = 1
    return word_dict


pos_bag = []
for f in positive_fileids:
    pos_bag.append((build_bag(movie_reviews.words(fileids=[f])), 'pos'))

neg_bag = []
for f in negative_fileids:
    neg_bag.append((build_bag(movie_reviews.words(fileids=[f])), 'neg'))

split = 800
sentiment_classifier = NaiveBayesClassifier.train(
    pos_bag[:split] + neg_bag[:split])

train_accuracy = nltk.classify.util.accuracy(
    sentiment_classifier, pos_bag[:split] + neg_bag[:split])*100

test_accuracy = nltk.classify.util.accuracy(
    sentiment_classifier, pos_bag[split:] + neg_bag[split:])*100

print "Accuracy on the training set: " + str(train_accuracy) + "%"
print "Accuracy on the test set: " + str(test_accuracy) + "%"

most_informative = sentiment_classifier.show_most_informative_features()
