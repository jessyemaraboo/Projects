import pandas as pd
import os

#Import datasets
df_2021 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\raw\TF_SOC_POP_STRUCT_2021.csv", sep='|')

df_2022 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\raw\TF_SOC_POP_STRUCT_2022.csv", sep= '|', encoding='latin1')

df_2023 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\raw\TF_SOC_POP_STRUCT_2023.csv", sep= '|')

df_2024 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\raw\TF_SOC_POP_STRUCT_2024.csv", sep='|')

df_2025 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\raw\TF_SOC_POP_STRUCT_2025.csv", sep='|')

population_2022 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\processed\population_2022.csv", sep=',')
population_2023 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\processed\population_2023.csv", sep=',')
population_2024 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\processed\population_2024.csv", sep=',')
population_2025 = pd.read_csv(r"C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\processed\population_2025.csv", sep=',')

#TasKS
#Removing unnecessary columns
def columns_remover(df1):
  columns_bin = [col for col in df1.columns if col.endswith("FR")]
  df1 = df1.drop(columns=columns_bin)
  return df1
      
population_2021 = columns_remover(df_2021)
population_2022 = columns_remover(df_2022)
population_2023 = columns_remover(df_2023)
population_2024 = columns_remover(df_2024)
population_2025 = columns_remover(df_2025)

population_2021.columns

#Sorting people by area: Flanders
def sort_dataframe(df):
  df = df[df["TX_RGN_DESCR_NL"].str.match("Vlaams Gewest")]
  return df

population_2021 = sort_dataframe(population_2021)
population_2022 = sort_dataframe(population_2022)
population_2023 = sort_dataframe(population_2023)
population_2024 = sort_dataframe(population_2024)
population_2025 = sort_dataframe(population_2025)

population_2021.head(50)

#Saving sorted data
def save_csv(df, file_name):
  df.to_csv(file_name, sep=",", index=False, encoding = "utf-8")
  
save_csv(population_2021, "population_2021_test.csv")

CD_SEX_dict = {"F":"Fem", "M":"Masc"}

population_2022["CD_SEX"] = population_2022["CD_SEX"].replace(CD_SEX_dict)
population_2023["CD_SEX"] = population_2023["CD_SEX"].replace(CD_SEX_dict)
population_2024["CD_SEX"] = population_2024["CD_SEX"].replace(CD_SEX_dict)
population_2025["CD_SEX"] = population_2025["CD_SEX"].replace(CD_SEX_dict)