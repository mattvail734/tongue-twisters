import os
import spacy
from spacy import displacy


def tokenize(corpus):
    nlp = spacy.load('en_core_web_md', parse=True, tag=True, entity=True)
    tokenized_corpus = []
    for doc in corpus:
        tokenized_corpus.append(nlp(doc))
    return tokenized_corpus


def dep_tagged_to_html(tokenized_line, file_name):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, file_name)
    dep_tagged_html = displacy.render(tokenized_line, style='dep', minify=True)
    f = open(file_path, 'w')
    f.write(dep_tagged_html)
    f.close()


def dep_tagged_to_svg(tokenized_line, file_name):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, file_name)
    dep_tagged_svg = displacy.render(tokenized_line, style='dep')
    f = open(file_path, 'w')
    f.write(dep_tagged_svg)
    f.close()


def entities_to_html(tokenized_line, file_name):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, file_name)
    entities_html = displacy.render(tokenized_line, style='ent', minify=True)
    f = open(file_path, 'w')
    f.write(entities_html)
    f.close()


def entities_to_svg(tokenized_line, file_name):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, file_name)
    entities_svg = displacy.render(tokenized_line, style='ent')
    f = open(file_path, 'w')
    f.write(entities_svg)
    f.close()
