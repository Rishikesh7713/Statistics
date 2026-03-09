import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Bestsellers with categories.csv")

data.head(5)

data.isnull().sum()

pri_q1=np.quantile(data["Price"], 0.25)
pri_q2=np.quantile(data["Price"], 0.50)
pri_q3=np.quantile(data["Price"], 0.75)

print("Price Quartiles : ")
print("Q1 : ",pri_q1)
print("Q2 : ",pri_q2)
print("Q3 : ",pri_q3)

IQR_pri=pri_q3-pri_q2
print("Interquartile Range of Price : ",IQR_pri)