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




# Package Finetuning
warnings.filterwarnings('ignore')
tqdm.pandas()

#
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
#

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
    return tweets

def plot_sentiment_of_month() -> px.pie:
    tbm = tweets.loc[tweets['date'] == month]
    sentiment = Counter(tbm['sentiment'])
    fig = px.pie(
        data_frame = tbm,
        names = sentiment.keys(),
        values = sentiment.values(),
        title = f'Sentiment of Tweets in {month}',
        height=400,
        width=400 
    )
    return fig

def plot_hashtags_of_month() -> None:
    timeseries = dict.fromkeys(months.keys(), 0)
    ts_month = tweets.loc[tweets['date'] == month]
    hashtags = []
    for entry in ts_month['hashtags']:
        if str(entry).strip() != 'None':
            hashtags += ast.literal_eval(entry.lower())
        else:
            hashtags.append('none')
    hashtag_count = Counter(hashtags)
    hashtags = dict(hashtag_count.most_common(10))
    fig = px.bar(
        data_frame = ts_month,
        y = hashtags.keys(),
        x = hashtags.values(),
        labels = {
            'y': 'Hashtag',
            'x': 'Count'
        },
        orientation = 'h',
        title = 'Top Used Hashtags in {Month}',
        height=400,
        width=400
        
    )
    return fig

def plot_posting_users_of_month() -> None:
    tbm = tweets.loc[tweets['date'] == month]
    users = dict(Counter(tbm['username']).most_common(10))
    fig = px.bar(
        x = users.keys(),
        y = users.values(),
        labels = {
            'x': 'Usernames (@)',
            'y': 'Number of Posts'
        },
        title = 'Most Active Posting Users',
    )
    return fig

def plot_tagged_users_of_month() -> None:
    tbm = tweets.loc[tweets['date'] == month]
    top_users = Counter(tbm['reply_to']).most_common(11)
    users = {}
    for entry in top_users:
        if ast.literal_eval(entry[0]) != list():
            users[entry[0]] = entry[1]
    fig = px.bar(
        x = users.keys(),
        y = users.values(),
        labels = {
            'x': 'Usernames (@)',
            'y': 'Number of Mentions'
        },
        title = 'Most Tagged Users',
    )
    return fig

def plot_validity_of_month() -> None:
    tbm = tweets.loc[tweets['date'] == month]
    validity = Counter(tbm['validity'])
    fig = px.pie(
        data_frame = tbm,
        names = validity.keys(), 
        values = validity.values(),
        height = 400,
        width = 400
        )
    return fig

def wordcloud_tweets() -> WordCloud:
    tbm = tweets.loc[tweets['date'] == month]
    wv_all_tweets = WordCloud(
        background_color='white',
        width=400,
        height=400,
        stopwords=set(STOPWORDS),
        max_words=1000,
        min_font_size=12,
        random_state=2
    )
    wv_all_tweets.generate(' '.join(tbm['tweet']))
    return wv_all_tweets

def plot_power_law_distribution() -> px.scatter:
  # If the majority of the scatter is a straight line, we are straight vibin'

  degrees = []
  power_fit = powerlaw.Fit([x[1] for x in G.degree])
  for node, degree in G.degree:
    degrees.append(degree)
  degrees = Counter(degrees)
  fig = px.scatter(
    x = degrees.keys(),
    y = degrees.values(),
    title = f'Log Distribution of Graph (Alpha = {round(power_fit.alpha, 2)})',
    labels = {
      'x': 'Node Degree',
      'y': 'Probability: p(k) = P(X = k)'
    },
    height=600
  )
  fig.update_xaxes(type='log')
  fig.update_yaxes(type='log')
  return fig

def calculate_pagerank() -> str:
    top_k_scored_users = sorted(nx.pagerank(G).items(), key = lambda x:x[1], reverse=True)
    results = ''
    for i in range(10):
        results += f'@{top_k_scored_users[i][0]} ({round(top_k_scored_users[i][1], 4)})\n'
    return results
def calculate_hubs() -> str:
    hubs = sorted(nx.hits(G)[0].items(), key = lambda x:x[1], reverse=True)
    results = ''
    for i in range(10):
        results += f'@{hubs[i][0]} ({round(hubs[i][1], 4)})\n'
    return results
def calculate_authorities() -> str:
    authorities = sorted(nx.hits(G)[1].items(), key = lambda x:x[1], reverse=True)
    results = ''
    for i in range(10):
        results += f'@{authorities[i][0]} ({round(authorities[i][1], 4)})\n'
    return results



# ------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(
    page_title='Twitter Dashboard',
    page_icon=':bird:',
    layout='wide'
)

if __name__ == '__main__':
    with st.spinner('Please wait while resources are being generated...'):
        # DataLoader & Configuration
        tweets = load_dataset()
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

    st.subheader(
        body = 'Text-based Analytics & Visualizations',
        divider = 'rainbow'
    )

    month = st.selectbox(
        label = 'Please select a month',
        options = months.values()
    )

    assets = st.container()
    with assets:
        # Row 1 
        sentiment, hashtags = st.columns(2)
        with sentiment:
            st.plotly_chart(figure_or_data=plot_sentiment_of_month())
        with hashtags:
            st.plotly_chart(figure_or_data=plot_hashtags_of_month())
        # Row 2 
        posts, tags = st.columns(2)
        with posts:
            st.plotly_chart(figure_or_data=plot_posting_users_of_month(),
                            use_container_width=True)
        with tags:
            st.plotly_chart(figure_or_data=plot_tagged_users_of_month(),
                            use_container_width=True)
        # Row 3 
        wc, validity = st.columns(2)
        with wc:
            st.write(wordcloud_tweets().to_image())
        with validity:
            st.plotly_chart(figure_or_data=plot_validity_of_month())
    
    st.subheader(
        body = 'Graph Analytics & Visualization',
        divider = 'rainbow'
    )

    gexf_file = st.radio(
        'Select gexf file:',
        [
         'gexf\\vaccine_tweets_whole_graph.gexf',
         'gexf\\vaccine_tweets_misinformation_graph.gexf'
         ]
    )

    G = nx.read_gexf(gexf_file)
    graph_assets = st.container()
    with graph_assets:
        image, pl = st.columns(2)
        with image:
            if gexf_file == 'gexf\\vaccine_tweets_whole_graph.gexf':
                st.image('images\\vaccines_whole.png')
            else:
                st.image('images\\vaccines_misinformation.png')
            st.write(f'Nodes: {G.number_of_nodes()}')
            st.write(f'Edges: {G.number_of_edges()}')
        with pl:
            st.write(plot_power_law_distribution())
    pagerank, authorities, hubs = st.columns(3)
    with pagerank:
        txt = st.text_area(
            label = 'Pagerank',
            value = calculate_pagerank(),
            height = 250
        )
    with authorities:
        txt = st.text_area(
            label = 'Authorities',
            value = calculate_authorities(),
            height = 250
        )
    with hubs:
        txt = st.text_area(
            label = 'Hubs',
            value = calculate_hubs(),
            height = 250
        )
    
    st.subheader(
        body = 'LLM QA',
        divider = 'rainbow'
    )

    st.subheader(
        body = 'Resources',
        divider='rainbow'   
    )

    st.page_link("twitter-dashboard.py", label="Twitter", icon="🐦")
    st.page_link("pages\\reddit-dashboard.py", label="Reddit", icon="🅱️")
    st.page_link("pages\\qa.py", label="QA Dashboard", icon="🤖")


   




