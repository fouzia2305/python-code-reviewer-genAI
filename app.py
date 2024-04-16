from openai import OpenAI
import streamlit as st

st.title("🤖 Python Code Reviewer - Let AI Improve Your Code 🚀")

f = open("keys/.openai_api_key.txt")
key = f.read()

client = OpenAI(api_key = key)

prompt=st.text_input("Enter your Python code here:")

response=None
if st.button("Review code")==True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )
   

   
if response and response.choices:
    st.success("Code reviewed successfully!")
    st.subheader("Reviewed Python code:")
    st.write(response.choices[0].message.content)

