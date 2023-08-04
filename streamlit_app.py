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

    # tags names
    tag_names = ['.net','android','arrays','asp.net','c','c#','c++','css','database','django','git','html','ios','iphone','java','javascript','jquery','linux','mysql','objective-c','performance','php','python','ruby','ruby-on-rails','sql','sql-server','string','visual-studio','windows']
    
    # model
    model = joblib.load('model.pkl')

    # Preprocess the input question if needed
    processed_question = [question]  # Example of putting the question into a list; you may need to do more processing here depending on your model

    # Predict the tags
    predicted_values  = model.predict(processed_question)

    # Translate numerical predictions into tag names
    predicted_tags = [tag_names[i] for i in range(len(predicted_values[0])) if predicted_values[0][i] == 1]

    st.write('predicted_tags', predicted_tags)

st.write("Outside the form")
