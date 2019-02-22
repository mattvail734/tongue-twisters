from afinn import Afinn

af = Afinn()


def sent_score(corpus):
    sentiment_scores = [af.score(article) for article in corpus]
    return sentiment_scores


def sent_category(scores):
    sentiment_category = [
        'positive' if score > 0
        else 'negative' if score < 0
        else 'neutral'
        for score in scores]
    return sentiment_category
