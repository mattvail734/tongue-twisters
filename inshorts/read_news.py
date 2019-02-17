import csv
import pandas

# import cleaned news data from a csv
def import_corpus(file_name):
    news = open(file_name)
    reader = csv.reader(news)
    corpus = []
    next(reader)
    for row in reader:
        corpus.append()
    return corpus
