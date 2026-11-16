#Importing important packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#--------Loading datasets-------#
df = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/language_school_data.csv")
df2 = df.drop_duplicates()

#-------Standardization and Consistency--------#

#---Cleaning Course column---#
#Course Names

#Counting unique courses 

df2["course"].nunique() #47

#mask to get only full course names
mask_full = df2["course"].str.len() >=4

#Applying mask
df2[mask_full]["course"].sort_values().unique() 

#Abbreviations
mask_abreviations = df2["course"].str.len() <=5
df2[mask_abreviations]["course"].sort_values().unique()

#Cleaning extra spaces and caracteres
df2.loc[:, "course"] = df2["course"].astype(str).str.strip().str.replace(r'[^A-Za-z]', "", regex=True)

#Creating a mask to identify "ENGLISH" abreviations
mask_en = df2["course"].astype(str).str.startswith("En",na=False)

#Aplying mask and changing results to ENGLISH
df2.loc[mask_en, "course"] = "English"

#Standardizing course names
#Valid course name: 
#-1st letter capitalized
#-full course name
#List of courses: Dutch, English, French, German, Italian, Japanese, Portuguese, Spanish 

df2.loc[:, "course"] = df2["course"].str.capitalize()

#Create a dictionary with references of abreviations
course_val = {"Jp": "Japanese", 
   "Fr":"French",  
   "Nl":"Dutch", 
   "Es":"Spanish", 
   "Jap":"Japanese",
   "De":"German", 
   "Port":"Portuguese",
   "Ital":"Italian",
   "Neth":"Dutch",
   "Pt":"Portuguese",
   "It": "Italian",
   "Span":"Spanish",
   "Dutchh":"Dutch",
   "Ger":"German"
   }

#Transforming abreviations into validc course names
df2["course"] = df2["course"].replace(course_val)

#Relation Course x Students
course_stu = df2["course"].value_counts().reset_index()
course_stu.columns = ["course","total_students"]

#------Visualization------#
#using seaborn to create a barchart with the relation student per class

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(data = course_stu, x="course", y="total_students", label="Students")

plt.title("Number of students per course")
plt.xlabel("Courses")
plt.ylabel("Students")

plt.xticks(rotation = 45, ha= "center")
plt.tight_layout()

plt.show()

#--------------------------------------------------# 
# Saving new dataset#
df2.to_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index=False, sep=",", encoding="utf-8")