import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dt=pd.read_csv("Bestsellers with categories.csv")
dt.head(5)

dt.isnull().sum()

var_rating=np.var(dt["User Rating"])
print("Variance of Rating is : ",var_rating)
plt.show()

std_dev_year=np.std(dt["Year"])
print("Standard Deviation of Year is : ",std_dev_year)
plt.show()

plt.hist(dt["Price"], edgecolor="Green", color="b")
plt.xlabel("Name")
plt.ylabel("Price")
plt.show()