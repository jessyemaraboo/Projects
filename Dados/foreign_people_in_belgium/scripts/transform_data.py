import os
import tkinter as tk

def rename_txt_to_csv(folder):
  for file in os.listdir(folder):
    if file.endswith(".txt"):
      past_path = os.path.join(folder, file)
      new_name = file.replace(".txt", ".csv")
      new_path = os.path.join(folder, new_name)
      
      os.rename(past_path, new_path)
      print(f"Renamed: {file} -> {new_name}")

rename_txt_to_csv(r'C:\Users\jessy\OneDrive\Documentos\Data Analytics\Portfolio\foreign_people_in_belgium\data\raw')