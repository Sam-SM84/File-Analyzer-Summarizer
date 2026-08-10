from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

def extract_keywords(text,n):
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

    return Counter(cleaned).most_common(n)

def describtion(text,file):
    print("Text Describtion : ")
    print("Pages : ",len(file))
    print("Words : ",len(text.split()))