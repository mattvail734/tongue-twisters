import os
import matplotlib.pyplot as plt
import seaborn as sns
import get_news
import entity_recognition

# dependencies
# SpaCy the en_core language model
# python3 -m spacy download en_core_web_md


def main():
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)

    seed_urls = ['https://inshorts.com/en/read/technology',
                 'https://inshorts.com/en/read/sports',
                 'https://inshorts.com/en/read/world']

    news_df = get_news.build_dataframe(seed_urls)
    news_df.to_html('initial_dataframe.html', columns=['news_headline', 'news_article', 'news_category'], max_rows=5)
    news_df.to_html('normalized_text.html', columns=['full_text', 'normalized_text'], max_rows=5)
    news_df.to_html('POS_tagged_text.html', columns=['normalized_text', 'POS_tagged_text'], max_rows=5)
    news_df.to_html('chunked_tagged_text.html', columns=['normalized_text', 'chunked_text'], max_rows=5)
    news_df.to_html('con_tagged_text.html', columns=['normalized_text', 'con_tagged_text'], max_rows=5)
    news_df.to_html('dep_tagged_text.html', columns=['normalized_text', 'dep_tagged_text'], max_rows=5)
    news_df.to_html('sentiment.html', columns=['news_headline', 'news_category', 'sentiment_score', 'sentiment_category'], max_rows=5)

    ordered_entity_df = entity_recognition.identify_named_entities(news_df['normalized_text'])
    ordered_entity_df.to_html('entities.html', columns=['Name', 'Type', 'Count'], max_rows=8)

    # NEED TO FIX BOXPLOT
    sns.boxplot(
        x='news_category', y='sentiment_score', hue='news_category',
        data=news_df['news_headline', 'news_article', 'news_category', 'sent_scores'],
        palette='Set2')
    sns.despine(trim=True, left=True)
    plt.savefig('Sentiment_Histogram.png')


if __name__ == "__main__":
    main()
