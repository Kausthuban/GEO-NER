import fuzzer
import spacy
import NLP_model
import streamlit as st

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

result = NLP_model.extract(nlp,text)
for i in result:
    temp ,ind = fuzzer.fuzzy_search("Ascii.csv",i)
    st.write(f"The word {i} is found at index {ind} and the canonical name is {temp}")
