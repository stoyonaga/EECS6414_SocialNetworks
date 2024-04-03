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
subreddits = ["AntiVaccineMemes", "VaccineHomicide", "VaccinesCause", "VaccineGasLight", "VaccineCultVictims"]

def get_key_figures(subreddit):
    graph = nx.read_gexf("Reddit_Graphs/" + subreddit + "_graph.gexf")
    pr = nx.pagerank(graph)
    top_10_pr = sorted(pr.items(), key = lambda x: x[1], reverse = True)[:10]
    hubs, auth = nx.hits(graph)
    top_10_hubs = sorted(hubs.items(), key = lambda x: x[1], reverse = True)[:10]
    top_10_auth = sorted(auth.items(), key = lambda x: x[1], reverse = True)[:10]
    st.table([{'User': user, "Pagerank score contribution": contribution} for user, contribution in top_10_pr])
    st.table([{'User': user, "Hubs score contribution": contribution} for user, contribution in top_10_hubs])
    st.table([{'User': user, "Authorities score contribution": contribution} for user, contribution in top_10_auth])


def all_images(month):
    #image = Image.open("Reddit_results/" + month + "_wc.png")
    st.title("WordCloud")
    st.image("Reddit_results/" + month + "_wc.png", width=500)
    st.title("Sentiment Pie Chart")
    st.image("Reddit_results/" + month + "_pie.png", width = 500)
def subreddit_images(subreddit):
    st.title("Common malicious subreddits between users")
    st.image("Reddit_results/" + subreddit + ".png", width=500)
if __name__ == '__main__':
    with st.spinner('Please wait while resources are being generated...'):
        # DataLoader & Configuration
      
        time.sleep(2)
        #
    
    st.header(
        body = 'GS/EECS 6414 Reddit Dashboard',
        divider='rainbow'
        )
    st.write(
        """
        The goal of our project is to create a robust multifold analytics and visualization system for COVID misinformation 
        in Reddit. Firstly, we will analyze several datasets which contain social media posts about COVID-19 in addition to 
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
    st.title("Sentiment Analysis")
    month = st.selectbox(
            label = 'Please select a month', 
            options = months
        )

    

    all_images(month)

    subreddit = st.selectbox(
        label = 'Please select a subreddit', 
        options = subreddits
    )

    subreddit_images(subreddit)
    get_key_figures(subreddit)
    st.page_link("twitter-dashboard.py", label="Twitter", icon="🐦")
    st.page_link("pages\\reddit-dashboard.py", label="Reddit", icon="🅱️")
    st.page_link("pages\\qa.py", label="QA Dashboard", icon="🤖")
