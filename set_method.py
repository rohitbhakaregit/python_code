"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""


set1=set(("shirt","pant","t-shirt","trouser","jenes"))

set1.add("lungi")
print("output from set1:",set1)

"""
set1.clear()
print("cleared set1 :",set1)

del set1
print("deleted set1 :",set1)
"""

set2=set1.copy();
print("output from set2:",set2)

set2.update(["ramchandra"])                                     #syntax is bit weared []
print("update from set2:",set2)

set3={"gajar","shirt"}

print("difference:" ,set3.difference(set1))       #valible in set3 not avalible in set1
print("intersection",set1.intersection(set3))    # show the common 
set3.intersection_update(set1)                    #remove items wich avalible in Set1 & not avalible in set3
print("intersection_update",set3)
print("symmetric_difference",set1.symmetric_difference(set3))

print("subset:",set3.issubset(set1))
print("isdisjoint:",set1.isdisjoint(set3))  #is two of them are totally different ? 
    