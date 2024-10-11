import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



filename = "./datasets/netflix_data.csv"

df = pd.read_csv(filename, nrows = 10)
df = pd.read_csv(filename)

last = df.tail(10)

index_max = df["imdb_score"].idxmax()
max_row = df.loc[index_max]

index_max = df["runtime"].idxmax()
max_row = df.loc[index_max]

print(max_row)

count_by_year = df['release_year'].value_counts()

year_max_count = count_by_year.idxmax()
max_count = count_by_year.max()

count_age_certification = df['age_certification'].value_counts()

df['decade'] = (df['release_year'] // 10) * 10


mean_scores = df.groupby(['decade', 'type'])['imdb_score'].mean().unstack()

colors = ['blue', 'orange']

plt.figure(figsize=(10, 5))
mean_scores.plot(kind='bar', color = colors)
plt.title('Average IMDb Scores by Decade')
plt.xlabel('Decade')
plt.ylabel('Average IMDb Score')
plt.xticks(rotation=0)
plt.ylim(0, 10)
plt.grid(axis='y')
plt.legend(title='Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
plt.close() 


votes_sum = df.groupby(['decade', 'type'])['imdb_votes'].sum().unstack()

colors = ['blue', 'green']

plt.close('all')

plt.figure(figsize=(10, 5))
votes_sum.plot(kind='bar', color=colors)
plt.title('Total IMDb Votes by Decade')
plt.xlabel('Decade')
plt.ylabel('Total IMDb Votes')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.legend(title='Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


     