from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
llm = OpenAI()
# result = llm.predict("hi")
# print(result)





import streamlit as st
import time

st.title('인공지능 시인')

contents = st.text_input("poet title", "......")
# st.write("The current poet title is", contents)


if st.button("시 작성"):    
    with st.spinner('Wait for it...'):
        time.sleep(3)
        st.write(contents)
