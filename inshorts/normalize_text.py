import spacy
import nltk
import unicodedata
import re
from nltk.tokenize.toktok import ToktokTokenizer
from bs4 import BeautifulSoup
from contractions import CONTRACTION_MAP

# to tag using Spacy; first download the en_core language model
# python3 -m spacy download en_core_web_md

nlp = spacy.load('en_core_web_md', parse=True, tag=True, entity=True)
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
stopword_list.remove('no')
stopword_list.remove('not')


# text is a single set of words NOT an iterable
def strip_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    stripped_text = soup.get_text()
    return stripped_text


# text is a single set of words NOT an iterable
def remove_accented_chars(text):
    text = unicodedata.normalize(
        'NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text


# text is a single set of words NOT an iterable
def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):
    contractions_pattern = re.compile('({})'.format('|'.join(
        contraction_mapping.keys())), flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
            if contraction_mapping.get(match)\
            else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text


# text is a single set of words NOT an iterable
def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text


# text is a single set of words NOT an iterable
def simple_stemmer(text):
    ps = nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text


# text is a single set of words NOT an iterable
def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text


# text is a single set of words NOT an iterable
def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


# corpus is a Panda series; each element is a single set of words
def normalize(
        corpus, html_stripping=True, contraction_expansion=True,
        accented_char_removal=True, text_lower_case=True, text_lemmatization=True,
        special_char_removal=True, stopword_removal=True, remove_digits=True):

        normalized_text = []
        # normalize each document in the corpus
        for doc in corpus:
            # strip html
            if html_stripping:
                doc = strip_html_tags(doc)
            # expand contractions
            if contraction_expansion:
                doc = expand_contractions(doc)
            # remove accented characters
            if accented_char_removal:
                doc = remove_accented_chars(doc)
            # lowercase the text
            if text_lower_case:
                doc = doc.lower()
            # remove extra newlines
            doc = re.sub(r'[\r|\n|\r\n]+', ' ', doc)
            # lemmatize the text
            if text_lemmatization:
                doc = lemmatize_text(doc)
            # remove special characters and/or digits
            if special_char_removal:
                # insert spaces between special characters
                special_char_pattern = re.compile(r'([{.(-)}])')
                doc = special_char_pattern.sub(' \\1 ', doc)
                doc = remove_special_characters(doc, remove_digits=remove_digits)
            # remove extra whitespace
            doc = re.sub(' +', ' ', doc)
            # remove stopword
            if stopword_removal:
                doc = remove_stopwords(doc, is_lower_case=text_lower_case)
            # tag the text with parts of speech using Spacy english language model

            normalized_text.append(doc)

        return normalized_text
