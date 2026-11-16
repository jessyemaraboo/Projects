import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Importing dataset
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv")

df2.head(20)

df2["student_status"] = df2["student_status"].replace(
    ["Nan", "NaN", "nan", "  "], np.nan
)

#-------------Logical data validation ----------------#

#----------Student Status cleaning -------------#

#Counting unique values
df2["student_status"].nunique() #13

#Getting different values
df2["student_status"].value_counts()

#Student_status standardization
#Possible values: Pending, On hold, Enrolled
#Removing extra spaces and setting all to lower and then capitilizing
df2["student_status"] = df2["student_status"].astype(str).str.strip().str.lower()

df2["student_status"]  = df2["student_status"] .str.capitalize()

#Standadizing 
student_status_list = {"Enr":"Enrolled",
                       "Pend":"Pending",
                       "Trancado":"On hold",
                       "Enrol":"Enrolled",
                       "Pendingg":"Pending",
                       "E":"Enrolled",
                       "?":"Pending",
                       "On-hold":"On hold"
                       }
#Replacing misspelled values for the student_status_list and standardizing student status
df2["student_status"]  = df2["student_status"].replace(student_status_list)

#Grouping student per status
#Removing null/nan values
df2_clean = df2.dropna()

#grouping student status
student_per_status = df2_clean.groupby("student_status")["student_id"].nunique().reset_index()

student_per_status.columns = ["student_status","total_student"]

(student_per_status.sort_values(by="total_student", ascending=False)).head(30)

#-----Visualization----#
#removing nan

#Creating a bar chart to express students per status category

fig, ax = plt.subplots(figsize=(10,6))

student_per_status.plot(
  kind="bar",
  x="student_status",
  y="total_student",
  ax=ax,
  color="#1f77b4",
  rot=0,
  label="total of student"
)
ax.set_xlabel("Status category")
ax.set_ylabel("Total of students")
ax.set_title("Number of students per status category")

plt.tight_layout()
plt.show()
#---------------------------------------------#
df2.to_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index=False, sep=",", encoding="utf-8")