
#----------Loading important packages-----------#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt

#--------Loading datasets-------#
df = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/language_school_data.csv")
df2 = df.drop_duplicates()

#-------Standardization and Consistency--------#

#---Cleaning Classes_ids---#
#Standard: C-YYYY-000

#Unique classes Id
df["class_id"].nunique()

#Extracting class_id years and saving in a new column named "class_id_years"
df2["class_year"] = df2["class_id"].astype(str).str.split("-").str[1]

df2 ["class_year"].nunique()

#Sorting years

pd.Series(df2["class_year"].unique()).sort_values() #pd.Series tranform an array numpy in a pandas series.
df2["class_year"].value_counts()

#Valid Class_Id standard: C-YYYY-000

valid_class = r'^C-[0-9]{4}-[0-9]{3}$'

#Tracking invalid class_ids

mask = df2["class_id"].astype(str).str.match(valid_class, na=False)
# invalids 
~mask.sum()

df2[mask]["class_id"] #apply mask to filter (~in)valid ids

#Filtering students with invalid classes Classes

student_class = df2[~mask][["student_id", "class_id"]]
student_class[mask].head(20)
student_class.shape


#Unique Students per class
mask = df2["class_id"].astype(str).str.match(valid_class) &     df2["student_id"].astype(str).str.match(student_id_pattern) #&   ~df2["student_id"].duplicated() 

student_class[mask]["class_id"].value_counts()

#---Visuzalization---#
#--------------------------------------------#
#filtering class records per year: class_id_years, class_id

"""
mask_1 = class_year_viz['years'].astype(str).str.match(r'^[0-9]{4}$')

class_year = df2[["class_id", "class_year"]]
class_year_viz = class_year["class_year"].value_counts().reset_index()
class_year_viz.columns = ["years","number_of_records"]
class_year_viz = class_year_viz[mask_1].sort_values(by = 'years')"""
#-------------------------------------------#

#Simplified code
class_year_viz = (
    df2["class_year"]
    .value_counts()
    .reset_index(name="number_of_records")
    .rename(columns={"class_year": ""})
)

# Sorting data
class_year_viz = (
    class_year_viz[class_year_viz['year'].astype(str).str.match(r'^[0-9]{4}$')]
    .sort_values(by='year')
)

#---Making a bar graph

fig, ax = plt.subplots(figsize=(10, 6))

plt.bar(class_year_viz["year"], class_year_viz["number_of_records"], label = "number of records")

plt.xlabel("Year")
plt.ylabel("Number of records")
plt.title("Class records per year")

plt.legend()

plt.xticks(rotation=45, ha="center") 
plt.tight_layout() 
plt.show()

#----------Cleaning class_ids column------------#
mask_x = (df2["class_id"].str.len() > 10) &(df2["class_id"].astype(str).str.match(r'^C-[0-9]{4}-[0-9]{3}$')) & (df2["class_id"].notna()) #Getting only the ids that fall into the specified criteria

#Changinf values
df2.loc[mask_x, "class_id"] = df2[mask_x]["class_id"].str.slice(0,10) #For ids that has only 1 extra digit

#2nd version of mask_x for totally invalid ids
mask_x = (df2["class_id"].str.len() > 11) |~(df2["class_id"].astype(str).str.match(r'^C-[0-9]{4}-[0-9]{3}$')) & (df2["class_id"].notna()) 

#Changing invalid class values
df2.loc["class_id"] = df2["class_id"].str.strip().replace({"nan": np.nan, "None": np.nan})

#Converting class_year to datetime
df2["class_year"] = pd.to_datetime(df2["class_year"], format="%Y", errors="coerce").dt.to_period("Y")

#Saving clean columns as a df2 csv
df2.to_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index=False, sep=",", encoding="utf-8")
#-------------------------------------------------#
