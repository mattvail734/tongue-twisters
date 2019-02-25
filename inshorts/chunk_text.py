from nltk.chunk.util import tree2conlltags, conlltags2tree
from nltk.tag import UnigramTagger, BigramTagger
from nltk.chunk import ChunkParserI
from nltk.corpus import conll2000

# first download the nltk conll2000 corpora
# nltk.download('conll2000')


# chunk_sents is a single set of words NOT an iterable
def conll_tag_chunks(chunk_sents):
    tagged_sents = [tree2conlltags(tree) for tree in chunk_sents]
    return [[(t, c) for (w, t, c) in sent] for sent in tagged_sents]


def combined_tagger(train_data, taggers, backoff=None):
    for tagger in taggers:
        backoff = tagger(train_data, backoff=backoff)
    return backoff


class NGramTagChunker(ChunkParserI):

    def __init__(self, train_sentences, tagger_classes=[UnigramTagger, BigramTagger]):
        train_sent_tags = conll_tag_chunks(train_sentences)
        self.chunk_tagger = combined_tagger(train_sent_tags, tagger_classes)

    def parse(self, tagged_sentence):
        if not tagged_sentence:
            return None
        pos_tags = [tag for word, tag in tagged_sentence]
        chunk_pos_tags = self.chunk_tagger.tag(pos_tags)
        chunk_tags = [chunk_tag for (pos_tag, chunk_tag) in chunk_pos_tags]
        wpc_tags = [
            (word, pos_tag, chunk_tag)
            for ((word, pos_tag), chunk_tag)
            in zip(tagged_sentence, chunk_tags)]
        return conlltags2tree(wpc_tags)


# train chunker model
training_data = conll2000.chunked_sents()
ntc = NGramTagChunker(training_data)
