import string
import nltk
from collections import Counter
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.classify import PositiveNaiveBayesClassifier
# nltk.download('movie_reviews')
# nltk.download('stopwords')
# nltk.download('punkt')


# for f in positive_fileids:
#     pos_words = movie_reviews.words(fileids=[f])
#     for word in pos_words:
#         if word not in exclude:
#             word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
#             pos_bag[word] = 'pos'
#
# for f in negative_fileids:
#     neg_words = movie_reviews.words(fileids=[f])
#     for word in neg_words:
#         if word not in exclude:
#             word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
#             neg_bag[word] = 'neg'
#
# split = 800
#
# sentiment_classifier = NaiveBayesClassifier.train(pos_bag[:split] + neg_bag[:split])


exclude = nltk.corpus.stopwords.words("english") + list(string.punctuation)

romeo_text = """Why then, O brawling love! O loving hate!
O any thing, of nothing first create!
O heavy lightness, serious vanity,
Misshapen chaos of well-seeming forms,
Feather of lead, bright smoke, cold fire, sick health,
Still-waking sleep, that is not what it is!
This love feel I, that feel no love in this."""

romeo_text.split()
romeo_words = nltk.word_tokenize(romeo_text)


def build_bag_of_words_features_filtered(words):
    return {word: 1 for word in words if word not in exclude}


print build_bag_of_words_features_filtered(romeo_words)

# sports_sentences = ['The team dominated the game', 'They lost the ball',
# 'The game was intense', 'The goalkeeper catched the ball',
# 'The other team controlled the ball']
#
# various_sentences = ['The President did not comment',
# 'I lost the keys', 'The team won the game', 'Sara has two kids',
# 'The ball went off the court', 'They had the ball for the whole game',
# 'The show is over']
#
#
# def features(sentence):
#     words = sentence.lower().split()
#     return dict(('contains(%s)' % w, True) for w in words)
#
# positive_featuresets = list(map(features, sports_sentences))
# print positive_featuresets
# unlabeled_featuresets = list(map(features, various_sentences))
# classifier = PositiveNaiveBayesClassifier.train(positive_featuresets, unlabeled_featuresets)
# print classifier.classify(features('The cat is on the table'))
# print classifier.classify(features('My team lost the game'))
