import collections


c=collections.Counter()

string=input("Enter the string ")
c.update(string)
print("sequence",c)
