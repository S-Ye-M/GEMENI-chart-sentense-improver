import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

st.title("Gemini AI Chat",anchor=False)
st.write("Hey buddy, what's on your mind? 😊")

user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Get Response", type="primary"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(user_prompt)
                st.success("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                
                
                
                
                
                
                
                #python -m streamlit run gemini_chat.py