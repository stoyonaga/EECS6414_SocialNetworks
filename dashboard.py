# ----- Required Packages (GUI & Visualizations) -----
import streamlit as st
import os 
import warnings 
import plotly.express as px 
from wordcloud import WordCloud, STOPWORDS
# ----- Data Analytics -----
import pandas as pd 
from tqdm import tqdm
from collections import Counter
import networkx as nx
import ast



# Package Finetuning
warnings.filterwarnings('ignore')
tqdm.pandas()

def load_dataset() -> None:
    # Load initial dataset to dataframe
    tweets = pd.read_parquet('datasets\\UPDATED_vaccine_tweets.parquet.gzip')
    months = {
        # '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October'
        # '11': 'November',
        # '12': 'December'
    }
    # Extract Month from Date Column and Convert into Month Only
    tweets_ts= tweets['date'].progress_apply(lambda x: months[x[5:7]])
    # Apply New Date Format to Dataframe
    tweets['date'] = tweets_ts


st.set_page_config(
    page_title='Twitter Dashboard',
    page_icon=':bird:',
    layout='wide'
)

if __name__ == '__main__':
    pass

