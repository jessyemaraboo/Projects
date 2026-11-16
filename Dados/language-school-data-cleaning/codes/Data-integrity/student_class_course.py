#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

#Importing dataset
df2 = pd.read_csv("Data_Analysis_Study\Python\Mini-Projects\Project2Beginner\datasets\df2.csv")
df2.head()

audit_1 = pd.read_csv("Data Analytics\Data_Analysis_Study\Python\Mini-Projects\Project2Beginner\datasets\teacher_course_class_missing_values_auditing.csv")

#---------Data integrity---------#
# Student - Class

#Students linked to no class or multiple classes
class_per_student = df2.groupby("student_id")["class_id"].nunique().sort_values(ascending=False).reset_index()

class_per_student.columns = ["student_id","total_associated_classes"]

orphan_student = class_per_student[class_per_student["total_associated_classes"] < 1]

len(orphan_student) #61

class_per_student.head(40)

#NaNs per column
student_class_course = df2[["student_id", "class_id", "course"]]
student_class_course = student_class_course.drop_duplicates() # 922

student_class_course["student_id"].isna().sum()
student_class_course["course"].isna().sum()
student_class_course["class_id"].isna().sum()

#Students per class
students_per_class = df2.groupby("class_id")["student_id"].nunique().sort_values(ascending=False).reset_index()
### 585 classes has 1 student, 25 has 2 and 2 classes has 6. 2 class has either 3 or 7 students.

#--Classes with no students
orphan_class = students_per_class[students_per_class["student_id"] < 1]

len(orphan_class) #141

students_per_class.head(40)

#Valid student id linked to an inexistent class
student_null_classes = df2[df2["class_id"].isna() & df2["student_id"].notna()][["student_id", "class_id"]]

len(student_null_classes) #62

student_null_classes.head(40)

#Duplicated student-class

student_class_duplicated = df2[df2.duplicated(subset=["student_id","class_id"], keep=False)][["student_id","class_id", "course", "student_email"]].sort_values(by="student_id")

student_class_duplicated_list = student_class_duplicated["student_id"]

len(student_class_duplicated) #32
len(student_class_duplicated_list)

#--Removing inconsistencies
inconsistent_student_audit = df2[(df2["student_id"] == "STU0123")]

inconsistent_student_audit.to_csv("inconsistent_student_id_records_auditing_report.csv", index=False)

df2 = df2[~(df2["student_id"] == "STU0123")]

#duplicated removal
df2.drop_duplicates(subset=["student_id","class_id","student_email"], keep='first', inplace=True)
#--------
### The class C-2027-001 has 16 unique students and the class C-2015-999 has 15 students, the others C-2009-777 has 7, C-2028-999 -> 6,C-2010-001 -> 6, C-2020-054 -> 3. The other classes has either 2 or 1 student;

#*-------------------Visualization----------------------------*
#***Visualization Box-plot***#
plt.figure(figsize=(8,5))
sns.boxplot(y="total_students", data=students_per_class)

plt.title("Distribution of students per class")
plt.show()
#*-----------------------------------------------*
#Classes per courses
grouped_course = df2.groupby("course")["class_id"].nunique().sort_values(ascending=False).reset_index()

grouped_course.columns = ["course", "total_classes"]
grouped_course.head()

#*-----------------------------------------------*
#***Visualization bar graph***#
plt.figure(figsize=(10,6))

plt.bar(grouped_course["course"], grouped_course["total_classes"], label="classes")

plt.xlabel("Courses")
plt.ylabel("Total classes")
plt.title("Total classes per course")
plt.legend()
plt.xticks(rotation=45, ha="center")
plt.tight_layout()
plt.show()
#*-----------------------------------------------*
#Courses per students
grouped_student_course = df2.groupby("student_id")["course"].nunique().sort_values(ascending=False).reset_index()
grouped_student_course.columns = ["course", "total_courses"]

#*--------------------------------------------*
#***Visualization Box-plot***#
plt.figure(figsize=(8,5))

sns.boxplot(y = "total_courses", data=grouped_student_course)

plt.title("Distribution of courses per student")
plt.show()

#-------------------------------------------*
#Identifying student with 0 course
courses_with_no_student = grouped_student_course[grouped_student_course["total_courses"]<1][["course", "total_courses"]]
#22 students in 0 courses

courses_with_no_student.head(25)
#*------------------------------------------*#

