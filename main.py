from analyzer import *
from summarizer import summarize
from file_reader import *

import sys
sys.stdout.reconfigure(encoding="utf-8")


text_list = load_PDF("papers/Joz2.pdf")


print("------------- Original Text -------------")
describtion(text_list)

print("------------- Extracted Words -------------")
print_keywords(return_string(text_list),5)

print("------------- PDF summary -------------")
summarized_text = summarize(return_string(text_list),paragraph_count=3)
print(summarized_text)

print(search_text(text_list,'برنامه',10))
