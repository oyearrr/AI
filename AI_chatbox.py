import streamlit as st
import time
import ollama
#streamlit run /Users/skyler/Desktop/VScode/AI/AI_chatbox.py

client = ollama.Client(host = "http://localhost:11434")

if 'message' not in st.session_state:
    st.session_state['message'] = []

st.title("AI chatbox")
st.divider()

prompt = st.chat_input("Input your questions:")
if prompt:
    st.session_state['message'].append({"role":"user","content":prompt})
    for i in st.session_state['message']:
        st.chat_message(i['role']).markdown(i['content'])

    with st.spinner("Thinking..."):
        response = client.chat(
            model = "deepseek-r1:32b",
            messages = [{"role":"user","content":prompt}]
        )
        st.session_state['message'].append({"role":"assistant","content":response['message']['content']})
        st.chat_message("assistant").markdown(response['message']['content'])