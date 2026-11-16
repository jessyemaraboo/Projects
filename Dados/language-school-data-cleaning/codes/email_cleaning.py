#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

#Lading dataset
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv")
df2.head()

#---Email column cleaning
#Exploring
df2["student_email"].head(20)
df2["student_email"].nunique() #857
df2["student_email"].value_counts()

#Identifying emails with anomalies
valid_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

student_email = df2["student_email"]

#Emails with anomalies
emails_anomalies = df2[~df2["student_email"].str.match(valid_email, na=True)][ "student_email"] #83

emails_anomalies.value_counts().head(20)

#Checking whetcher this email is unique per student or a span
mask = df2["student_email"] == "john.smith.example.com"

df2[mask]["student_id"].head(20) #Span, it was registered to 14 different students.

#Replacing all invalid emails to NaN

df2.loc[~df2["student_email"].str.match(valid_email, na=True),"student_email"] = np.nan

#Analysing e-mail providers
email_providers = df2["student_email"].str.split("@").str[1]

email_providers.head(30)
email_providers.value_counts() #2 values: one ending with .com and the other .co (24)

#Replacing the misspelled .co end to .com
mask_email_providers = df2["student_email"].str.contains(r".co$", na=False)

df2[mask_email_providers]["student_email"].head(10)

#Adding an "m" to the end of all .co
df2.loc[mask_email_providers, "student_email"] = df2["student_email"] + "m"

#Checking changes
df2["student_email"].str.split("@").str[1].value_counts() #857, only 1 provider ending with .com
#--------------------------------------------#
#Saving new clean dataset
df2.to_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index=False, sep=",", encoding="utf-8")
