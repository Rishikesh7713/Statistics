import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Titanic Dataset.csv")

data.head(5)

min_age=data["Age"].min()
print("Minimum Age : ", min_age)

max_age=data["Age"].max()
print("Maximum Age : ", max_age)

bins=[0, 15, 30, 45, 60, 75]

data['Age'] = data['Age'].fillna(data['Age'].median())

data["binned_age"]=pd.cut(data["Age"], bins)

print(data[["binned_age", "Age"]].head())

age_labels=["Young", "Young", "Adult", "Middle Age", "Middle Older Age", "Senior"]

data["binned_age"].value_counts().plot(kind="bar")

plt.title("Dance Class Age Distribution")
plt.xlabel("Ages")
plt.ylabel("Count")
plt.show()

labels=["PassengerId", "Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
for label in labels:
    print("Disrtibution of", label)
    sns.displot(data[label])
    plt.show()
    print("Skewness -", data[label].skew())

data["log_SibSp"]=np.log(data["SibSp"])
data["log_Parch"]=np.log(data["Parch"])
data["log_Fare"]=np.log(data["Fare"])