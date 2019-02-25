import pandas as pd
import spacy


def identify_named_entities(corpus):
    nlp = spacy.load('en_core_web_md', parse=True, tag=True, entity=True)
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
    entity_df = pd.DataFrame(named_entities, columns=['Name', 'Type'])
    ordered_entity_df = (entity_df.groupby(['Name', 'Type']).size().sort_values(ascending=False).reset_index().rename(columns={0: 'Count'}))
    return ordered_entity_df
