# duplicateRowChecker
Python script which takes all csv or xlsx files in two folders and checks if rows exist in one folder but not the other (and vice versa), with the option to create either a) one csv file which containing all duplicate rows, or b) two csv files which contain all unique rows in each folder.

Instructions for use:
1) Group files into Folder1 and Folder2. Files placed in Folder1 will be checked against those in Folder2 and vice versa. 
    a) Ensure all files are in .csv or .xlsx format and all contain the same headers (case-sensitive). Files not in .csv or .xlsx format will be skipped.
    b) Ensure the folder names are not changed.
2) Run duplicateRowChecker.py, in either in an IDE or from the cmd line.