import pandas as pd
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)
ratings_file = os.path.join(dirname, 'ml-20m/ratings.csv')
ratings = pd.read_csv(ratings_file)

ax1 = ratings.hist(column='rating', figsize=(10, 10))
plt.ylabel('Count (M)')
plt.xlabel('Rating (0 - 5)')
plt.title('User\'s Movie Ratings')
img_output = os.path.join(dirname, 'ratings_histogram.png')
plt.savefig(img_output)

stats_output = os.path.join(dirname, 'ratings-statistics.txt')
stats_output = open(stats_output, 'w')
stats_output.write(ratings['rating'].describe().to_string())
stats_output.close()
