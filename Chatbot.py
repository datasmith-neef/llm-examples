import openai
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Datasmith-GPT für Profis")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM and Datasmith Office")

# Dropdown-Menü hinzufügen
role_options = ["Standard", "Tutorial-Writer"]
selected_role = st.selectbox("Rolle auswählen:", role_options)

# Den Prompt für die Rolle "Tutorial-Writer" festlegen
if selected_role == "Tutorial-Writer":
    tutorial_prompt = """
    Du bist ein spezialisiertes Tutorial-Modul namens TutorialGPT. Deine Expertise besteht darin, detaillierte und leicht verständliche Tutorials zu generieren. Sobald ich dir meine Anforderungen schildere, schlüpfst du in die entsprechende Expertenrolle und erstellst ein vollständiges Tutorial.
    
    1. Frage mich nach dem gewünschten Thema des Tutorials. Warte auf meine Antwort!
    2. Stelle mir basierend auf dem Thema aus Schritt 1 fünf Fragen, deren Antworten für dich ein perfektes Briefing zum Thema und Ziel des Tutorials darstellen.
    3. Schlüpfe, basierend auf den Antworten aus Schritt 2, in die ideale Expertenrolle und bitte mich um Bestätigung. Warte auf meine Antwort!
    4. Entwickle ein detailliertes Tutorial mit Titel, Kurzbeschreibung und strukturierter Gliederung. Bitte mich um Feedback und gehe erst nach meiner endgültigen Bestätigung zu Schritt 5.
    5. Sobald ich mit dem Lehrplan zufrieden bin, beginne mit der kapitelweisen Erstellung des Tutorials. Frage mich nach jedem Kapitel um Feedback und fahre erst fort, wenn ich zufrieden bin.
    
    Beachte: Gehe immer davon aus, dass der Benutzer keine Vorkenntnisse zum Thema hat. Gestalte die Tutorials immer sehr detailliert und leicht nachvollziehbar.
    """
else:
    tutorial_prompt = ""

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # Den ausgewählten Prompt basierend auf der ausgewählten Rolle verwenden
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages, prompt=tutorial_prompt)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
