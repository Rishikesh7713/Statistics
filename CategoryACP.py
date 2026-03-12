import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Titanic Dataset.csv")

data.isnull().sum()

data.head(5)

median=np.median(data["Genre"])
print(median)

sns.barplot(data["Genre"])
plt.show()

