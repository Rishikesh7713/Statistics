import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("IMDB Dataset (2).csv")

data.head(5)

data.isnull().sum()

plt.hist(data["Runtime"])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

plt.hist(data["IMDB_Rating"])
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.show()

data["Runtime"].unique()

bins_time=np.arange(80, 230, 10)
plt.hist(data["Runtime"], edgecolor="black", bins=bins_time, color="g")
plt.ylabel("Count of Movies")
plt.xlabel("Runtime")
plt.show()

data["IMDB_Rating"].unique()

bins_rating=np.arange(8, 10, 0.20)
plt.hist(data["IMDB_Rating"], edgecolor="black", bins=bins_rating, color="g")
plt.ylabel("Countof Movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)
plt.show()