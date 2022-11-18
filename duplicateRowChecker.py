# Python script which takes all csv or xlsx files in two folders and checks if rows exist in one folder but not the other (and vice versa), 
# with the option to create either: 
# a) one csv file which containing all duplicate rows, or 
# b) two csv files which contain all unique rows in each folder, or
# c) no files.

# V 0.1

import os
import warnings
import numpy as np
import pandas as pd
from config.definitions import ROOT_DIR

checklist = os.listdir(ROOT_DIR)
if 'Folder1' not in checklist or 'Folder2' not in checklist:
    print("Folder1/Folder2 missing. Please see README for required directory architecture.")
    print("Goodbye :)")

# Creates dataframe df1 from first csv or xlsx file in Folder1 and appends data from any additional csv or xlsx files in Folder1
filelist = os.listdir(os.path.join(ROOT_DIR,"Folder1"))

# count used to both kill  while loop which checks for an xlsx or csv file in the folder and to set following for loop which appends data from 2nd xlsx/csv files
count = 0
first = 0
while count != len(filelist) and first != 1:
    if filelist[count].endswith('.xlsx'):
        df1 = pd.read_excel(os.path.join(ROOT_DIR,"Folder1",str(filelist[count])))
        first = 1
    elif filelist[count].endswith('.csv'):
        df1 = pd.read_csv(os.path.join(ROOT_DIR,"Folder1",str(filelist[count])))
        first = 1
    else:
        pass
    count += 1
if count == len(filelist):
    print("No .csv or .xlsx files found in Folder1.")
    print("Goodbye :)")
    quit()
else:
    for filename in filelist[count:]:
        if filename.endswith('.xlsx'):
            df_temp = pd.read_excel(os.path.join(ROOT_DIR,"Folder1",str(filename)))
            df1 = df1.append(df_temp)
        elif filename.endswith('.csv'):
            df_temp = pd.read_csv(os.path.join(ROOT_DIR,"Folder1",str(filename)))
            df1 = df1.append(df_temp)
        else:
            pass
print("Folder1 loaded.")

# Creates dataframe df2 from first csv or xlsx file in Folder2 and appends data from any additional csv or xlsx files in Folder1
filelist = os.listdir(os.path.join(ROOT_DIR,"Folder2"))

# count used to both kill  while loop which checks for an xlsx or csv file in the folder and to set following for loop which appends data from 2nd xlsx/csv files
count = 0
first = 0
while count != len(filelist) and first != 1:
    if filelist[count].endswith('.xlsx'):
        df2 = pd.read_excel(os.path.join(ROOT_DIR,"Folder2",str(filelist[count])))
        first = 1
    elif filelist[count].endswith('.csv'):
        df2 = pd.read_csv(os.path.join(ROOT_DIR,"Folder2",str(filelist[count])))
        first = 1
    else:
        pass
    count += 1
if count == len(filelist):
    print("No .csv or .xlsx files found in Folder2.")
    print("Goodbye :)")
    quit()
else:
    for filename in filelist[count:]:
        if filename.endswith('.xlsx'):
            df_temp = pd.read_excel(os.path.join(ROOT_DIR,"Folder2",str(filename)))
            df2 = df2.append(df_temp)
        elif filename.endswith('.csv'):
            df_temp = pd.read_csv(os.path.join(ROOT_DIR,"Folder2",str(filename)))
            df2 = df2.append(df_temp)
        else:
            pass
print("Folder2 loaded.")