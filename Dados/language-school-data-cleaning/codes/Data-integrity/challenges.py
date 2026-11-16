#Import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np

#Import raw dataset
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index_col = 0)

df1 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/language_school_data.csv", index_col = 0)

df2_clean = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/language_school_complete_clean.csv")

df2.head()
#------------------------------------------------------------

#Cardinality analysis (class per student)
classes_per_student = df2.groupby("student_id")["class_id"].nunique().sort_values(ascending=False)

classes_per_student.describe() #min 0, max 19

#Student density
student_per_class = df2.groupby("student_id")["class_id"].nunique()
student_per_class.head(40)

len(df2[df2["student_id"] == "STU0123"][["student_id", "class_id","student_status", "course","student_email"]])

#Isolating problematic ids
mask = df2["student_id"] == "STU0123"
df_auditing = df2[mask].copy()

df_auditing.to_csv("inconsistent_student_id_records_auditing_report.csv", index=False)

#Isolating missing values from course, teacher_id e class_id
mask_null = (df2["teacher_id"].isnull()) | (df2["class_id"].isnull()) | (df2["course"].isnull())

null_values = df2[mask_null]
null_values = null_values.reset_index(drop=True)
null_values.to_csv("teacher_course_class_missing_values_auditing.csv", index=False)

df2_x = df2[~mask_null]

#Creating metrics of data cleaning
report_data = {
  "Metric": [ 
    "Total rows",	
    "Total columns",
    "Duplicated records",
    "Missing values",	
    "Unique students",
    "Unique courses",
    "Invalid student IDs",	
    "Invalid class IDs",	
    "Invalid teacher IDs",	
    "Invalid courses",	
    "Invalid statuses",	
    "Invalid ages",	
    "Invalid fees",	
    "Invalid dates",	
    "Invalid module counts",	
    "Potential duplicate students",	
    "Potential class/course inconsistencies",	
    "Potential teacher/course inconsistencies",	
  ],
  "Before cleaning": [
    "1000",
    "12",
    "31",
    "545",
    "839",
    "47",
    "861",
    "82",
    "659",
    "657",
    "620",
    "90",
    "111",
    "114",
    "161",
    "160",
    "123",
    "201"
  ],
  "After cleaning":[
    "796",
    "15",
    "0",
    "1025",
    "647",
    "8",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0"
  ]
}

metric_table = {
  "Metric":[
    "Total rows",
    "Unique students",
    "Unique courses",
    "Null values",
    "Duplicate records"
  ],
  "Before cleaning" :[
    "1000",
    "839",
    "47",
    "545",
    "31"  
  ],
  "After cleaning":[
    "796",
    "647",
    "8",
    "1025",
    "0"  
  ]
}

#Visualization
#--Missing values by column
missing_values = df1.isnull().sum().reset_index()
missing_values.columns = ["columns", "missing_values"]

plt.figure(figsize=[10,5])

plt.bar(missing_values["columns"], missing_values["missing_values"], label="missing values")

plt.xlabel("Missing values")
plt.ylabel("Dataset columns")
plt.title("Distribution of missing values per column")

plt.legend()
plt.xticks(rotation=45)
plt.show()

#-----#

#--Number of raw courses and clean courses
course_comp = { 
  "Course_column": [
  "Course_column_RAW",
  "Course_column_CLEAN",
], 
  "Unique_categories": [
    df1["course"].nunique(),
    df2_clean["course"].nunique(),
]
  
} 

course_comp = pd.DataFrame(course_comp)

#--Bar graph
plt.figure(figsize=[10,5])

plt.bar(course_comp["Course_column"], course_comp["Unique_categories"], label="unique course categories")

plt.xlabel("Columns")
plt.ylabel("Unique categories")
plt.title("Unique course categories per table")

plt.legend()
plt.xticks()
plt.show()

#--Students per status
student_per_status = df2_clean["student_status"].value_counts()

student_per_status.plot(
  kind="pie",
  autopct="%1.1f%%", #show percentages
  startangle=90,
  figsize=(6,6),
  colors=["#4C72B0", "#55A868", "#C4814E"]
)
plt.title("Distribution of student per status", fontsize=14, fontweight="bold",)
plt.ylabel("")
plt.show()

#--Records by enrollment year
records_enrollment_year = df2["enrollment_year"].value_counts().reset_index().sort_values(by="enrollment_year")

print(records_enrollment_year)

#--viz

plt.figure(figsize=(10,5))

plt.bar(records_enrollment_year["enrollment_year"], records_enrollment_year["count"],  label="enrollments by year")

plt.ylabel("Total Records")
plt.xlabel("Enrollment_year")
plt.title("Data records by enrollment year")

plt.legend()
plt.xticks(records_enrollment_year["enrollment_year"])
plt.show()

#--Monthly fees distribution
#--Viz
plt.figure(figsize=(8, 5))

plt.hist(
  df2_clean["monthly_fee"],
  bins=6,
  color="#4C72B0",
  edgecolor="black"
)

plt.title("Distribution of monthly fees")
plt.xlabel("Monthly fees")
plt.ylabel("Frequency")
plt.show()

#----
columns = ["total_course_modules","completed_modules","age","class_year","mode_course_modules","enrollment_year"]

for i in columns:
  df2[i] = df2[i].astype("Int64")
#------
  
def percentage_dataset(value):
  result = (value / 10915)* 100
  return f"{result:.2f}%"
  