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
        {"role": "system", "content": "Your expertise in code review is invaluable. Thank you for diligently finding bugs, errors, and providing corrected code."},
        {"role": "user", "content": prompt}
      ]
    )
   

   
if response and response.choices:
    st.success("Code reviewed successfully!")
    st.subheader("Reviewed Python code:")
    st.write(response.choices[0].message.content)

