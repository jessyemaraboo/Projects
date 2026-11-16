#Import important packages
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

#Import dataset
df2 = pd.read_csv("Data_Analysis_Study\Python\Mini-Projects\Project2Beginner\datasets\df2.csv")
df2.head()

#-----------Data integrity--------#
#Teacher - Class - Course

#Teacher linked to multiple classes
class_per_teacher = df2.groupby("teacher_id")["class_id"].nunique().reset_index().sort_values(by="class_id", ascending=False)

class_per_teacher.head(40)
class_per_teacher["class_id"].value_counts() #(1 teacher with 24 classes, is that valid? 'TCH0012')

#Teachers linked to multiple courses
courses_per_teacher = df2.groupby("teacher_id")["course"].nunique().reset_index().sort_values(by="course", ascending=False)

courses_per_teacher.head(40)
courses_per_teacher["course"].value_counts() #No appearant sign of inconsistency

teacher_multiple_course = courses_per_teacher[courses_per_teacher["courses"] > 1][["teacher_id", "courses"]]

len(teacher_multiple_course) #85

#Classes linked to multiple teachers
teachers_per_class = df2.groupby("class_id")["teacher_id"].nunique().reset_index().sort_values(by="teacher_id", ascending=False)

teachers_per_class.head(40)
teachers_per_class["teacher_id"].value_counts() #Multiple inconsistencies were found

#Classes linked to multiple courses
courses_per_class = df2.groupby("class_id")["course"].nunique().reset_index().sort_values(by="course", ascending=False)

courses_per_class.head(40)
courses_per_class["course"].value_counts() #Multiple inconsistencies were found 

inconsistent_courses_per_class = courses_per_class[courses_per_class["course"] > 1]["class_id"]

##### Counting class_ids associated with multiple courses
course_class_count = courses_per_class["course"].value_counts()
print(course_class_count)
len(course_class_count) # 775

# Extracting class_ids associated with more than 1 course
inconsistent_class_id = (courses_per_class[courses_per_class["course"] > 1]["class_id"]).tolist()

len(inconsistent_class_id)

# Extracting teachers associated with inconsistent classes
inconsistent_teacher_class = df2[df2["class_id"].isin(inconsistent_class_id)][["class_id", "course","teacher_id"]].dropna()

# Sorting values by class_id
inconsistent_teacher_class = inconsistent_teacher_class.sort_values(by="class_id", ascending=False)

#--Removing inconsistent classes
inconsistent_courses_per_class = courses_per_class[courses_per_class["course"] > 1]["class_id"].sort_values(ascending=False)

inconsistent_courses_per_class.to_csv("inconsistent_class_course_records_auditing_report.csv", index=False)

df2 = df2[~(df2["class_id"].isin(inconsistent_courses_per_class))]

#*-----Visualization-------*#
#Teacher associated with multiple courses
#Preparing data for visualization
teacher_multiple_course_viz = courses_per_teacher["course"].value_counts().reset_index()
teacher_multiple_course_viz.columns = ["number_of_courses_per_teacher","total_teachers_associated"]

#Making a bargraph
plt.figure(figsize=(8,5))

plt.barh(teacher_multiple_course_viz["number_of_courses_per_teacher"], teacher_multiple_course_viz["total_teachers_associated"], label="total teachers")

plt.xlabel("Total teachers associated with mutiple courses")
plt.ylabel("Number of courses per teacher")
plt.title("Teachers associated with multiple courses")
plt.legend()
plt.show()

#------------------------------------------------------#

