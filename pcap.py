import streamlit as st
import json

def start_pcap() :
    # Laden der JSON-Daten
    with open("questions.json", "r") as file:
        questions = json.load(file)

    # Anzeigen der Fragen und Optionen mit Streamlit
    for q_key, q_val in questions.items():
        st.markdown(f"### {q_key}: {q_val['Question']}")
        
        # Wenn es einen CodeSnippet gibt, zeigen Sie ihn an
        if "CodeSnippet" in q_val:
            code = "\n".join(q_val["CodeSnippet"])
            st.code(code, language="python")
        
        # Erstellen von Radiobuttons für Optionen
        options = q_val["Options"]
        option = st.radio("Options", [options[key] for key in options], key=q_key)

        # Sie können hier eine Logik hinzufügen, um den ausgewählten Wert zu überprüfen
        # oder eine Benutzerantwort zu speichern
