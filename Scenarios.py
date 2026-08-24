import streamlit as st
from choice import ChatGoogleGenerativeAI , ChatPromptTemplate
import process
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


def enact():
    
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key = api_key)
    ll = st.selectbox("Learning Language",["Chinese","Japanese","French","Korean","Spanish","German","Dutch","Hindi","Tamil","Telugu","English","Kannada","Marathi","Bengali","Vietnamese","Tagalog","Portuguese","urdu","Turkish","Arabic","Malayalam"], index = None )
    scenario = st.selectbox("Select Scenario",["Ordering a Dish","Meeting an Old friend","Asking for directions","Booking a Travel ticket at counter","Buying Groceries at a store"],index = None)
    
    if st.button("Submit"):
        system_template = "Translate from English to {ll}"
        prompt = ChatPromptTemplate.from_messages(
            messages = [
                ("system",system_template),
                ("user","Hello, How may I help you?")
            ] 
        )
        chain = prompt | llm 
        result = chain.invoke(
            {
                "ll" : ll
            }
        )
        st.chat_message("assistant").write(result.content)
        
    if st.button("speak"):
        text = process.voice_input()
        response = process.enact_llm(text,ll,scenario)
        #print(response)
        if response:
            response.replace("*"," ")
            process.text_to_speech(response)
            audio_file=open("speech.mp3","rb")
            audio_bytes=audio_file.read()
            st.audio(audio_bytes)
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")
    