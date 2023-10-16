import openai
import streamlit as st
import os    
import pcap
import streamlit as st


import streamlit as st

st.markdown("""
    <style>
        @keyframes typewriter {
            from { 
                width: 0; 
            }
            to { 
                width: 100%; 
            }
        }

        @keyframes blink {
            from, to {
                border-color: transparent;
            }
            50% {
                border-color: black;
            }
   
     
        }

        .typewriter-text {
            display: inline-block;
            overflow: hidden;
            border-right: 0.05em solid black;  /* Cursor-Effekt */
            white-space: nowrap;
            font-size: 2.5rem; 
            font-weight: bold;
            animation: 
        typewriter 5s steps(50, end), 
        blink .75s step-end 13, 
        fadeOutCursor 0.25s forwards 10s;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="typewriter-text">💬 Datasmith-GPT</div>', unsafe_allow_html=True)

st.caption("🚀 A chatbot powered by OpenAI LLM and Datasmith Office")




st.markdown("---")




with st.sidebar:

    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    

    user_option = st.radio("Wählen Sie eine Option:", options=["Anmelden", "Registrieren"])

    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")

    if openai_api_key and username and password :
        user = s.Users(username,openai_api_key)
    

    if user_option == "Registrieren":
        confirm_password = st.text_input("Passwort bestätigen", type="password")
        if st.button("Registrieren"):
            if password == confirm_password:
                # Speichern Sie die Benutzerdaten in einer Datenbank oder einer Datei
                st.success("Registrierung erfolgreich!")
            else:
                st.error("Die Passwörter stimmen nicht überein.")

    elif user_option == "Anmelden":
        if st.button("Anmelden"):
            # Überprüfen Sie die Benutzerdaten mit den gespeicherten Daten
            # Beispiel: if check_credentials(username, password):
            if True:  # Platzhalter für die Überprüfung der Anmeldeinformationen
                st.success("Anmeldung erfolgreich!")
                openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
                if st.button("API-Schlüssel speichern"):
                    encrypted_key = encrypt_key(openai_api_key)
                    # Speichern Sie den verschlüsselten Schlüssel in der Datenbank oder in einer Datei
                    st.success("API-Schlüssel erfolgreich gespeichert!")
            else:
                st.error("Falscher Benutzername oder Passwort.")


tutorial_prompt = ""
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant","content": "Hi, welche Aufgabe kann ich für dich übernehmen"}]

# Dropdown-Menü hinzufügen
role_options = ["Standard", "Tutorial-Writer", "PCAP"]
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
    # Systemnachricht zur Liste der Nachrichten hinzufügen
    st.session_state.messages.append({"role": "system", "content": tutorial_prompt})

# Nachrichten anzeigen, außer denen mit der Rolle "system"
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

if selected_role == "PCAP":
    pcap.start_pcap()
