# -*- coding: utf-8 -*-
"""Churn Prediction using Logistic Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qi45OhfwwSJ3Xt8pDk_7IwaJSn0FdBdB

IMPORTING NECESSARY LIBRARIES
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.simplefilter("ignore")

"""LOADING THE TELECOM DATASET FOR OUR CHURN PREDICTION"""

dt = pd.read_csv("/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(dt.head())
print(dt.describe())

"""DATA PREPROCESSING AND CLEANING"""

def remove_indices(col):
    return dt[dt[col]=="No phone service"].index
def remove_indices_another(col):
    return dt[dt[col]=="No internet service"].index

#dropping unncessary columns
print(dt.shape)
re_cols = ["customerID","gender","Partner","Dependents"]
for i in re_cols:
    dt = dt.drop(i,axis=1)
print(dt.shape)


print(dt.shape)
column_name = ["SeniorCitizen","tenure","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges","Churn"]
for i in column_name:
    re_in = remove_indices(i)
    re_in_an = remove_indices_another(i)
    dt.drop(re_in, inplace=True)
    dt.drop(re_in_an, inplace=True)
print(dt.shape)
print(dt)

#encoding categorical data into numerical data
print(dt.head())
encoder = LabelEncoder()
for i in column_name:
    dt[i] = encoder.fit_transform(dt[i])
print(dt.head())

"""SPLITTING INTO DEPENDENT AND INDEPENDENT ATTRIBUTES

"""

x = dt.drop("Churn",axis=1)
y = dt["Churn"]

"""DEFINING TRAINING AND TESTING DATA"""

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.4,random_state=42)

"""CREATING OBJECT FOR LOGISTIC REGRESSION"""

lo_rg = LogisticRegression()
lo_rg.fit(x_train, y_train)

"""TEST DATA PREDICTION"""

y_pred = lo_rg.predict(x_test)
print(x_test)
print(y_pred)

"""ACCURACY SCORE"""

accr = accuracy_score(y_test,y_pred)
print("Accuracy Score: ", accr)

cr = classification_report(y_test,y_pred)
print(cr)

"""COLLECTING USER DATA FOR PREDICTION"""

# Initialize an empty list to store user input
user_data = []

# Ask user for input
senior_citizen = int(input("Is the customer a Senior Citizen? (0 for No, 1 for Yes): "))
user_data.append(senior_citizen)

tenure = int(input("Enter tenure (in months): "))
user_data.append(tenure)

phone_service = int(input("Does the customer have Phone Service? (0 for No, 1 for Yes): "))
user_data.append(phone_service)

multiple_lines = int(input("Does the customer have Multiple Lines? (0 for No, 1 for Yes): "))
user_data.append(multiple_lines)

internet_service = int(input("Enter Internet Service ( 0 for DSL or 1 for Fiber optic): "))
user_data.append(internet_service)

online_security = int(input("Does the customer have Online Security? (0 for No, 1 for Yes): "))
user_data.append(online_security)

online_backup = int(input("Does the customer have Online Backup? (0 for No, 1 for Yes): "))
user_data.append(online_backup)

device_protection = int(input("Does the customer have Device Protection? (0 for No, 1 for Yes): "))
user_data.append(device_protection)

tech_support = int(input("Does the customer have Tech Support? (0 for No, 1 for Yes): "))
user_data.append(tech_support)

streaming_tv = int(input("Does the customer have Streaming TV? (0 for No, 1 for Yes): "))
user_data.append(streaming_tv)

streaming_movies = int(input("Does the customer have Streaming Movies? (0 for No, 1 for Yes): "))
user_data.append(streaming_movies)

contract = int(input("Enter Contract Type (0 for Month-to-month, 1 for One year, 2 for Two years): "))
user_data.append(contract)

paperless_billing = int(input("Is Paperless Billing enabled? (0 for No, 1 for Yes): "))
user_data.append(paperless_billing)

payment_method = int(input("Enter Payment Method (0 for Electronic Check, 1 for Mailed Check, 2 for Bank Transfer, 3 for Credit Card): "))
user_data.append(payment_method)

monthly_charges = float(input("Enter Monthly Charges: "))
user_data.append(monthly_charges)

total_charges = float(input("Enter Total Charges: "))
user_data.append(total_charges)

print("User data collected successfully:", user_data)

"""Predicting with the Collected data

"""

input_array = np.array(user_data).reshape(1, -1)

# Get probability estimates for each class
probabilities = lo_rg.predict_proba(input_array)

# Print the probability values
print("Probability of NO (class 0):", probabilities[0, 0])
print("Probability of YES (class 1):", probabilities[0, 1])

y_pred = lo_rg.predict(input_array)
if y_pred==0:
    print("Churn Prediction result is: NO")
elif y_pred==1:
    print("Churn Prediction result is: YES")