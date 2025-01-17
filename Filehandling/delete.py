# delete file 
import os
os.remove("demofile.txt")
# chack if file is avilabel
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# use for delete folder
import os
os.rmdir("myfolder")