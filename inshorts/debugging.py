import unicodedata

text = unicodedata.normalize('NFKD', 'Sómě Áccěntěd těxt').encode('ascii', 'ignore').decode('utf-8', 'ignore')
print(text)
