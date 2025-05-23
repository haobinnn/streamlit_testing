import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a test of my Streamlit setup for Build with AI 2025.")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

pangit = st.text_input("Pangit ka sabihin mo bakit")
if pangit:
    st.write("omsim shongit ka tlga")