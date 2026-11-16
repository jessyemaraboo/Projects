#Importing important packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#--------Loading datasets-------#
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv")
df2 = df.drop_duplicates()

#-------Logical data validation--------#

#----------Exploring column-----------#

#Unique values
df2["total_course_modules"].value_counts()
df2["total_course_modules"].nunique() #10

#--Removing invalid values for course modules
#unique values
df2["total_course_modules"].value_counts()

#Different total modules per course
modules_per_course = df2.groupby("course")["total_course_modules"].unique().reset_index()

modules_per_course.columns = ["course", "total_modules"]

modules_per_course.head(30)


#Getting student_id, "total_course_modules", "completed_modules" and "class_year"
df2_clean = df2.dropna()

student_module = df2_clean[["student_id", "total_course_modules", "completed_modules", "class_year"]]
student_module.head(30)

#Students where completed_modules is > total_course_modules

completed_modules_converted = pd.to_numeric(df2_clean["completed_modules"], errors="coerce") 

total_course_module_converted = pd.to_numeric(df2_clean["total_course_modules"], errors="coerce") 

mask = (completed_modules_converted > total_course_module_converted) 

val_student_modules = student_module[mask]

val_student_modules["student_id"].nunique()

#Students with negative completed modules

mask = (completed_modules_converted < 0)

negative_modules = student_module[mask]

negative_modules["student_id"].nunique()

#Students with non-numeric values

mask = completed_modules_converted.isna() & student_module["completed_modules"].notna()

non_numeric_modules = student_module[mask]

non_numeric_modules["student_id"].nunique()


#----Cleaning total_course_modules---#
#------removing nans-----#
df2 = df2.replace({"nan": np.nan, "Nan": np.nan, "NaN": np.nan})

#Replacing non-numeric and different values
df2["total_course_modules"] = df2["total_course_modules"].replace("twelve", "12") #also 12.0 for 12

#----Cleaning completed_modules---#

#Replacing non-numeric and different values
df2["completed_modules"] = df2["completed_modules"].replace("twelve", "12")

#treating invalid values and converting columns to numeric
columns = [ "total_course_modules", "completed_modules"]

for col in columns:
  df2[col] = pd.to_numeric(df2[col], errors="coerce")
  df2.loc[(df2[col] < 0) | (df2[col] >= 99), col] = np.nan
  
#Standardizing modules per course and saving in a new column (made with gemini's assistance)
mode_courses = (df2.groupby("course")["total_course_modules"].agg(lambda x: x.mode()[0]).to_dict())

df2["mode_course_modules"] = df2["course"].map(mode_courses)
  
#New columns to treat extra modules per student
df2["extra_modules"] = np.where(
  df2["completed_modules"] > df2["total_course_modules"],
  df2["completed_modules"] - df2["total_course_modules"], 0)

#Fixing the difference between the total_course_module and the completed_modules by student
df2.loc[
       df2["completed_modules"] > df2["mode_course_modules"],
       "completed_modules",
   ] = df2["mode_course_modules"]


#------------------------------------------


