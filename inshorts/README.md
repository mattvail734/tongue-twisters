# inshorts analysis

[inshorts](https://inshorts.com/) is a website that provides 60-word articles on current affairs. 

## Summary

This project:

1. Downloads all stories from the inshorts website using [requests](http://docs.python-requests.org/en/master/)
2. Parses the HTML using [Beautify Soup](https://www.crummy.com/software/BeautifulSoup/)
3. Stores the stories in a [Pandas](https://pandas.pydata.org/pandas-docs/stable/)
4. Normalizes, [stems](https://en.wikipedia.org/wiki/Stemming), and [lemmatizes](https://en.wikipedia.org/wiki/Lemmatisation) the text using [NLTK](https://www.nltk.org/) and [SpaCy](https://spacy.io/)
5. Tags the [parts of speech](https://en.wikipedia.org/wiki/Part_of_speech) (POS) using the [Penn Treebank Notation](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/Penn-Treebank-Tagset.pdf) also via SpaCy
6: Chunks 
7: Parses
