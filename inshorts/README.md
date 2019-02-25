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
normalize_text.py takes the news dataframe and does the following pre-processing:

1. removes all accented characters (aprés-ski => apres-ski) using the standard Python unicodedata library
2. expands contractions (can't => cannot) using a standard set of contractions available [here](https://github.com/polymathnexus5/tongue-twisters/blob/master/inshorts/contractions.py)
3. removes all special characters (Wow! so crazy 13?%$!! => Wow so crazy) using the nltk.porter.PorterStemmer() class
4. removes all stopwords using a NLTK tokenizer and the built in NLTK stopwords corpus
5. converts the text to lowercase

normalize_text.py also provides methods to:
6. stems the text (run, ran, running, runs, runner => run "the root stem"); stemming is done according to an algorithm that does NOT guarantee that the resulting root will be semantically correct or even in the dictionary (i.e. daily stems to daili using the NLTK Porter stemmer)
7. lemmatize the text; lemmatization is very similar to stemming except that in lemmatization the resulting word is always in the dictionary. The resulting word is called the "lemma"

You should either stem or lemmatize but not both.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>full_text</th>
      <th>normalized_text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Twitter CEO to not attend parliament panel mee...</td>
      <td>twitter ceo not attend parliament panel meet m...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PETA criticises Google Doodle on Steve Irwin, ...</td>
      <td>peta criticise google doodle steve irwin face ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Vietnam threatens to deport Trump, Kim Jong-un...</td>
      <td>vietnam threaten deport trump kim jong un impe...</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Drug lord Pablo Escobar's former home demolish...</td>
      <td>drug lord pablo escobar former home demolish c...</td>
    </tr>
  </tbody>
</table>

## Tagging
tag_text.py uses SpaCy to tag each word with its corresponding part of speech (POS). SpaCy has several models covering many languages; here we use the standard English 'en_core_web_md' 2.0.0 language model (found [here](https://github.com/explosion/spacy-models/releases/tag/en_core_web_md-2.0.0) with info [here](https://spacy.io/models/).

Details on how SpaCy tags can be found [here](https://spacy.io/api/annotation#section-pos-tagging).
"The English part-of-speech tagger uses the [OntoNotes 5](https://catalog.ldc.upenn.edu/LDC2013T19) version of the Penn Treebank tag set. We also map the tags to the simpler Google Universal POS tag set."

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>normalized_text</th>
      <th>POS_tagged_text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>adobe fix bug damage macbook pro speaker adobe...</td>
      <td>[(adobe, NNP, PROPN), (fix, VB, VERB), (bug, N...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>end mn us army contract microsoft employee ceo...</td>
      <td>[(end, VB, VERB), (mn, IN, ADP), (us, PRP, PRO...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>kill injure china mine accident least people k...</td>
      <td>[(kill, VB, VERB), (injure, NN, NOUN), (china,...</td>
    </tr>
    <tr>
      <th>74</th>
      <td>saudi arabia look make india regional hub oil ...</td>
      <td>[(saudi, JJ, ADJ), (arabia, NNS, NOUN), (look,...</td>
    </tr>
  </tbody>
</table>

## Language Parsing
chunk_text.py takes each word and "chunks" or groups them into phrases. There are five major categories of phrases:
1. Noun phrase
2. Verb phrase
3. Adjective phrase
4. Adverb phrase
5. Prepositional phrase


## Named Entity Identification
entity_recognition.py uses the built in SpaCy named entity recognition to identify named entities throughout the news articles. It then groups entities, counts occurrences, and sorts them by most frequent.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Type</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>india</td>
      <td>GPE</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pakistan</td>
      <td>GPE</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>first</td>
      <td>ORDINAL</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>year</td>
      <td>DATE</td>
      <td>9</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>83</th>
      <td>korea</td>
      <td>GPE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>84</th>
      <td>kim</td>
      <td>PERSON</td>
      <td>1</td>
    </tr>
    <tr>
      <th>85</th>
      <td>july</td>
      <td>DATE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>86</th>
      <td>afghanistan</td>
      <td>GPE</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

<div class="entities" style="line-height: 2.5">Twitter given 
<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    10 days
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>
</mark>
 to reply to parliament panel questions. 
<mark class="entity" style="background: #7aecec; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    The Parliamentary Committee on Information Technology
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">ORG</span>
</mark>
 on 
<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    Monday
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>
</mark>
 granted 
<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    10 days
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>
</mark>
 to Twitter CEO 
<mark class="entity" style="background: #aa9cfc; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    Jack Dorsey
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">PERSON</span>
</mark>
 to respond in writing to questions that remained unanswered. The committee had summoned 
<mark class="entity" style="background: #aa9cfc; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    Dorsey
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">PERSON</span>
</mark>
 on 
<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    February 11
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>
</mark>
 to question him on "safeguarding citizen rights on social/online media platforms". It also allowed 
<mark class="entity" style="background: #bfeeb7; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    Twitter VP
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">PRODUCT</span>
</mark>
 and 
<mark class="entity" style="background: #7aecec; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    Global Policy Head
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">ORG</span>
</mark>
 
<mark class="entity" style="background: #aa9cfc; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    Colin Crowell
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">PERSON</span>
</mark>
 to appear before the panel.</div>

## Sentiment Analysis
sentiment.py uses the Afinn Lexicon to assign a sentiment score to each article. Afinn works with a corpus of roughly 2,477 unique words built from Twitter posts and manually labeled on a scale from -5 (most negative) to +5 (most positive) with 0 being a neutral word. The sentiment score of an article is then computed using the average polarity of the words (sum of all polarity scores in the article divided by the total number of words).

details on the Afinn model and results are [here](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6006/pdf/imm6006.pdf)

<p align="left">
  <img src="https://github.com/polymathnexus5/tongue-twisters/blob/master/inshorts/Sentiment_Histogram.png" alt="Histogram" height="500" width="500" style="float:right">
</p>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>news_headline</th>
      <th>news_category</th>
      <th>sentiment_score</th>
      <th>sentiment_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BJP MP-led panel summons officials of Facebook...</td>
      <td>technology</td>
      <td>0.0</td>
      <td>neutral</td>
    </tr>
    <tr>
      <th>1</th>
      <td>We are very aware of iPhone pricing concerns: ...</td>
      <td>technology</td>
      <td>0.0</td>
      <td>neutral</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Saudi Arabia looking to make India regional hu...</td>
      <td>world</td>
      <td>5.0</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Trump calls on OPEC to 'relax,' says oil price...</td>
      <td>world</td>
      <td>2.0</td>
      <td>positive</td>
    </tr>
  </tbody>
</table>

[top](#inshorts-analysis)
