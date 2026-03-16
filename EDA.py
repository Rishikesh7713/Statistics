import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Titanic Dataset.csv")

data.head(5)

sns.countplot(x="Gender", hue="Survived", data=data)
plt.show()

sns.countplot(x="Pclass", hue="Survived", data=data)
plt.show()

sns.displot(data["Age"], kde=False, bins=40)
plt.show()

sns.countplot(x="Gender", data=data)
plt.show()

sns.countplot(x="Survived", hue="SibSp", data=data, palette="mako")
plt.show()

sns.countplot(x="Survived", hue="Parch", data=data, palette="mako")
plt.show()

sns.displot(data["Fare"])
plt.show()

sns.boxplot(x="Pclass", y="Age", data=data, palette="winter")
plt.show()

sns.heatmap(data.corr())
plt.show()