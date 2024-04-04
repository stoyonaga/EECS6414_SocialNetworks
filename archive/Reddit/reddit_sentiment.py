import praw
import pandas as pd
import random
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

keep = ['id', 'subreddit.id', 'subreddit.name', 'created_utc', 'body', 'sentiment', 'score']

df_final = pd.DataFrame()
for x in range(15):
    
    print(x)
    df_adding = pd.read_csv("C:/Users/aarykary/Desktop/the-reddit-covid-dataset-comments.csv", nrows= 4000, skiprows = range(1, (x+1) * 1000000), engine = "python" )
    df_final = pd.concat([df_final, df_adding])
print(df_final.columns)
df_final.to_csv("reddit_final_data_frame.csv")
#df = df[keep]
sentiment_distribution_over_months = {
    "January": [0,0,0],
    "February": [0,0,0],
    "March": [0,0,0],
    "April": [0,0,0],
    "May": [0,0,0],
    "June": [0,0,0],
    "July": [0,0,0],
    "August": [0,0,0],
    "September": [0,0,0],
    "October": [0,0,0],
    "November": [0,0,0],
    "December": [0,0,0],
}

 


for index, row in df_final.iterrows():
    #print(datetime.utcfromtimestamp(row["created_utc"]).month)
    #distribution_over_months[datetime.utcfromtimestamp(row["created_utc"]).month] += 1
    
    if row['sentiment'] > 0.25:
        #print(datetime.utcfromtimestamp(row["created_utc"]).strftime('%B'))
        
        sentiment_distribution_over_months[datetime.utcfromtimestamp(row["created_utc"]).strftime('%B')][2] += 1
    elif row['sentiment'] < - 0.25: 
         

        sentiment_distribution_over_months[datetime.utcfromtimestamp(row["created_utc"]).strftime('%B')][1] += 1
    else:
         

        sentiment_distribution_over_months[datetime.utcfromtimestamp(row["created_utc"]).strftime('%B')][0] += 1

print(sentiment_distribution_over_months)


keys = list(sentiment_distribution_over_months.keys())
values = list(sentiment_distribution_over_months.values())

input_final_list = []
counter = 0

months = keys

negatives = []
neutrals = []
positives = []
for x in values:
    negatives.append(x[0])
    neutrals.append(x[1])
    positives.append(x[2])
    


# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size
 
index = range(len(months))
plt.bar(index, negatives, width=0.25, label='Negative')
plt.bar([i + 0.25 for i in index], neutrals, width=0.25, label='Neutral')
plt.bar([i + 0.5 for i in index], positives, width=0.25, label= 'Positive')

# Adding labels and title
plt.xlabel('Months')
plt.ylabel('Values')
plt.title("Distribution of Reddit comment sentiment over months")
plt.xticks([i + 0.25 for i in index], months, rotation=45)
plt.legend()
plt.style.use("dark_background")
# Display plot
plt.tight_layout()
plt.show()







