import streamlit as st
import requests

st.title("AI Meme Poster Generator")

topic = st.text_input("Enter topic")
tone = st.selectbox("Select tone", ["Funny", "Sarcastic", "Motivational"])
mode = st.selectbox("Select mode", ["meme", "poster"])

if st.button("Generate"):

    response = requests.post(
        "http://127.0.0.1:8000/generate",
        json={"topic": topic, "tone": tone, "mode": mode}
    )

    st.write("Status Code:", response.status_code)
    st.write("Raw Response:", response.text)

    if response.status_code == 200:
        data = response.json()
        st.success(data.get("caption", "No caption"))
        st.image(data.get("image_path", ""))
    else:
        st.error("Backend Error")
