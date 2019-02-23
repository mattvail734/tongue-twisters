# inshorts analysis

[inshorts](https://inshorts.com/) is a website that provides 60-word articles on current affairs. 

## Summary

This project:

1. Downloads all stories from the inshorts website using [requests](http://docs.python-requests.org/en/master/)
2. Parses the HTML using [Beautify Soup](https://www.crummy.com/software/BeautifulSoup/)
3. Stores the stories in a [Pandas](https://pandas.pydata.org/pandas-docs/stable/)
4. Normalizes, [stems](https://en.wikipedia.org/wiki/Stemming), and [lemmatizes](https://en.wikipedia.org/wiki/Lemmatisation) the text using [NLTK](https://www.nltk.org/) and [SpaCy](https://spacy.io/)
5. Tags the [parts of speech](https://en.wikipedia.org/wiki/Part_of_speech) (POS) using the [Penn Treebank Notation](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/Penn-Treebank-Tagset.pdf) via SpaCy
6. [Chunks](https://en.wikipedia.org/wiki/Shallow_parsing) (shallow parsing) the text using the [CONL2000](https://www.clips.uantwerpen.be/conll2000/chunking/) via NLTK
7. [Constituency parses](https://en.wikipedia.org/wiki/Parse_tree#Constituency-based_parse_trees) the text using the [Stanford Parser](https://nlp.stanford.edu/software/lex-parser.shtml) also via NLTK
8. [Dependency parses](https://en.wikipedia.org/wiki/Parse_tree#Dependency-based_parse_trees) the text using the [Universal Dependencies Scheme](https://universaldependencies.org/u/dep/index.html) via SpaCy
9. [Identifies named entities](https://en.wikipedia.org/wiki/Named-entity_recognition) using SpaCy
10. [Analyzes the sentiment](https://en.wikipedia.org/wiki/Sentiment_analysis) using the [Afinn](https://github.com/fnielsen/afinn) lexicon
