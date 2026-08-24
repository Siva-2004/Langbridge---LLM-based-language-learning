import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


def study(topic , ll , kl):
    st.subheader(topic)
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key = api_key)
    if topic != "history": 
        system_template = "Give only the markdown code for a table containing translations of atleast or more than 15 common and unique words of following topic only in three columns {learn_language}, phonetic representation and {known_language} repectively."
        prompt = ChatPromptTemplate.from_messages(
            messages = [
                ("system",system_template),
                ("user","{sub}")
            ] 
        )
        chain = prompt | llm 
        result = chain.invoke(
            {
                "learn_language" : ll,
                "known_language" : kl,
                "sub" :  topic
            }
        )
        
        st.markdown(result.content)
    
    else:
        system_template = "Give a brief about the history of {learn_language} in {known_language}"
        prompt = ChatPromptTemplate.from_messages(
            messages = [
                ("system",system_template),
                ("user","Detailed History")
            ] 
        )
        chain = prompt | llm 
        result = chain.invoke(
            {
                "learn_language" : ll,
                "known_language" : kl,
            }
        )
        st.markdown(result.content)
        
def golden_sentences(ll,kl):
    st.subheader("Golden Sentences")
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key = api_key)
    system_template = "Give only the markdown code for a table containing translations of the given sentences only in three columns {learn_language}, phonetic representaiton and {known_language} repectively."
    prompt = ChatPromptTemplate.from_messages(
            messages = [
                ("system",system_template),
                ("user",["This is an apple.",
                                 "The apple is red.",
                                 "The apple is red.",
                                 "It is John’s apple",
                                 "I must give it to him.",
                                 "I give John his apple.",
                                 "He gives it to Sara.",
                                 "She gives it to us.",
                                 "We give her the apple.",
                                 "She doesn’t want the apple.",
                                 "They want to give it to me.",
                                 "But I do not want the apple either.",
                                 "I can’t eat the apple.",
                                 "It’s not mine.",
                                 "My apples are green.",
                                 "I will not take the red apple.",
                                 "Do you want an apple?",
                                 "Which one do you want?",
                                 "I will give you the red apple.",
                                 "It was John’s apple.",
                                 "But he said he doesn’t want it anymore.",
                                 "So now it is yours.",
                                 "You should eat it.",
                                 "Did you eat the apple?",
                                 "Why didn’t you eat it?",
                                 "If you ate it, you would be happy.",
                                 "Now someone else will eat the apple.",
                                 "They will eat all of the apples.",
                                 "And there are a lot of apples to eat.",
                                 "Most of them are red.",
                                 "But some of them are green.",
                                 "And none of the apples are blue.",
                                 "A few of them are big.",
                                 "And one of the apples is very small.",
                                 "But all of the apples are beautiful.",
                                 "These are beautiful, big, red apples.",
                                 "You can have as many as you want.",
                                 "Because I have enough for everyone.",
                                 "Almost everyone likes apples.",
                                 "The biggest ones are the best.",
                                 "Small apples are good too.",
                                 "But the big apples are better."
                                ])
            ] 
        )
    chain = prompt | llm 
    result = chain.invoke(
            {
                "learn_language" : ll,
                "known_language" : kl,
            }
        )
    st.markdown(result.content)
    
def generate_forms(verb,ll,kl):
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key = api_key)
    system_template = "Give only the markdown code for a table containing all tense forms of given verb only in columns {learn_language} ,{known_language},examples in {learn_language} and examples in {known_language}  repectively."
    prompt = ChatPromptTemplate.from_messages(
        messages = [
            ("system",system_template),
            ("user","{sub}")
        ] 
    )
    chain = prompt | llm 
    result = chain.invoke(
        {
            "learn_language" : ll,
            "known_language" : kl,
            "sub" :  verb
        }
    )
    
    st.markdown(result.content)
    