from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from hazm import *
from langdetect import detect
from sklearn.feature_extraction.text import TfidfVectorizer

def return_keywords(text,n):
    english = detect(text) == 'en'
    message = []
    if english : 
        tokens = word_tokenize(text)

        """
                stop_words = set(stopwords.words('english'))
        cleaned = []
        symbols = ['(',')',',','.','-','/','_']
        for word in tokens:
            if (word.lower() not in stop_words and
                word not in symbols and
                len(word) > 1 and
                word.isalpha()):
                cleaned.append(word)
        """
        cleaned = clean_list_english(tokens)
        keywords =  Counter(cleaned).most_common(n)
        for word , count in keywords:
            message.append({"Word" : word,"Count" : count}) 

    else :
        normalizer = Normalizer()
        text = normalizer.normalize(text)
        tokens = word_tokenize(text)
        """
                stop_words = set(stopwords_list())

        cleaned = []
        symbols = ['(',')',',','.','-','/','_']
        for kalame in tokens:
            if (kalame not in stop_words and
                kalame not in symbols and
                len(kalame) > 1) :
                cleaned.append(kalame)
        """
        tamiz = clean_list_persian(tokens)

        keywords =  Counter(tamiz).most_common(n)
        for word , count in keywords:
            message.append({"Word" : word,"Count" : count}) 

    return message

def return_TFIDF(text_list,n):
    english = detect(return_string(text_list)) == 'en'
    if english : 
        text_list = clean_list_english(text_list)
    else :
        text_list = clean_list_persian(text_list)

    tfidf = TfidfVectorizer()
    result = tfidf.fit_transform(text_list)
    words = tfidf.get_feature_names_out()
    scores = result.mean(axis=0).A1
    keywords = list(zip(words,scores))
    keywords.sort(key=lambda x:x[1],reverse=True)

    message = []
    for word , score in keywords[:n]:
        message.append({"Word" : word,"Score" : score})
    return message

def describtion(text):
    result = []
    result.append("-------------------------")
    result.append("Text Describtion : ")
    result.append("Pages : " + str(len(text)))
    result.append("Words : " + str(len(return_string(text).split())))
    result.append("Detected language : " + str(detect(return_string(text))))
    return result

def return_string(text_list):
    text_string = ""
    for page in text_list:
        text_string += page
    return text_string

def clean_list_english(text_list):
    stop_words = set(stopwords.words('english'))
    cleaned = []
    symbols = ['(',')',',','.','-','/','_']
    for word in text_list:
        if (word.lower() not in stop_words and
            word not in symbols and
            len(word) > 1 and
            word.isalpha()):
            cleaned.append(word)
    return cleaned

def clean_list_persian(text_list):
    stop_words = set(stopwords_list())
    tamiz = []
    symbols = ['(',')',',','.','-','/','_']
    for kalame in text_list:
        if (kalame not in stop_words and
            kalame not in symbols and
            len(kalame) > 1) :
            tamiz.append(kalame)
    return tamiz
