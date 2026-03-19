import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("StudentsPerformance.csv")

data.head(5)

data.isnull().sum()

sns.histplot(x="mathscore", data=data, kde=True)
plt.show()

race_counts = data['race/ethnicity'].value_counts()
plt.pie(race_counts, data=data)
plt.show()

sns.boxplot(x="gender", y="math score", data=data)
plt.show()