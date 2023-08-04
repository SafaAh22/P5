import streamlit as st
import joblib

st.write('Projet 5')

# question = st.text_input('Enter Your Question', '')
# st.write('Your Question is', question)

with st.form("my_form"):
   st.write("Enter Your Question")
   question = st.text_input('Enter Your Question')


   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       model = joblib.load('model.pkl')
       tags = model.predict(question)
       st.write('question', question)

st.write("Outside the form")
