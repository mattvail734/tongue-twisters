import requests
from bs4 import BeautifulSoup
import pandas as pd
import normalize_corpus
import tag_corpus
import os

dirname = os.path.dirname(__file__)

seed_urls = ['https://inshorts.com/en/read/technology',
             'https://inshorts.com/en/read/sports',
             'https://inshorts.com/en/read/world']


def build_dataset(seed_urls):
    news_data = []
    for url in seed_urls:
        news_category = url.split('/')[-1]
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')

        news_articles = [
            {'news_headline': headline.find(
                'span', attrs={'itemprop': 'headline'}).string,
                'news_article': article.find(
                    'div', attrs={'itemprop': 'articleBody'}).string,
                'news_category': news_category}

            for headline, article in zip(soup.find_all(
                'div', class_=['news-card-title news-right-box']),
                soup.find_all('div', class_=['news-card-content news-right-box']))
        ]
        news_data.extend(news_articles)
    df = pd.DataFrame(news_data)
    df = df[['news_headline', 'news_article', 'news_category']]
    return df


news_df = build_dataset(seed_urls)

# combine headline and article text
news_df['full_text'] = news_df['news_headline'].map(str) + '. ' + news_df['news_article']

# clean text
news_df['clean_text'] = normalize_corpus.normalize(news_df['full_text'], text_lemmatization=False, text_lower_case=False, special_char_removal=False)

# tag parts of speech (POS) in the text
news_df = tag_corpus.tag(news_df)

# store in csv
news_output = os.path.join(dirname, 'news.csv')
news_df.to_csv(news_output, index=False, encoding='utf-8')
