from analyzer import *
from summarizer import summarize
from file_reader import *

import sys
sys.stdout.reconfigure(encoding="utf-8")

import streamlit as st

#python -m streamlit run F:\my_python\paperAnalyzer\main.py

st.title("File Analyzer/Summarizer")

uploaded_file = st.file_uploader(
    "Upload a file",
    accept_multiple_files=False,
    type=["pdf","txt"]
)
text_list = []

if uploaded_file:
    st.success(f"Successfuly uploaded . Selected file : {uploaded_file.name}")
    text_list = load_PDF(uploaded_file)
else:
    st.error("There currently no files")
    

method = st.selectbox("What should this program do? : ",['Extract keywords','Find word','Summarize','Describtion'])
if method == 'Extract keywords':
    #st.write(return_string(text_list))
    n = st.number_input("Enter number of top common words :", min_value=5, format="%d")
    if st.button("Print"):
        keywords = return_keywords(return_string(text_list),n)
        for i in keywords:
            st.write(i)

elif method == 'Find word':
    word = st.text_input("Enter the word : ")
    distance = st.slider("Choose the distance level of the word displayment : ",min_value=5,max_value=100)
    if st.button("search") :
        if word:
            result = search_text(text_list,word,distance)
            for r in result:
                st.write("-------------------------")
                st.write("Page : ",r['Page'] + 1)
                st.write("Text : ",r['Text'])

        else :
            st.error("Please fill the input box")

elif method == 'Summarize':
    count = st.slider("Choose the paragraph amount of the summarized text : ",min_value=1,max_value=7)
    if st.button("summarize") :
        st.write(summarize(return_string(text_list),count))

else:
    desc = describtion(text_list)
    for i in desc : 
        st.write(i)


