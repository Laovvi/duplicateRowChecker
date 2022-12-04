### duplicateRowChecker
Python script which takes all csv or xlsx files in two folders and checks if rows exist in one folder but not the other (and vice versa). An .xlsx is exported which contains a sheet of rows in Folder1 files but not in Folder2 files, a sheet with rows in Folder2 files but not in Folder1 files , and a sheet with rows in both Folder1 and Folder2 files.

V0.9 - Completed but untested

#### Instructions for use:
1. Group files into Folder1 and Folder2. Files placed in Folder1 will be checked against those in Folder2 and vice versa. 
    1. Ensure all files are in .csv or .xlsx format and all contain the same headers (case-sensitive). Files not in .csv or .xlsx format will be skipped.
    2. Ensure the folder names are not changed.
2. Run duplicateRowChecker.py, in either in an IDE or from the cmd line.

###### Sample directory layout:
```bash
C:.
└───duplicateRowChecker
    ├───config
    │   └───definitions.py
    ├───Folder1
    │   ├───file1.csv
    │   └───file2.csv
    ├───Folder2
    │   ├───file1.xlsx
    │   └───file3.csv
    ├───.gitignore
    ├───duplicateRowChecker.py
    ├───LICENSE
    └───README.md
```
