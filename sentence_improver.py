import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

st.title( "Sentance Improver",anchor=False)
st.write("Enter a sentence and get a professional version! 😊")

user_sentence = st.text_area("Enter your sentence:", height=150)

if st.button("Improve Sentence", type="primary"):
    if not user_sentence.strip():
        st.warning("Please enter a sentence.")
    else:
        with st.spinner("Improving..."):
            try:
                prompt = f'Improve this sentence professionally: "{user_sentence}"'
                response = model.generate_content(prompt)
                st.success("Improved Sentence:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                
                
                
                
                
                
                #python -m streamlit run sentence_improver.py
                
                