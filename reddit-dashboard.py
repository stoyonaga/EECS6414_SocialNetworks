# ----- Required Packages (GUI & Visualizations) -----
import streamlit as st
import os 
import time
import warnings 
import plotly.express as px 
from wordcloud import WordCloud, STOPWORDS
# ----- Data Analytics -----
import pandas as pd 
from tqdm import tqdm
from collections import Counter
import networkx as nx
import powerlaw
import ast
import praw 
import networkx as nx
import pandas as pd
import nltk
from datetime import datetime
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud, STOPWORDS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from PIL import Image

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def all_images(month):
    #image = Image.open("Reddit_results/" + month + "_wc.png")
    st.image("Reddit_results/" + month + "_wc.png")
    st.image("Reddit_results/" + month + "_pie.png")
if __name__ == '__main__':
    with st.spinner('Please wait while resources are being generated...'):
        # DataLoader & Configuration
      
        time.sleep(2)
        #
    
    st.header(
        body = 'GS/EECS 6414 Twitter Dashboard',
        divider='rainbow'
        )
    st.write(
        """
        The goal of our project is to create a robust multifold analytics and visualization system for COVID misinformation 
        in Twitter. Firstly, we will analyze several datasets which contain social media posts about COVID-19 in addition to 
        user-level demographics (i.e., Number of Followers, Biography, etc.,). From this, we will apply NLP techniques which augment 
        the available datasets for data mining and visualization purposes. 


        Secondly, we will create directed social networks with malicious posts and tagged users to determine how misinformation travels. 
        The resulting network characteristics will be reported in the methodology section. Using these characteristics, we will determine what 
        null model most closely corresponds to our social networks.
        

        Lastly, through the process of data analytics, graph visualization, and pattern recognition, we seek to answer the 
        following research questions based on various subgraph motifs:

        1. Which users participate the most in the dissemination of misinformation?
        2. What NLP-based patterns can be drawn from users who spread misinformation?
        3. How is misinformation propagated in terms of a longitudinal time frame?
        4. What are notable similarities and differences in how misinformation spreads between Twitter and Reddit?
        """,
        unsafe_allow_html= False,
    ) 
 

    st.header(
            body = 'GS/EECS 6414 Reddit Dashboard',
            divider='rainbow'
            )

    month = st.selectbox(
            label = 'Please select a month', 
            options = months
        )
    all_images(month)

