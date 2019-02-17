import pandas as pd
import nltk
import spacy


def tag(corpus):
    sentence = str(corpus.iloc[1].news_headline)
    sentence_nlp = nltk.nlp(sentence)
    spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp]
    pd.DataFrame(spacy_pos_tagged, columns=['Word', 'POS tag', 'Tag type'])
    nltk_pos_tagged = nltk.pos_tag(sentence.split())
    pd.DataFrame(nltk_pos_tagged, columns=['Word', 'POS tag'])
