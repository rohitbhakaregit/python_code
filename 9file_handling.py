import os
"""fd=open("file_dummy.txt","a")

print (fd.write("I will show who I am "))
fd.close()



f= open("file_dummy.txt","r")
print (f.readline())
f.close();
"""

fr=open("file_dummy.txt","r")

for l in fr:
	print(l)
fr.close


if os.path.exists("file_dummy.txt"):
	os.remove("file_dummy.txt")