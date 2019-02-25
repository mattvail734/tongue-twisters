import spacy


# corpus is a Panda Series; each element is a single set of words
# ouput is a Panda Series; each element is a single set of tuples
# using Spacy - each tuple is a threesome (word, POS tag, Tag type)
# using NLTK - each tuple is a pair (word, POS tag)
def POS_tag_text(corpus):
    nlp = spacy.load('en_core_web_md', parse=True, tag=True, entity=True)
    tagged_corpus = []
    for line in corpus:
        line_nlp = nlp(line)
        tagged_line = []
        for word in line_nlp:
            tagged_line.append(tuple([word, word.tag_, word.pos_]))
        tagged_corpus.append(tagged_line)
    return tagged_corpus


def chunk_text(corpus):
    # NEED TO COMPLETE THIS METHOD
    chunked_corpus = corpus
    return chunked_corpus


def con_tag_text(corpus):
    # NEED TO COMPLETE THIS METHOD
    con_tagged_corpus = corpus
    return con_tagged_corpus


def dep_tag_text(corpus):
    # NEED TO COMPLETE THIS METHOD
    dep_tagged_corpus = corpus
    return dep_tagged_corpus
