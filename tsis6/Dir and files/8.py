import os

path=r"C:\Users\paras\hello\tsis6\Dir and files\delete"


#           Delete file
# |
if os.path.exists(path) and os.access(path, os.X_OK):
    path=r"C:\Users\paras\hello\tsis6\Dir and files\delete"
    os.chdir(path)
    file_to_delete="Something"
    os.remove(file_to_delete)
else:
    print('Path not found or is not accessible')



#           Create file
# |
# os.chdir(path)
# if not os.path.exists("Something"):
#     with open("Something", 'w') as f:
#         f.close()