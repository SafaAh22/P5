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
        # Preprocess the input question if needed
    processed_question = [question]  # Example of putting the question into a list; you may need to do more processing here depending on your model

    # Predict the tags
    predicted_tags = model.predict(processed_question)
    st.write('question', question)

st.write("Outside the form")
