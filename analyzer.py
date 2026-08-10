from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from hazm import *

def print_keywords(text,n,english=True):
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
        n = Normalizer()
        text = n.normalize(text)
        tokens = word_tokenize(text)
        stop_words = set(stopwords_list())

        cleaned = []
        symbols = ['(',')',',','.','-','/','_']
        for kalame in tokens:
            if (kalame not in stop_words and
                kalame not in symbols and
                len(kalame) > 1) :
                cleaned.append(kalame)
        print(cleaned)

def describtion(text,file):
    print("Text Describtion : ")
    print("Pages : ",len(file))
    print("Words : ",len(text.split()))
