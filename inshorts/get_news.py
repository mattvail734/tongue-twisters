import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import normalize_text
import tag_text
import sentiment


def fetch_data(seed_urls):
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


def build_dataframe(seed_urls):
    news_df = fetch_data(seed_urls)
    # combine headline and article text
    news_df['full_text'] = news_df['news_headline'].map(str) + '. ' + news_df['news_article']
    # preprocess text
    news_df['normalized_text'] = normalize_text.normalize(news_df['full_text'])
    # POS tag text
    news_df['POS_tagged_text'] = tag_text.POS_tag_text(news_df['normalized_text'])
    # chunk (shallow parse) text
    news_df['chunked_text'] = tag_text.chunk_text(news_df['normalized_text'])
    # constituency parse text
    news_df['con_tagged_text'] = tag_text.con_tag_text(news_df['normalized_text'])
    # dependency parse text
    news_df['dep_tagged_text'] = tag_text.dep_tag_text(news_df['normalized_text'])
    # calculate sentiment
    news_df['sentiment_score'] = sentiment.sent_score(news_df['normalized_text'])
    # assign sentiment category
    news_df['sentiment_category'] = sentiment.sent_category(news_df['sentiment_score'])
    return news_df


# store in csv
def store_dataframe(df):
    dirname = os.path.dirname(__file__)
    news_output = os.path.join(dirname, 'news.csv')
    df.to_csv(news_output, index=False, encoding='utf-8')


# import data from a local csv
def import_corpus(file_name):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, file_name)
    return pd.read_csv(file_path)
