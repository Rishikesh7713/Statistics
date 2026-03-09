import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Titanic Dataset.csv")

data.head(5)

data.dtypes

nominal_cat=["Name", "Ticket", "Cabin"]

ordinal_cat=["Embarked", "Gender"]

data["Gender"].value_counts()

gender_cat=["Female", "Male"]

data["Gender"] = pd.Categorical(data["Gender"], gender_cat, ordered=True)

median_index=np.median(data["Gender"].cat.codes)
median_gender=gender_cat[int(median_index)]
print(median_gender)

data["Embarked"].value_counts()

embarked_cat=["S", "C", "Q"]

data["Embarked"] = pd.Categorical(data["Embarked"], embarked_cat, ordered=True)

median_index=np.median(data["Embarked"].cat.codes)
median_embarked=embarked_cat[int(median_index)]
print(median_embarked)
