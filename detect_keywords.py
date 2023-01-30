from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import numpy as np
from md_to_text import get_text_article
from collections import Counter
from operator import itemgetter


def get_scores(file, language='english'):

    #Your text®
    text, split_word = get_text_article(file)
    text = [text]

    list_words = []
    list_word_not_voc = []
    #instantiate TfidfVectorizer
    tfidf = TfidfVectorizer(stop_words=stopwords.words(language))

    #apply tfidf
    tfidf_matrix = tfidf.fit_transform(text)

    #get feature names
    feature_names = tfidf.vocabulary_

    vocab = set(tfidf.vocabulary_)

    # get words not in vocabulary
    words = str(text).split(' ')
    stop_words = set(stopwords.words(language))

    words = [word.replace(',', '') for word in words]
    words = [word.replace('.', '') for word in words]

    not_in_vocab = [word for word in words if word.lower() not in vocab and word.lower() not in stop_words and  len(word) > 2]
    count_words = Counter(not_in_vocab)
    sorted_word_counts = sorted(count_words.items(), key=itemgetter(1), reverse=True)
    #get tfidf scores
    scores = zip(feature_names, np.asarray(tfidf_matrix.sum(axis=0)).ravel())
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    #Print top keywords
    for score in sorted_scores:
        list_words.append(score[0])
        print(score)
    for word in sorted_word_counts:
        list_word_not_voc.append(word[0])

    return list_words, list_word_not_voc, split_word