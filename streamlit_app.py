import streamlit as st

st.write('Hello world!')

user_input = st.text_input("Enter your question here")

if st.button('Predict'):
  st.write('Tags')
