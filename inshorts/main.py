import get_news
import chunk_text
import entity_text
from nltk.corpus import conll2000

training_data = conll2000.chunked_sents()

# train chunker model
ntc = chunk_text.NGramTagChunker(training_data)

news_df = get_news.build_dataframe()
entity_df = entity_text.identify_named_entities(news_df['normalized_text'])
print(news_df['normalized_text'].head)
top_entities = entity_text.top_entities(entity_df)
print(top_entities)
