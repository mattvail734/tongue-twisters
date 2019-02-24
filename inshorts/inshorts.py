import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import conll2000
import get_news
import chunk_text
import entity_text
import sentiment


def main():
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)

    training_data = conll2000.chunked_sents()

    # train chunker model
    ntc = chunk_text.NGramTagChunker(training_data)

    seed_urls = ['https://inshorts.com/en/read/technology',
                 'https://inshorts.com/en/read/sports',
                 'https://inshorts.com/en/read/world']

    news_df = get_news.build_dataframe(seed_urls)
    news_df.to_html('initial_dataframe.html', columns=['news_headline', 'news_article', 'news_category'], max_rows=5)


    entity_df = entity_text.identify_named_entities(news_df['normalized_text'])
    top_entities = entity_text.top_entities(entity_df)

    sentiment_score = np.array(sentiment.sent_score(news_df['normalized_text'])).T
    sentiment_category = np.array(sentiment.sent_category(sentiment_score)).T
    sent_dict = {
        'news_category': news_df['news_category'],
        'sentiment_score': sentiment_score.astype('float'),
        'sentiment_category': sentiment_category}
    sent_df = pd.DataFrame(data=sent_dict)
    print(sent_df.groupby(by=['news_category']).describe())

    sns.boxplot(x='news_category', y='sentiment_score', hue='news_category', data=sent_df, palette='Set2')
    sns.despine(trim=True, left=True)
    plt.savefig('Sentiment_Histogram.png')


if __name__ == "__main__":
    main()
