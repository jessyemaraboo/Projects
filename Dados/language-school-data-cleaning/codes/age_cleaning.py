#Importing important datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Importing dataset
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv")
df2.head(35)


#-------Logical data validation--------#

#----------Exploring column-----------#
df2["age"].head(30)
df2["age"].value_counts()
df2["age"].nunique()

#----Exploring ages
age_converted = pd.to_numeric(df2["age"], errors="coerce")

#Minimun age recorded
age_converted.min() #-3

#Maximum age recorded
age_converted.max() #150

#-----Invalid ages------#

#Negative ages
negative_ages = age_converted[age_converted < 0]

len(negative_ages) #12

#Decimal ages
decimal_ages = age_converted[(age_converted % 1 !=0) & (age_converted.notna())]

len(decimal_ages) #25

#Non-numeric ages
mask_non_numeric = age_converted.isna() & df2["age"].notna()

non_numeric_ages = df2[mask_non_numeric]["age"]

len(non_numeric_ages) #14

#Invalid high age
age_converted.value_counts().sort_values(ascending=False) #150.0 = 24

#Stabilishng school age range ignoring extreme 
age_range = (age_converted >= 1 ) & (age_converted <= 100 )

#Getting lowest age
lower_age = age_range.quantile(0.01)

#Getting highest age
upper_age = age_range.quantile(0.99)

print(lower_age, upper_age)

#Records that fall out of the range 16 -72
(~age_range).sum() #90

#-------Cleaning dataset column df2""age"------#

#Replacing non-numeric values for numeric ones
non_numeric_ages.value_counts()
df2["age"] = df2["age"].replace("twenty", "20")

#Changing data type from string to numeric float
df2["age"] = pd.to_numeric(df2["age"], errors="coerce")

mask = (df2["age"] < 16) | (df2["age"] > 72)

df2.loc[mask, "age"] = np.nan

#Converting age column and removing .00 numbers
df2["age"] = (
    pd.to_numeric(df2["age"], errors="coerce")
    .apply(lambda x: int(x) if pd.notna(x) else pd.NA)
    .astype("Int64")
)

#Changing columns from float to int
columns_to_integer = ["total_course_modules", "completed_modules", "extra_modules", "mode_course_modules"]

for col in columns_to_integer:
  df2[col] = df2[col].astype("Int64")
  
#----------------------------------------------#
#Saving clean dataset#
df2.to_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index=False, sep=",", encoding="utf-8")
