import streamlit as st
import choice
import os
from dotenv import load_dotenv

def learn():
    st. header("Learn Vocabulary")
    st.divider()
    ll = st.selectbox("Learning Language",["Chinese","Japanese","French","Korean","Spanish","German","Dutch","Hindi","Tamil","Telugu","English","Kannada","Marathi","Bengali","Vietnamese","Tagalog","Portuguese","urdu","Turkish","Arabic","Malayalam"], index = None )
    kl = st.selectbox("Known Language",["Chinese","Japanese","French","Korean","Spanish","German","Dutch","Hindi","Tamil","Telugu","English","Kannada","Marathi","Bengali","Vietnamese","Tagalog","Portuguese","urdu","Turkish","Arabic","Malayalam"], index = None )
    #st.write(lang)
    #st.write(known_lang)
    golden_sentences = st.button("Learn Golden Sentences")
     
    col1, col2, col3, col4 = st.columns(4,gap='large')
    with col1:
        st.image("static/Greetings.jpg", caption = 'greetings')
        st.image("static/Numbers.jpg", caption = 'numbers')
        st.image("static/Food.jpg", caption = 'Food')
    with col2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        greetings = st.button("Greetings")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        numbers = st.button("Numbers")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        Food = st.button("Food")
        
    with col3:
        st.image("static/Family.jpg",caption = 'Family')
        st.image("static/Transport.jpg", caption = 'Transport')
        st.image("static/History.jpg", caption = 'History')
        
    with col4:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        family = st.button("Family")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        Transport = st.button("Transport")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        History = st.button("History")
        
    if greetings:
        choice.study("greetings",ll,kl)
    elif numbers:
        choice.study("numbers",ll,kl)
    elif Food:
        choice.study("food",ll,kl)
    elif family:
        choice.study("family",ll,kl)
    elif Transport:
        choice.study("transport",ll,kl)
    elif History:
        choice.study("history",ll,kl)
    elif golden_sentences:
        choice.golden_sentences(ll,kl)
        
def verbs():
    st. header("Verb Forms")
    ll = st.selectbox("Learning Language",["Chinese","Japanese","French","Korean","Spanish","German","Dutch","Hindi","Tamil","Telugu","English","Kannada","Marathi","Bengali","Vietnamese","Tagalog","Portuguese","urdu","Turkish","Arabic","Malayalam"], index = None)
    kl = st.selectbox("Known Language",["Chinese","Japanese","French","Korean","Spanish","German","Dutch","Hindi","Tamil","Telugu","English","Kannada","Marathi","Bengali","Vietnamese","Tagalog","Portuguese","urdu","Turkish","Arabic","Malayalam"], index = None)
    verb = st.text_input(placeholder="Enter any verb in your known language..",label="Enter a verb")
    if st.button("submit"):
        choice.generate_forms(verb,ll,kl)
    
    
    