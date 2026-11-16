#----------Loading important packages-----------#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#--------Loading datasets-------#
df = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/language_school_data.csv")
df2 = df.drop_duplicates()

#-------Standardization and Consistency--------#

#-----Student_id and Class_id-------#

#student_id
df2["student_id"].value_counts() #returned 839 types
#------#
df2["student_id"].nunique() #returns only the number
#------#

#---Checking for invalid ids

#clean blank spaces with .strstrip()
#Setting student_id standard:
standard_student = r'^[A-Z]{3}[0-9]{4}$'

#Filter for ids that do not follow the standard

invalid_ids_count = (
  ~df2['student_id'] 
  .astype(str) #Tranform the data into strings
  .str.strip() #remove extra spaces
  .str.match(standard_student, na=False) #check the ids following the student_id_pattern
  ).sum() #sums the result of ids that doesn't match the pattern

#Valid ID: Length: 7 (3 letters 'STU' and 4 numbers '0000')

mask = ~df2["student_id"].astype(str).str.strip().str.upper().str.match(standard_student, na=False)

df2[mask]['student_id'].sum()

#---Cleaning ids

df2.loc[:,"student_id"] = (
  df2["student_id"] #select the column student_id
  .astype(str) #Tranforms data into strings
  .str.replace(r'[?.\-\,\s/]', '', regex=True) #Remove the chacracteres between the bars and any other empty space (\s).
  .str.upper() #Set all letters to upper capitalization
  )

#Checking invalid ids count
invalid_ids_count # 101 ids were put in pattern (760 still doesn't follow the STU0001 pattern)

#---Transforming invalid ids in none

# Criteria: 
# - Less than 7 characteres, 
# - Composed by only letters, special characteres OR numbers.

invalid_ids_criteria = (
  df2["student_id"].astype(str).str.match(r'^.{0,6}$', na=False) | #less than 7 characteres
  df2["student_id"].astype(str).str.match(r'^[A-Za-z]+$', na=False) | #Composed by only letters
  df2["student_id"].astype(str).str.match(r'^[0-9]+$', na=False) #Composed by only numbers
)

#---Applying the criteria to the dataset transforming the invalid ids in NaNs

df2.loc[invalid_ids_criteria, "student_id"] = None
df2["student_id"].head(20)

#---Standardizing the ids

standard_id = df2["student_id"].str.extract(r'^([A-Z]+)[^0-9]*([0-9]+)$') #Extracting the letters and numbers

df2['student_id'] = (
  standard_id[0].str.upper() +
  standard_id[1].str.zfill(4)
)

 #---------------------------------------------------------------------#



