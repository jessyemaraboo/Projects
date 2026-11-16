#Introduction
"""This page aims to improve data cleaning skills by working with a fictitious and artificially generated language school dataset intentionally generated with inconsistencies that simulate real world data cleaning challenges"""

"""OBS: To run python in powershell type .venv/Scripts/activate and then type: python"""
#Importing packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
"""-------------------------------------"""

#Loading dataset

df = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/language_school_data.csv")
df.head()

#-------------------------------------
#Exploring dataset

df.info() #Getting dataset columns 
df.dtypes #Checking data types for each column

#Checking missing values

df.isnull().any().any() #Check if there is any missing value in the whole dataset.

df.isna().sum().sort_values(ascending=False) #Check how many missing values per column and sort the results in descending order.

#Summing all the missing values per column we have 399 missing entries
#-------------------------------------

#Percentage of the dataset affected by missing values

#Function to determine the percentage of a value for the whole dataset

def percentage_dataset(value):
  result = (value / len(df)) * 100
  return f"{result:.2f}%"
  
#All the missing entries

percentage_dataset(399) #39.90%

#student_id: 40
percentage_dataset(40) #4.00%

#→ class_id: 37
percentage_dataset(37) #3.70%    

#→ monthly_fee: 26
percentage_dataset(26) #2.60%

#→ course: 29
percentage_dataset(29) #2.90%

#→ teacher_id: 37
percentage_dataset(37) #2.70%

#→ student_status: 37
percentage_dataset(37) #3.70%

#→ total_course_modules: 32
percentage_dataset(32) #3.20%

#→ enrollment_date: 51
percentage_dataset(51)#5.10%

#→ age: 38
percentage_dataset(38) #3.80%

#→ student_email: 31
percentage_dataset(31)#3.10%

#Identifying empty values not recognized by pandas
sus = [" ", " ", "" "", '', ' ' ]

mask = df.apply(lambda col: col.astype(str).str.strip().isin(sus))

df[mask.any(axis=1)] #FALSE
#or
empty_values = (df == "").sum()

#---Visualization  
#Creating a barchart that illustrates the amount of missing values per column

missing_values = df.isna().sum().reset_index()

missing_values.columns = ["dataset_columns", "total_missing_values"]

#------generating bargraph------#

fig, ax = plt.subplots(figsize =(10,6))

ax.bar(missing_values['dataset_columns'], missing_values["total_missing_values"], label = "missing values")

ax.set_xlabel("Dataset columns")
ax.set_ylabel("Number of missing values")
ax.set_title("Number of missing values by columns")
ax.legend()

plt.xticks(rotation=45, ha="center") #ha=center assure that the xlabels are aligned to teir own data

plt.tight_layout() #adjust graph to not cut the xlabels
plt.show()

#---------Duplicates-----------#
#detecting duplicates

df.duplicated().sum() #returned 31

#Returning duplicated rows and organising as a list to confirm duplication

duplicated_rows = df[df.duplicated(keep = False)].sort_values(by=list(df.columns)) #keep=false keeps both the original and the duplicate in the results

#---Percentage duplicates x wholedataset

def percentage_dataset(value):
  result = (value / len(df)) * 100
  return f"{result:.2f}%" #reusing function

percentage_dataset(31) #3.10%

#---Removing duplicates

df2 = df.drop_duplicates() #969 rows after removal of duplication

#Exploring more duplicate values
#student_id

df2.duplicated(subset="student_id").sum() #returned 129

#---displaying ids and info

student_id_duplicates = df2[
  df2.duplicated(subset="student_id", keep = False)
  ].sort_values(by=list(df.columns)) #with keep=false there is an increase of 26 values



