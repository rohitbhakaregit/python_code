string = "rohit Bhakare "

mylist=[]

"""
for letter in string:
	mylist.append(letter)

print mylist

"""# by list compression 

mylist=[ letter for letter in string]
print mylist

mylist = [num for num in range(10,20) if num%2 ==0 ]
print mylist