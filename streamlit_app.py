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
    
    # model
    model = joblib.load('model.pkl')
    multilab_bin = joblib.load('multilab_bin2')

    # Preprocess the input question if needed
    processed_question = [question]  # Example of putting the question into a list; you may need to do more processing here depending on your model

    # Predict the tags
    predicted_values  = model.predict(processed_question)

    # Translate numerical predictions into tag names
    predicted_tags = multilab_bin.inverse_transform(predicted_values)
    st.write('predicted_tags', predicted_tags)

    st.write('multilab_bin', multilab_bin.classes_)

st.write("Outside the form")
