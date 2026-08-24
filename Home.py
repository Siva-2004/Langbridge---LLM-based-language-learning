import streamlit as st
import os
from dotenv import load_dotenv

def config_page():
    st.set_page_config(layout = "wide")
    
config_page()

from streamlit_option_menu import option_menu  # noqa: E402
import Learn  # noqa:E402
import practice  # noqa:E402
import Scenarios  # noqa: E402

st.title("LANG BRIDGE")
st.subheader("Learn languages like never before !!!")

choosen = option_menu(
    menu_title = None,
    options = ["Home🏠","Vocabulary📚","Verb Forms🧠","Scenarios🎭","Conversation Practice🗣️"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
)

if choosen == "Home🏠":
    st.subheader("Popular Languages")
    col1, col2, col3  = st.columns(3 , gap = "large")
    with col1:
        st.image("static/united-states-of-america.png" ,caption = "English(US)")
        st.image("static/france.png", caption = "French")
        
    with col2:
        st.image("static/united-kingdom.png", caption = "English(UK)")
        st.image("static/germany.png", caption = "German")
    with col3:
        st.image("static/spain.png", caption = "Spanish")
        st.image("static/china.png", caption = "Chinese (Mandarin)")
        
    st.divider()
    st.markdown("<div style = 'text-align: center' ><p style = 'font-size : 25px'> Using AI to learn a language offers a personalized, efficient, and interactive experience that traditional methods often lack. AI-powered language learning tools adapt to your individual pace, strengths, and weaknesses, providing tailored lessons and real-time feedback to help you improve faster. With features like speech recognition, conversational practice, and instant translations, AI creates an immersive environment that mimics real-world interactions, making learning more engaging and practical. Additionally, AI can analyse your progress and adjust content to focus on areas where you need the most improvement, ensuring a more effective learning journey. Whether you're a beginner or advanced learner, AI makes language learning accessible, flexible, and highly effective.</p></div>",unsafe_allow_html = True)
    
    
    
elif choosen == "Vocabulary📚":
    Learn.learn()
    
elif choosen == "Scenarios🎭":
    Scenarios.enact()
    
elif choosen == "Conversation Practice🗣️":
    practice.speak() 
    
elif choosen == "Verb Forms🧠":
    Learn.verbs()
    

