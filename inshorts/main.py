import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import conll2000
import get_news
import chunk_text
import entity_text
import sentiment

training_data = conll2000.chunked_sents()

# train chunker model
ntc = chunk_text.NGramTagChunker(training_data)

news_df = get_news.build_dataframe()
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

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
sp = sns.stripplot(
    x='news_category', y='sentiment_score', hue='news_category',
    data=sent_df, ax=ax1)
bp = sns.boxplot(
    x='news_category', y='sentiment_score', hue='news_category',
    data=sent_df, palette='Set2', ax=ax2)
t = f.suptitle('Visualizing News Sentiment', fontsize=14)
plt.show()
