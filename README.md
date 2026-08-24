# LangBridge – LLM-Powered Language Learning Assistant

LangBridge is an interactive language-learning application that uses **Large Language Models (LLMs)** to help users practice new languages through conversational interactions.

The application simulates real-world conversations, allowing learners to practice communicating in a target language without requiring a native-speaking conversation partner. It supports both **text-based and voice-based interaction** to provide an interactive language-learning experience.

---

## Features

- Interactive conversations with an LLM for language practice
- Practice multiple languages through conversational scenarios
- AI-powered responses using the Google Gemini API
- Context-aware conversations using LangChain
- Speech-to-text for voice-based user input
- Text-to-speech for listening and pronunciation practice
- Streamlit-based web interface
- Secure API key management using environment variables

---

## Application Workflow

```text
                    User Selects Language
                            |
                            v
                    +---------------+
                    |  User Input   |
                    | Text / Voice  |
                    +-------+-------+
                            |
                     Voice Input?
                       /       \
                     Yes        No
                      |          |
                      v          |
               Speech-to-Text    |
                      |          |
                      +----+-----+
                           |
                           v
                    +---------------+
                    |   LangChain   |
                    +-------+-------+
                            |
                            v
                    +---------------+
                    | Google Gemini |
                    |      LLM      |
                    +-------+-------+
                            |
                            v
                    Context-Aware
                       Response
                            |
                            v
                    +---------------+
                    | Text-to-Speech|
                    +-------+-------+
                            |
                            v
                    User Hears / Reads
                       the Response
                            |
                            v
                    Continue Practice## Technologies Used
```

LangBridge is built using:

- **Python** - Application development and integration
- **Google Gemini API** - Large Language Model for generating conversational responses
- **LangChain** - Framework for interacting with the LLM
- **Streamlit** - Interactive web application interface
- **Speech Recognition** - Converts spoken input into text
- **pyttsx3** - Text-to-speech conversion
- **gTTS** - Google Text-to-Speech

## Environment Variables

Create a `.env` file in the root directory of the project:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace your_gemini_api_key_here with your actual Google Gemini API key.

