import os
import string

path=r"C:\Users\paras\hello\tsis6\Dir and files"
os.chdir(path)

if not os.path.exists("Letters"):
   os.makedirs("Letters")

path=r"C:\Users\paras\hello\tsis6\Dir and files\chars"
os.chdir(path)

for l in string.ascii_uppercase:
   with open(l + ".txt", "w") as f:
       f.close()