import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Titanic Dataset.csv")
data.head(5)

data.dtypes

data.isnull().sum()