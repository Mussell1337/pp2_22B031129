import os

path=r"C:\Users\paras\hello\tsis6\Dir and files"

if os.path.exists(path):
    file=os.path.basename(path)
    dir=os.path.dirname(path)
    print('Filename: '+file)
    print('Directory: '+dir)
    print()
else:
    print('Not found')