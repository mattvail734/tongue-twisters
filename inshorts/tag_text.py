import spacy
import nltk

# to tag using Spacy; first download the en_core language model
# python3 -m spacy download en_core_web_md

nlp = spacy.load('en_core_web_md', parse=True, tag=True, entity=True)


# corpus is a Panda Series; each element is a single set of words
# ouput is a Panda Series; each element is a single set of tuples
# using Spacy - each tuple is a threesome (word, POS tag, Tag type)
# using NLTK - each tuple is a pair (word, POS tag)
def tag_text(corpus, model='spacy'):
    if (model == 'spacy'):
        tagged_corpus = []
        for line in corpus:
            line_nlp = nlp(line)
            tagged_line = []
            for word in line_nlp:
                tagged_line.append(tuple([word, word.tag_, word.pos_]))
            tagged_corpus.append(tagged_line)
    if (model == 'nltk'):
        tagged_corpus = []
        for line in corpus:
            nltk_pos_tagged = nltk.pos_tag(line.split())
            tagged_corpus.append(nltk_pos_tagged)
    return tagged_corpus
