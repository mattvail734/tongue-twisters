import spacy
import pandas as pd

nlp = spacy.load('en_core_web_md', parse=True, tag=True, entity=True)


# corpus is a Panda series; each element is a single set of tuples
# using NLTK - each tuple is a pair (word, POS tag)
def identify_named_entities(corpus):
    named_entities = []
    for doc in corpus:
        temp_entity_name = ''
        temp_named_entity = None
        doc = nlp(doc)
        for word in doc:
            term = word.text
            tag = word.ent_type_
            if tag:
                temp_entity_name = ' '.join([temp_entity_name, term]).strip()
                temp_named_entity = (temp_entity_name, tag)
            else:
                if temp_named_entity:
                    named_entities.append(temp_named_entity)
                    temp_entity_name = ''
                    temp_named_entity = None
    entity_df = pd.DataFrame(named_entities, columns=['Entity Name', 'Entity Type'])
    return entity_df


def top_entities(entity_df, top=15):
    top_entities = (entity_df.groupby(by=['Entity Name', 'Entity Type']).size()
                    .sort_values(ascending=False).reset_index().rename(columns={0: 'Frequency'}))
    top_entities.T.iloc[:, :top]
