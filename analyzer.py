from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from hazm import *
from langdetect import detect

def print_keywords(text,n):
    english = detect(text) == 'en'
    if english : 
        tokens = word_tokenize(text)
        
        stop_words = set(stopwords.words('english'))
        #tokens = cleanse(text)
        cleaned = []
        symbols = ['(',')',',','.','-','/','_']
        for word in tokens:
            if (word.lower() not in stop_words and
                word not in symbols and
                len(word) > 1 and
                word.isalpha()):
                cleaned.append(word)

        keywords =  Counter(cleaned).most_common(n)
        for word , count in keywords:
            print(f"{word} : {count}")

    else :
        normalizer = Normalizer()
        text = normalizer.normalize(text)
        tokens = word_tokenize(text)
        stop_words = set(stopwords_list())

        cleaned = []
        symbols = ['(',')',',','.','-','/','_']
        for kalame in tokens:
            if (kalame not in stop_words and
                kalame not in symbols and
                len(kalame) > 1) :
                cleaned.append(kalame)

        keywords =  Counter(cleaned).most_common(n)
        for word , count in keywords:
            print(f"{word} : {count}")

def describtion(text):
    print("Text Describtion : ")
    print("Pages : ",len(text))
    print("Words : ",len(return_string(text).split()))
    print("Detected language : ",detect(text))

def return_string(text_list):
    text_string = ""
    for page in text_list:
        text_string += page
    return text_string

