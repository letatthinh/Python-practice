import os

path ="E:\God of war"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
        #os.path.join(root,file)
		filelist.append(file)

#print all the file names
for name in filelist:
    print(name)