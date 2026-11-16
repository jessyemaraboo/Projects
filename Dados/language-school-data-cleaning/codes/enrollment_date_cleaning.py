#Import important packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

#Import dataset
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv")
df2.head(30)

#----Exploring column----#
df2["enrollment_date"].head(30)
df2["enrollment_date"].value_counts()
df2["enrollment_date"].nunique()

#Different date patterns
#Converting column in a new temporary variable
enrollment_converted = pd.to_datetime(df2["enrollment_date"], errors="coerce")

#Creating a mask to identify different formats
mask_enrollment = (enrollment_converted.isna()) & (df2["enrollment_date"].notna())

#Saving mask results
multiple_enrollment_formats = df2[mask_enrollment]["enrollment_date"]

multiple_enrollment_formats.head(30)
multiple_enrollment_formats.value_counts() #5 +1 (right pattern YYYY-MM-DD)

#---Cleaning enrollment_date column---#

#Cleaning "not available"
df2.loc[mask_enrollment, "enrollment_date"] = df2["enrollment_date"].str.upper().replace("NOT-AVAILABLE", np.nan)

#Replacing multiple date separators for "-"
df2.loc[mask_enrollment, "enrollment_date"] = df2["enrollment_date"].str.upper().replace(r'[^A-Z0-9]', "-", regex=True)

#Fixing dates in wrong format format YYYY-DD-MM to YYYY-MM-DD using regex
df2.loc[mask_enrollment, "enrollment_date"] = df2["enrollment_date"].replace(r'^(\d{4})-(\d{2})-(\d{2})$', r'\1-\3-\2', regex=True )

#Converting data using format="mixed" for mixed date formats
df2["enrollment_date"] = pd.to_datetime(df2["enrollment_date"], format="mixed", errors="coerce")

df2["enrollment_date"] = df2["enrollment_date"].dt.strftime("%Y-%m-%d")
#-----------------------------#

#---- Variables using for testing ----#

multiple_enrollment_formats = multiple_enrollment_formats.str.upper().replace(r'[^A-Z0-9]', "-", regex=True)

multiple_enrollment_formats = multiple_enrollment_formats.replace("NOT-AVAILABLE", np.nan)

#Fixing format YYYY-DD-MM to YYYY-MM-DD
multiple_enrollment_formats = multiple_enrollment_formats.replace(r'^(\d{4})-(\d{2})-(\d{2})$', r'\1-\3-\2', regex=True )

#Converting to datetime
standardized_date = pd.to_datetime(multiple_enrollment_formats, format="mixed" ,errors="coerce")

standardized_date = standardized_date.dt.strftime("%Y-%m-%d")

standardized_date.head(30)

#Converting the enrollment_year column to date

df2["enrollment_year"] = pd.to_datetime(df2["enrollment_year"], format= "%Y", errors="coerce").dt.to_period("Y")

#---------------------------------------------------#
#********** Visualization **********#

#Preparing data: enrollments per year
df2["enrollment_year"] = df2["enrollment_date"].astype(str).str.split("-").str[0]

enrollment_viz = df2.groupby("enrollment_year")["enrollment_date"].count().dropna().reset_index()

enrollment_viz.columns = ["enrollment_year","total_enrollments"]

enrollment_viz.head(20)

#Creating a barchart
plt.figure(figsize=(10,6))

plt.bar(enrollment_viz["enrollment_year"],
        enrollment_viz["total_enrollments"],
        color = "#1f77b4",
        label = "total enrollments")

plt.xlabel("Years")
plt.ylabel("Total of enrollments")
plt.title("Enrollments per year")

plt.legend()


plt.tight_layout()
plt.show()
#*------------------------------------------------------*
df2.to_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv", index=False, sep=",", encoding="utf-8")

