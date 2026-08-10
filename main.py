from analyzer import print_keywords , describtion
from summarizer import summarize
from file_reader import load_PDF , load_text

import sys
sys.stdout.reconfigure(encoding="utf-8")


text , file = load_PDF("papers/Joz2.pdf")

print("------------- Original Text -------------")
describtion(text,file)

print("------------- Extracted Words -------------")
print_keywords(text,5,english=False)


print("------------- PDF summary -------------")
summarized_text = summarize(text,paragraph_count=1)
print(summarized_text)


