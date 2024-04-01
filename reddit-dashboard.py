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


st.set_page_config(
    page_title='Reddit Dashboard',
    page_icon=':bird:',
    layout='wide'
)

 st.header(
        body = 'GS/EECS 6414 Twitter Dashboard',
        divider='rainbow'
        )

 month = st.selectbox(
        label = 'Please select a month',
        options = months.values()
    )

