import streamlit as st
import joblib

st.write('Projet 5')

# question = st.text_input('Enter Your Question', '')
# st.write('Your Question is', question)

with st.form("my_form"):
   st.write("Enter Your Question")
   question = st.text_input('Enter Your Question')
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val, 'question', question)

st.write("Outside the form")
