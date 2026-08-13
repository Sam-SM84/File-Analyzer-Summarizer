from analyzer import *
from summarizer import *
from file_reader import *

import sys
sys.stdout.reconfigure(encoding="utf-8")

import streamlit as st

import pandas as pd

#python -m streamlit run F:\my_python\paperAnalyzer\main.py

st.title("File Analyzer/Summarizer")
st.subheader("by Sam SalahiMoghaddam")
uploaded_file = st.file_uploader(
    "Upload a file",
    accept_multiple_files=False,
    type=["pdf","txt"]
)
text_list = []
output = []

if uploaded_file:
    st.success(f"Successfuly uploaded . Selected file : {uploaded_file.name}")
    text_list = load_PDF(uploaded_file)
else:
    st.error("There currently no files")
    

method = st.selectbox("What should this program do? : ",['Extract keywords','Find word','Summarize','Describtion'])
if method == 'Extract keywords':
    #st.write(return_string(text_list))
    n = st.number_input("Enter number of top common words :", min_value=5, format="%d")
    if st.button("Show results") : 
        output.clear()
        output.append("-------------------------")
        output.append("Top " + str(n) + " repeated words : ")
            #st.write("Top " + str(n) + " repeated words : ")
        keywords = return_keywords(return_string(text_list),n)
        for i in keywords:
            output.append(str(i['Word']) + " : " + str(i['Count']))
                #st.write(i)
        output.append("-------------------------")

        df = pd.DataFrame(keywords)
        chart = st.bar_chart(df, x="Word", y="Count")
        

elif method == 'Find word':
    word = st.text_input("Enter the word : ")
    output.clear()
    output.append("Results for the search of (" + word + ")")
    distance = st.slider("Choose the distance level of the word displayment : ",min_value=5,max_value=100)
    if st.button("Show results") : 
        if word:
            result = search_text(text_list,word,distance)
            for r in result:
                output.append("-------------------------")
                output.append("Page : " + str(r['Page'] + 1))
                output.append("Text : " + str(r['Text']))

        else :
            st.error("Please fill the input box")

elif method == 'Summarize':
    sm = st.selectbox("Select a summarization method : ",['TextRank','T5 (English Only)'])
    if sm == 'TextRank':
        count = st.slider("Choose the paragraph amount of the summarized text : ",min_value=1,max_value=10)
        if st.button("Show results") : 
            output.clear()
            output.append(summarize_textRank(return_string(text_list),count))

    else:
        min_length = st.slider("Minimum length : ",min_value=10,max_value=20)
        max_length = st.slider("Maximum length : ",min_value=20,max_value=100)
        if st.button("Show results"):
            output.clear()
            output.append(summarize_T5(return_string(text_list),min_length,max_length))

else:
    if st.button("Show results") : 
        desc = describtion(text_list)
        output.clear()
        for i in desc : 
            output.append(i)
        output.append("-------------------------")

for result in output:
    st.write(result)


