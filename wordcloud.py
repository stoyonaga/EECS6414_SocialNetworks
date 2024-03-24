import pandas as pd
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/aarykary/Desktop/the-reddit-covid-dataset-posts.csv", nrows = 38000, encoding = 'utf-8')
print(df.columns)
all_text = ""
for row in df.itertuples():
    all_text = all_text + str(row.selftext)


wc_comments = WordCloud(
    background_color='white',
    width=800,
    height=800,
    stopwords=set(STOPWORDS),
    max_words=1000,
    min_font_size=12,
    random_state=2).generate(all_text)
 
plt.figure(figsize = (10,5))
plt.imshow(wc_comments)