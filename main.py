from analyzer import extract_keywords , describtion
from summarizer import summarize
from file_reader import load_PDF , load_text

import sys
sys.stdout.reconfigure(encoding="utf-8")

text , file = loadPDF("papers/OpenGL-cutted.pdf")
print("------------- Original Text -------------")
describtion(text,file)
print("------------- Extracted Words -------------")
#analyse(cleanse(text,False),file)
keywords = extract_keywords(text,15)
for word , count in keywords:
    print(f"{word} : {count}")

print("------------- PDF summary -------------")
summarized_text = summarize(text,sentence_count=3)
print(summarized_text)
