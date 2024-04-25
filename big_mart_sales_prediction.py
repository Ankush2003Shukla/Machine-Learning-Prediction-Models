# -*- coding: utf-8 -*-
"""Big_Mart_Sales_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_ArXh3D2kFjxAaR85FOEJcpBbiItBQIy

**Problem Statement**

Make a ML model to predict the Big_Mart_Sales
"""

#importing the dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

#loading the dataset
dataset = pd.read_csv('/content/big_mart_data.csv')

#printing the first five rows
dataset.head()

#getting the rows and columns of the dataset
dataset.shape

#getting some info about the dataset
dataset.info()

#checking the null values
dataset.isnull().sum()

# mean value of "Item_Weight" column
dataset['Item_Weight'].mean()

dataset['Item_Weight'].fillna(dataset['Item_Weight'].mean(), inplace=True)

#checking the null values again
dataset.isnull().sum()

dataset['Outlet_Size'].mode()

mode_of_Outlet_size = dataset.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=(lambda x: x.mode()[0]))

print(mode_of_Outlet_size)

miss_values = dataset['Outlet_Size'].isnull()

print(miss_values)

dataset.loc[miss_values, 'Outlet_Size'] = dataset.loc[miss_values,'Outlet_Type'].apply(lambda x: mode_of_Outlet_size[x])

#checking the null values again
dataset.isnull().sum()

dataset.head()

#getting some statistical measures of the dataset
dataset.describe()

#Numerical Features
sns.set()
plt.figure(figsize=(6,6))
sns.displot(dataset['Item_Weight'])
plt.show()

#Numerical Features
sns.set()
plt.figure(figsize=(6,6))
sns.displot(dataset['Item_Visibility'])
plt.show()

#Numerical Features
sns.set()
plt.figure(figsize=(6,6))
sns.displot(dataset['Item_MRP'])
plt.show()

#Numerical Features
sns.set()
plt.figure(figsize=(6,6))
sns.displot(dataset['Item_Outlet_Sales'])
plt.show()

sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x ='Outlet_Establishment_Year',data=dataset)
plt.show()

sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x ='Item_Fat_Content',data=dataset)
plt.show()

dataset['Item_Fat_Content'].value_counts()

dataset.replace({'Item_Fat_Content':{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'}},inplace=True)

dataset['Item_Fat_Content'].value_counts()

sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x ='Item_Fat_Content',data=dataset)
plt.show()

sns.set()
plt.figure(figsize=(30,10))
sns.countplot(x ='Item_Type',data=dataset)
plt.show()

sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x ='Outlet_Size',data=dataset)
plt.show()

sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x ='Outlet_Establishment_Year',data=dataset)
plt.show()

#implementing Label Encoding
encoder = LabelEncoder()
dataset['Item_Fat_Content'] = encoder.fit_transform(dataset['Item_Fat_Content'])
dataset['Item_Type'] = encoder.fit_transform(dataset['Item_Type'])
dataset['Item_Identifier'] = encoder.fit_transform(dataset['Item_Identifier'])
dataset['Outlet_Identifier'] = encoder.fit_transform(dataset['Outlet_Identifier'])
dataset['Outlet_Size'] = encoder.fit_transform(dataset['Outlet_Size'])
dataset['Outlet_Location_Type'] = encoder.fit_transform(dataset['Outlet_Location_Type'])
dataset['Outlet_Type'] = encoder.fit_transform(dataset['Outlet_Type'])

dataset.head()

X = dataset.drop(columns='Item_Outlet_Sales',axis=1)
Y = dataset['Item_Outlet_Sales']

print(X)

print(Y)

#splitting the data into train test split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

#training the model
model = XGBRegressor()
model.fit(X_train,Y_train)

#getting prediction for training data
training_prediction = model.predict(X_train)
print(training_prediction)

#R squared Value
r2_train = metrics.r2_score(Y_train,training_prediction)
print("R squared value for training data : ",r2_train)

#getting prediction for testing data
testing_prediction = model.predict(X_test)
print(testing_prediction)

#R squared Value
r2_test = metrics.r2_score(Y_test,testing_prediction)
print("R squared value for testing data : ",r2_test)

