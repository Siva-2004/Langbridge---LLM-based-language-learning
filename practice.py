import streamlit as st
import os
from dotenv import load_dotenv
import process

def speak():
    ll = st.selectbox("Learning Language",["Chinese","Japanese","French","Korean","Spanish","German","Dutch","Hindi","Tamil","Telugu","English","Kannada","Marathi","Bengali","Vietnamese","Tagalog","Portuguese","urdu","Turkish","Arabic","Malayalam"], index = None )
    kl = st.selectbox("Known Language",["Chinese","Japanese","French","Korean","Spanish","German","Dutch","Hindi","Tamil","Telugu","English","Kannada","Marathi","Bengali","Vietnamese","Tagalog","Portuguese","urdu","Turkish","Arabic","Malayalam"], index = None )
    if st.button("Submit"):
        pass
    if st.button("Speak..."):
        text = process.voice_input()
        response = process.llm(text,ll,kl)
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