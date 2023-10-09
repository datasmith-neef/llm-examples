import streamlit as st
import time 

with st.sidebar:
    pass


st.title("Showcase Streamlit Frontend")
st.latex(r'\begin{equation} P(Y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \ldots + \beta_p X_p)}} \end{equation}')

st.write("das Schweizer Messer Markdown")


def change():
    #print("Parameter changed")
    print(st.session_state.checker)


state = st.checkbox("Paramater",value = True,on_change= change, key = "checker")


st.write("Uploading a File")
st.markdown("---")
image = st.file_uploader("Lade ein Bild hoch", type = ["png","jpg"])

if image is not None:
    st.image(image)

val = st.slider("Temperature of youre model",min_value = 0 , max_value = 1)
print(val)

val = st.text_input("Gib einen Wert ein ", max_chars = 50)
print(st.caption(val))

val = st.text_area("Kursbeschreibung")

val = st.date_input("Wähle ein Datum aus")
print(st.caption(val))

val = st.time_input("Set Timer")


import plotly.graph_objects as go

# Erstelle ein Tachometer (Gauge Chart)
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=270,
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [0, 360]}}
))

# Zeige das Tachometer in Streamlit
st.plotly_chart(fig)

bar = st.progress(0)
for i in range(10):
    time.sleep(2)
    bar.progress(i)

st.markdown("## Regeistrierung")
with st.form("User Registration"):
    col1,col2 = st.columns(2)
    col1.text_input("Vorname")
    col2.text_input("Nachname")
    st.text_input("email adresse")
    st.text_input("Passwort",type="password")
    st.form_submit_button("Senden")