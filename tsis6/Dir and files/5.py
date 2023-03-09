import os

path=r"C:\Users\paras\hello\tsis6\Dir and files"
os.chdir(path)

file_name="New List.txt"
items = ['User', 'Murat', 'OneDrive', 'Rabochiy stol']
with open(file_name, 'w') as f:
    for i in items:
        f.write(i+"\n")
    f.close()