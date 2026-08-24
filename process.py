import speech_recognition as sr
from gtts import gTTS
import streamlit as st
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print("perfect!!")




def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
    

def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    tts.save("speech.mp3")
    
def llm(user_text , ll, kl):
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                f"You are a friendly language tutor. Please help the user practice {ll} and  only respond in {ll} followed by {kl} to help them understand. if required correct the grammar used by user and also give remarks for the pronounciation of user in {ll} and {kl} only."
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )

    msgs = StreamlitChatMessageHistory(key="langchain_messages")
    model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key = api_key)
    chain = prompt | model | StrOutputParser()
    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="question",
        history_messages_key="chat_history",
    )
    
    if user_text:
        st.chat_message("human").write(user_text)

        # Assistant's response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            config = {"configurable": {"session_id": "any"}}

            response = chain_with_history.stream({"question": user_text}, config)
            print(response)

            for res in response:
                full_response += res or ""
                message_placeholder.markdown(full_response + "|")
                message_placeholder.markdown(full_response)
            
            return full_response
                

    else:
        st.warning("Please enter your question.")
        
def enact_llm(user_text,scenario,ll):
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                f"You are a friendly language tutor. Please help the user practice {ll} by enacting a real life scenario : {scenario}"
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )

    msgs = StreamlitChatMessageHistory(key="langchain_messages")
    model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key = api_key)
    chain = prompt | model | StrOutputParser()
    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="question",
        history_messages_key="chat_history",
    )
    
    if user_text:
        st.chat_message("human").write(user_text)

        # Assistant's response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            config = {"configurable": {"session_id": "any"}}

            response = chain_with_history.stream({"question": user_text}, config)
            print(response)

            for res in response:
                full_response += res or ""
                message_placeholder.markdown(full_response + "|")
                message_placeholder.markdown(full_response)
            
            return full_response
                

    else:
        st.warning("Please enter your question.")
    