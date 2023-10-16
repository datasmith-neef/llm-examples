import streamlit as st
import time 
import requests
from streamlit_lottie import st_lottie

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

val = st.slider("Temperature of youre model",min_value = 0 , max_value = 100)
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
    value=130,
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [0, 360]}}
))

# Zeige das Tachometer in Streamlit
st.plotly_chart(fig)

bar = st.progress(0)
for i in range(3):
    time.sleep(1)
    bar.progress(i)


st.markdown("## Registrierung")
with st.form("User Registration"):
    col1,col2 = st.columns(2)
    f_name = col1.text_input("Vorname")
    l_name = col2.text_input("Nachname")
    st.text_input("email adresse")
    st.text_input("Passwort",type="password")
    day,month,year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state = st.form_submit_button("Senden")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please Fill above fields")
        else:
            st.success("Submitted Sucussfully")
            


# # Load the Lottie file from a URL
# url = "https://lottie.host/d61820d7-b543-4882-a08b-31593bd0b8dc/MLYrGpQ9GY.json"
# response = requests.get(url)
# if response.status_code != 200:
#     st.error("Error loading Lottie animation.")
# else:
#     lottie_json = response.json()
#     # Display the Lottie animation with a unique key
#     with st_lottie(key="unique_key"):
#         st.write("This is displayed while the animation is playing.")


