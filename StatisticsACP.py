import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Bestsellers with categories.csv")

data.head()

median_year=np.median(data['Year'])
print("Median value of year : ", median_year)

mean_year=np.mean(data['Year'])
print("Mean age of year is : ", mean_year)

mode_rating=stats.mode(data["User Rating"])
print("Mode value of user rating : ", mode_rating)