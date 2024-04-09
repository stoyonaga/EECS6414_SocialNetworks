import streamlit as st
import os 
import time
import warnings 
# Large Language Model 
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
# Package Finetuning
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title='Twitter Dashboard',
    page_icon=':bird:',
    layout='wide'
)

def generate_prompt():
    response = generator(
        # Multinomial Sampling
        prompt,
        max_length=125,
        num_return_sequences=1,
        early_stopping=True,
        temperature=0.7,
        repetition_penalty=10.0,
        do_sample=True,
        num_beams=10,
        top_p=0.90,
        remove_invalid_values=True,
        truncation=True
    )
    for word in response[0]['generated_text'].split(" "):
        yield word + " "
        time.sleep(0.02)


if __name__ == '__main__':
    st.header(
        body = 'Large Language Model (QA) Dashboard',
        divider = 'rainbow'
    )
    prompt = st.text_input(
        label = 'Ask me a question!'
    )

    
    with st.spinner('Please wait while resources are being generated...'):
        tokenizer = AutoTokenizer.from_pretrained('model')
        model = AutoModelForCausalLM.from_pretrained('model')
        generator = pipeline(
            'text-generation',
            model = model,
            tokenizer = tokenizer
        )
        time.sleep(5)
    
    st.write_stream(generate_prompt())
    


    st.subheader(
        body = 'Resources',
        divider='rainbow'   
    )

    st.page_link("twitter-dashboard.py", label="Twitter", icon="🐦")
    st.page_link("pages\\reddit-dashboard.py", label="Reddit", icon="🅱️")
    st.page_link("pages\\qa.py", label="QA Dashboard", icon="🤖")
