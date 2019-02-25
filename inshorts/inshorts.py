import os
import matplotlib.pyplot as plt
import seaborn as sns
import get_news
import entity_recognition
import tokenize_text

# dependencies
# SpaCy the en_core language model
# python3 -m spacy download en_core_web_md

# general naming conventions:
# 'corpus' is a Panda series of docs
# 'doc' is a string of words
# 'word' is a single word string
# 'token' is the SpaCy tokenized version of 'word'


def main():
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)

    seed_urls = ['https://inshorts.com/en/read/technology',
                 'https://inshorts.com/en/read/sports',
                 'https://inshorts.com/en/read/world']

    news_df = get_news.build_dataframe(seed_urls)
    news_df.to_html('initial_dataframe.html', columns=['news_headline', 'news_article', 'news_category'], max_rows=5)
    news_df.to_html('normalized_text.html', columns=['full_text', 'normalized_text'], max_rows=5)
    news_df.to_html('tokenized_text.html', columns=['normalized_text', 'tokenized_text'], max_rows=5)
    tokenized_text = news_df['tokenized_text']
    tokenize_text.dep_tagged_to_html(tokenized_text[0], 'dep_tagged.html')
    tokenize_text.dep_tagged_to_svg(tokenized_text[0], 'dep_tagged.svg')
    tokenize_text.entities_to_html(tokenized_text[0], 'entity_visualization.html')
    tokenize_text.entities_to_svg(tokenized_text[0], 'entity_visualization.svg')

    ordered_entity_df = entity_recognition.identify_named_entities(news_df['normalized_text'])
    ordered_entity_df.to_html('entities.html', columns=['Name', 'Type', 'Count'], max_rows=8)

    news_df.to_html('sentiment.html', columns=['news_headline', 'news_category', 'sentiment_score', 'sentiment_category'], max_rows=5)
    sent_df = news_df[['news_category', 'sentiment_score', 'sentiment_category']]
    sent_df.groupby(by=['news_category'])
    sns.boxplot(
        x='news_category', y='sentiment_score', hue='news_category',
        data=sent_df, palette='Set2')
    sns.despine(trim=True, left=True)
    plt.savefig('Sentiment_Histogram.png')


if __name__ == "__main__":
    main()
