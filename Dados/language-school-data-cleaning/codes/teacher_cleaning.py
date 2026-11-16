#Import libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Importing dataset
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv")
df2.head(20)

#-------Standardization and Consistency--------#

#------Teachers and classes------#
#teacher_id - class_id

#Sorting unique teachers
df2["teacher_id"].nunique() #490

#Stabilishing standard valid teacher id: TCH0000
valid_teacher = r'^TCH[0-9]{4}$'

# ids that follow the standard: 106
mask = df2["teacher_id"].astype(str).str.match(valid_teacher, na=False)

#ids that have any inconsistency: 863
(~mask).sum()

#duplicated ids: 478
df2["teacher_id"].duplicated().sum()

#ids with mispelling: 453 (559-106)
mask_mispelled = (df2["teacher_id"].astype(str).str.upper().str.startswith(("TCH"), na=False))

mis_ids = df2[mask_mispelled]["teacher_id"]

len(mis_ids) #765
len(mis_ids[mask]) #106 valid pefect ids
len(mis_ids[~mask]) #659 ids with formatting problems

#Standardizing ids
df2["teacher_id_clean"] =   (df2["teacher_id"]
                             .astype(str)
                             .str.upper()
                             .str.replace(r"[^A-Z0-9]", "", regex=True))

#Grouping standardized ids and matching with their raw format
multiple_ids = df2.groupby("teacher_id_clean")["teacher_id"].unique()

#Returning the list with unique ids and their respective misspelled formats
multiple_formats = multiple_ids[multiple_ids.apply(len) > 1] #return unique clean ids from groupby with more than 1 raw teacher_ids 

#making basic changes
df2["teacher_id"] =  (df2["teacher_id"]
  .astype(str)
  .str.upper() 
  .str.replace(r"[^A-Z0-9]", "", regex=True) #analyze every string and remove anything but letters: A-Z and numbers: 0-9
)

#---Standardizing the ids---#

valid_teacher_id = df2["teacher_id"].str.extract(r'^([A-Z]+)[^0-9]*([0-9]+)$') #Extracting TCH and numbers from each valid id

df2['teacher_id'] = (
  valid_teacher_id[0].str.upper() +
  valid_teacher_id[1].str.zfill(4) #filling missing numbers
)

#Replacing invalid or empty, null/none values in NaNs with .replace()
df2.loc[~mask,"teacher_id"] = df2[~mask]["teacher_id"].str.strip().replace({"T0999": np.nan, "nan": np.nan, "None": np.nan}) #Tranform any null o empty space in NaN

#Unique ids after cleaning
df2["teacher_id"].nunique()

#----------Teacher-Course Consistency---------------#

#Grouping the columns teacher_id and aggregating unique courses related to unique teacher_ids

teacher_course = df2.groupby("teacher_id")["course"].unique().sort_values(ascending=False)

#Filtering teachers with more than one language course

teacher_course_filter = teacher_course[teacher_course.apply(len) >=  1].reset_index()

#Checking length

len(teacher_course_filter) #85

#Number courses per teacher: Creating a new column with the quantity of courses per teacher

teacher_course_filter["number_of_course_per_teacher"] = teacher_course_filter["course"].apply(len)

#Sorting values

teacher_course_filter.sort_values(by='number_of_course_per_teacher', ascending=False).head(30)

#Courses taught by teacher

teacher_course_filter["number_of_course_per_teacher"].value_counts()

#Creating a cross table to check the relation teacher x course
teacher_course_ct = pd.crosstab(df2["teacher_id"], df2["course"])

#Percentage for total number of teachers and courses they teach
def percentage_dataset(value):
  result = (value / len(teacher_course_filter)) * 100
  return f"{result:.2f}%"

#----------------------------------------------#

def percentage_dataset(value):
  result = (value / len(teacher_course_filter)) * 100
  return f"{result:.2f}%"

#------------Teacher x class consistency ---------#

#Removing nan values from class_id column before grouping
df2_clean = df2.dropna()

#Creating a group of teachers and classes they teach in
teacher_class = df2_clean.groupby("teacher_id")["class_id"].nunique().reset_index()

teacher_class.columns = [ "teacher_unique_id","class_per_teacher"]

#Creating a column with the number of class per teacher
teacher_class["total_class"] = teacher_class["class_per_teacher"].apply(len)

teacher_class.info()
teacher_class.head(30)

#sorting by total_class
teacher_class.sort_values(by='total_class', ascending=True).head(30)

teacher_class["total_class"].value_counts()

#Multiple teachers
class_teacher = df2_clean.groupby("class_id")["teacher_id"].nunique().reset_index()

def percentage_dataset(value):
  result = (value / len(teacher_class)) * 100
  return f"{result:.2f}%"

#class with 1 teacher: 373
#class with 2 teachers: 4
#class with 10 teachers: 2
#class with 3 teachers: 2
#class with 5 teachers: 1
#class with 4 teachers: 1
df2["class_id"].isna().sum()

#Grouping "class_id" e "course" unique values
course_class = df2.groupby("class_id")["course"].nunique().reset_index()
course_class.columns = ["class", "sum_different_course"]

#Filtering teacher with multiple classes and different courses
multiple_class_course = course_class[course_class["sum_different_course"] > 1]       

#Getting quantity of classes with multiple course assignments
len(multiple_class_course) 


#Inconsistent classes with multiple teachers
#IDS: C-2015-999 10 (11 records), C-2027-001 10, C-2010-001 5, C-2009-777 4, C-2020-054 3, C-2028-999 3, C-2020-095 2 , C-2022-152 2, C-2023-421 2, C-2024-322 2
#Saving classes ids with inconsistencies
inconsistency_class_teacher_course = class_teacher[class_teacher["course"] > 1]

#Converting classes ids to list
list_multiple_teacher_class = inconsistency_class_teacher_course["class_id"].tolist() 

#Creating a filter
inconsistent_class = df2_clean[df2_clean["class_id"].isin(list_multiple_teacher_class)]

#Printing ids with their assignments: teacher, class and course
inconsistent_class[["teacher_id", "class_id", "course"]]

#---------------------------------------#
#Saving clean new version of df2 dataset
df2.to_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index=False, sep=",", encoding="utf-8")
#---------------------------------------#