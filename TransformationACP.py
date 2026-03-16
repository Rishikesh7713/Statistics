import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Bestsellers with categories.csv")

data.head(5)

data.isnull().sum()

labels=["User Rating", "Reviews", "Price", "Year"]
for label in labels:
    print("Disrtibution of", label)
    sns.displot(data[label])
    plt.show()
    print("Skewness -", data[label].skew())

assosiation_1=pd.crosstab(data["User Rating"], data["Genre"])
print(assosiation_1)

assosiation_2=pd.crosstab(data["User Rating"], data["Price"])
print(assosiation_2)