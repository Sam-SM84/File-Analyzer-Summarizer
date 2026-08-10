#import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
#import string
import pymupdf
import sys
sys.stdout.reconfigure(encoding="utf-8")
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

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

def loadPDF(path):
    text = ""
    file = pymupdf.open(path)
    
    for page in file:
        text += page.get_text()
    return text , file

def analyse(text,file):
    print("Text Describtion : ")
    print("Pages : ",len(file))
    print("Words : ",len(text.split()))

def summarize(text,sentence_count=5):
    parser = PlaintextParser.from_string(text,Tokenizer('english'))
    summarizer = TextRankSummarizer()

    summary = summarizer(parser.document,sentence_count)
    result = "\n\n".join(str(sentence) for sentence in summary)

    return result

text , file = loadPDF("papers/OpenGL-cutted.pdf")
print("------------- Original Text -------------")
analyse(text,file)
print("------------- Extracted Words -------------")
#analyse(cleanse(text,False),file)
keywords = extract_keywords(text,15)
for word , count in keywords:
    print(f"{word} : {count}")

print("------------- PDF summary -------------")
summarized_text = summarize(text,sentence_count=3)
print(summarized_text)

"""
f = open("result.txt",'w')
f.write(summarized_text)
f.close()
print("\n\n Result stored!")
"""
