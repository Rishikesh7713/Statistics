import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Iris Dataset (1).csv")

data.head(5)

data.isnull().sum()

data.describe()

labels=["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
for label in labels:
    print("Distribution of :", label)
    sns.boxplot(data[label])
    plt.show()



labels=["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
for label in labels:
    print("Distribution of :", label)
    sns.displot(data[label])
    plt.show()

labels=["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
for label in labels:
    print("Skewness of  :", label)
    print(data[label].skew())