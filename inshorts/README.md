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

inshorts.py is driver program for the application. 

## Data Retrieval and HTML Parsing
get_news.py leverages requests to retrieve the news from inshorts. Retrieval is done by the build_dataset method. Given a set of urls, build_dataset downloads all html from those urls. After downloading the HTML, we create a BeautifulSoup object and use that to parse the html for news headlines, articles, and categories. Then, we store these three series in a Pandas dataframe and again utilize BeautifulSoup to remove html tags.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>news_headline</th>
      <th>news_article</th>
      <th>news_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Miss him today, every day: Apple CEO on Steve ...</td>
      <td>Remembering late Apple Co-founder Steve Jobs o...</td>
      <td>technology</td>
    </tr>
    <tr>
      <th>1</th>
      <td>End $479 mn US Army contract: Microsoft employ...</td>
      <td>Over 100 Microsoft workers have written to CEO...</td>
      <td>technology</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Year-long emergency declared in Sudan amid ant...</td>
      <td>Sudan's President Omar al-Bashir has declared ...</td>
      <td>world</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Drug lord Pablo Escobar's former home demolish...</td>
      <td>Colombian authorities on Friday demolished the...</td>
      <td>world</td>
    </tr>
  </tbody>
</table>

## Normalizing



## Tagging



## Language Parsing



## Named Entity Identification



## Sentiment Analysis
[Afinn Paper](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6006/pdf/imm6006.pdf)

