import praw
import pandas as pd
import random
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from nltk.sentiment.vader import SentimentIntensityAnalyzer


df = pd.read_csv("C:/Users/aarykary/reddit_final_data_frame.csv")
sentiment_analyze = SentimentIntensityAnalyzer()

word_clouds = {
    'January': '',
    'February': '',
    'March': '',
    'April': '',
    'May': '',
    'June': '',
    'July': '',
    'August': '',
    'September': '',
    'October': '',
    'November': '',
    'December': ''
}

months_counter = {
    'January': [0,0,0],
    'February': [0,0,0],
    'March': [0,0,0],
    'April': [0,0,0],
    'May': [0,0,0],
    'June': [0,0,0],
    'July': [0,0,0],
    'August': [0,0,0],
    'September': [0,0,0],
    'October': [0,0,0],
    'November': [0,0,0],
    'December': [0,0,0]
}

def monthly_sentiment(df):
    
    for index,row in df.iterrows():
        
        if row['sentiment'] >= 0.05:
            months_counter[datetime.utcfromtimestamp(row["created_utc"]).strftime("%B")][2] += 1
        elif row['sentiment'] <= -0.05:
            months_counter[datetime.utcfromtimestamp(row["created_utc"]).strftime("%B")][0] += 1
        else:
            months_counter[datetime.utcfromtimestamp(row["created_utc"]).strftime("%B")][1] += 1

       
        #print(index)
        word_clouds[datetime.utcfromtimestamp(row["created_utc"]).strftime("%B")] += str(row['body'])

    for key in word_clouds.keys():
        if word_clouds[key] == '' or len(list(word_clouds[key])) < 5:
            word_clouds[key] += "Covid conspiracy fauci vax false"
    print(months_counter)
    
    
    for key in months_counter.keys():
        current = months_counter[key]
        if current == [0,0,0]:
            current = [0,1,0]
        
        plt.title(key)
        plt.pie(current, labels = ['Negative', 'Neutral', 'Positive'], shadow = True)
        plt.legend(bbox_to_anchor = (1.1,1))
        plt.savefig(key + "_pie.png")
        plt.show()
        
    for key in word_clouds.keys():
        wc = WordCloud(
    background_color='white',
    width=800,
    height=800,
    stopwords=set(STOPWORDS),
    max_words=1000,
    min_font_size=12,
    random_state=2).generate(word_clouds[key])
        plt.figure(figsize = (10,5))
        plt.legend()
        plt.imshow(wc)
        plt.title(key)
        
        
        wc.to_file(key + "_wc.png")
monthly_sentiment(df)