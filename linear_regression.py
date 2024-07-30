# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PUVW-gxAZwJ8QF7_aYk0qpnz4mEvwGWP
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model

df = pd.read_csv("california_housing_train.csv")

print(df)

df.dropna(inplace=True)

xpoints=df["longitude"].values.reshape(-1,1)
ypoints=df["population"].values

x_train,x_test,y_train,y_test=train_test_split(xpoints,ypoints,test_size=0.1,random_state=42)

red=linear_model.LinearRegression()
red.fit(x_train,y_train)

ypoints_pred=red.predict(x_test)

plt.scatter(x_test,y_test,color="red",label="Actual")
plt.plot(x_test,ypoints_pred,color="blue", label="Predicted")
plt.xlabel("Longitude")
plt.ylabel("Population")
plt.title("Linear regression: longitude vs population")
plt.legend()
plt.show()