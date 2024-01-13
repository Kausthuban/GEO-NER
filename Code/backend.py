import fuzzer
import spacy
import newmodel
import streamlit as st
import datetime
nlp = spacy.load("en_core_web_trf")
text = ''
message = st.text_area("Type your message here:", height=100)
submit_button = st.button("Submit")

if submit_button:
    if message:
        text = message
        st.write("Message submitted successfully.")
    else:
        st.write("Please enter a message.")

result = newmodel.extract(nlp,text)
for i in result:
    temp ,ind = fuzzer.fuzzy_search("Ascii.csv",i)
    st.write(f"The word {i} is found at index {ind} and the canonical name is {temp}")
# for i in range(len(messages)):
#     st.write(f"{messages[i]}")