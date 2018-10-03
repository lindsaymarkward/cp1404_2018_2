"""CP1404 Week 10 - os examples"""
import os

# change up one directory
os.chdir('..')
print(os.getcwd())
for directory_name, directories, filenames in os.walk('.'):
    # print(dir_name, directories, files, sep='\n')

    # skip hidden folders
    if directory_name.startswith('./.'):
        continue
    # note that walk does not change directories
    print(os.getcwd())

    # print only the filenames that are not Python code files
    # for filename in filenames:
    #     if not filename.endswith('.py'):
    #         print(filename)

# print(os.listdir('.'))

# EAFP
try:
    os.mkdir('temp')
except FileExistsError as error:
    print("error: {}".format(error))
    print(type(error))

# LBYL
if not os.path.exists('temp'):
    os.mkdir('temp')

print(os.listdir('.'))
