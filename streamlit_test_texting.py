import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a test of my Streamlit setup for Build with AI 2025.")

name = st.text_input("What's your name?", key="intro_name")
if name:
    st.write(f"Hello, {name}!")

pangit = st.text_input("Pangit ka sabihin mo bakit", key="pangit1")
if pangit:
    st.write("omsim shongit ka tlga")

st.title("Okay ito serious mode, HAPPY BIRTHDAY MISHA")
st.write("Testing ko ito kasi pupunta ako ng Build AI bukas.")

name1 = st.text_input("What's your name again?", key="birthday_name")
if name1:
    if name1.lower() == 'misha':
        st.write("🎉 HAPPY BIRTHDAY MISHA!!!! 🎉")
    else:
        st.write(f"HUH {name1.upper()}?! ALAM MO BANG BIRTHDAY NI MISHA NGAUN?! 🎂")