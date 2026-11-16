#Importing important dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import dataset
df2 = pd.read_csv("Data_Analysis_Study/Python/Mini-Projects/Project2Beginner/datasets/df2.csv")
df2.head(30)

#Exploring column
df2["monthly_fee"].value_counts()
df2["monthly_fee"].nunique()

#-----Cleaning monthly_fee column-----#

#Converting monthly_fee in a new column
df2["monthly_fee_converted"] = pd.to_numeric(df2["monthly_fee"], errors="coerce")

#Mask to list non-numeric values
mask = (df2["monthly_fee_converted"].isna()) & (df2["monthly_fee"].notna())

fee_non_numeric = df2[mask]["monthly_fee"]

#Replacing textual values 
df2.loc[mask, "monthly_fee"] = df2["monthly_fee"].str.replace("four hundred", "400").str.strip()

#Removing EUR and €
df2.loc[mask, "monthly_fee"] = (df2["monthly_fee"].replace(r"EUR|, €|\$", "", regex=True).str.strip()) 

#Converting "monthly_fee" column
df2["monthly_fee"] = pd.to_numeric(df2["monthly_fee"], errors="coerce")

mask_valid_fees = (df2["monthly_fee"] > 1) & (df2["monthly_fee"] < 9999)

invalid_fees = df2[~mask_valid_fees]["monthly_fee"]

#Replacing invalid fees
df2.loc[~mask_valid_fees, "monthly_fee"] = np.nan
#-----------------------------------------------------------#
#----Visualization-----#
#Preparing data for visualization
mask_fee = df2["monthly_fee"].notna()
hist_fee = df2[mask_fee]["monthly_fee"]

#Creating histogram
plt.figure(figsize=(8,5))

plt.hist(hist_fee, bins=20, color="#1f77b4", edgecolor="black")

#Title and labels
plt.title("Monthly fees distribution")
plt.xlabel("Fees")
plt.ylabel("Frequency")

plt.show()
#----------------------------------------------------------#


