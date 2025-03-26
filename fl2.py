
import os
print("check if the file exists..")
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("The file is not found...")

myfile=open("newfile1.txt", 'w')
myfile.write("hello everyone..good evening...")
myfile.close()    
