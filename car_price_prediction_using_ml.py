# -*- coding: utf-8 -*-
"""Car_Price_Prediction_Using_ML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BLkfRO8PMO9YAMT8Bg6l1oBpMDP0CM6o
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("CarPrice.csv")
df

df.head()

df.tail()

df = df.drop(["car_ID"],axis=1)
df

df.info()

df.isnull().sum()

df.shape

df.describe()

print(df.CarName.unique())

df.fueltype.value_counts()

df.aspiration.value_counts()

df.doornumber.value_counts()

df.carbody.value_counts()

df.drivewheel.value_counts()

df.enginelocation.value_counts()

df.fuelsystem.value_counts()

sns.set_style("whitegrid")
plt.figure(figsize=(7,5))
sns.distplot(df.price)
plt.show()

#diag_kind="kde": This argument sets the kind of plot for the diagonal subplots. Here, it’s set to “kde”, which stands for Kernel Density Estimation, a technique for smoothing a histogram.
#diag_kws=dict(shade=True, bw=.05, vertical=False): This argument allows you to pass additional keyword arguments to the function used to draw the diagonal subplots. Here, shade=True means that the area under the KDE curve will be filled. bw=.05 sets the bandwidth of the kernel. vertical=False means that the KDE is horizontal.
plt.figure(figsize=(9,9))
sns.pairplot(df,diag_kind="kde",diag_kws=dict(shade=True, bw=.05, vertical=False))
plt.show()

x = df.drop(['price', 'CarName', 'fueltype', 'aspiration',	'doornumber', 'carbody',	'drivewheel', 'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem'], axis=1)
x

y=df["price"]
y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1234)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_train)
y_pred

y_train

y_pred1=model.predict(x_test)
y_pred1

from sklearn import metrics

error_square=metrics.r2_score(y_train,y_pred)
print("Error Square is :",error_square)

plt.scatter(y_train,y_pred)
plt.xlabel("Actual Values",fontsize=12)
plt.ylabel("Predicted Values",fontsize=12)
plt.title("Actual vs Predicted",fontsize=16)
plt.show()

from sklearn.linear_model import Lasso
modell=Lasso()
modell.fit(x_train,y_train)

y_pred2=modell.predict(x_train)
y_pred2

error_square2=metrics.r2_score(y_train,y_pred2)
print("error_square using Lasso:",error_square)

plt.scatter(y_train,y_pred2)
plt.xlabel("Actual Values",fontsize=12)
plt.ylabel("Predicted Values",fontsize=12)
plt.title("Actual vs Predicted",fontsize=16)
plt.show()

from sklearn.linear_model import Ridge
model2=Ridge()
model2.fit(x_train,y_train)

y_pred3=model2.predict(x_train)
y_pred3

error_square3=metrics.r2_score(y_train,y_pred3)
print("error square using Ridge is:",error_square3)

plt.scatter(y_train,y_pred3)
plt.xlabel("Actual Values",fontsize=12)
plt.ylabel("Predicted Values",fontsize=12)
plt.title("Actual vs Predicted",fontsize=16)
plt.show()