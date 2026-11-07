from google.colab import files 
upload = files.upload()

import pandas as pd 
df = pd.read_csv('bowling_stats.csv')
print(df.head())

import pandas as pd 
df = pd.read_csv('batting_stats.csv')
print(df.head())

import pandas as pd
top5 = df.sort_values(by='sixes', ascending=False).head(5)
print(top5)
