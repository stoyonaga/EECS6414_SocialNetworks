import streamlit as st
import os 
import time
import warnings 

# Package Finetuning
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title='Twitter Dashboard',
    page_icon=':bird:',
    layout='wide'
)

if __name__ == '__main__':
    st.header(
        body = 'Large Language Model (QA) Dashboard',
        divider = 'rainbow'
    )
    prompt = st.text_input(
        label = 'Ask me a question!'
    )

    st.subheader(
        body = 'Resources',
        divider='rainbow'   
    )

    st.page_link("twitter-dashboard.py", label="Twitter", icon="🐦")
    st.page_link("pages\\reddit-dashboard.py", label="Reddit", icon="🅱️")
    st.page_link("pages\\qa.py", label="QA Dashboard", icon="🤖")



